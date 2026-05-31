from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle, pandas as pd, shap, os, random
from typing import Optional

app = FastAPI(
    title="Churn Prediction XAI API",
    description="API prédictive churn — Opérateur Télécom Maroc",
    version="1.0.0"
)
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])

BASE = os.path.dirname(__file__)
with open(os.path.join(BASE, "..", "src", "model.pkl"), "rb") as f:
    model = pickle.load(f)

explainer = shap.TreeExplainer(model)

FEATURES = [
    'gender','SeniorCitizen','Partner','Dependents','tenure',
    'PhoneService','MultipleLines','InternetService','OnlineSecurity',
    'OnlineBackup','DeviceProtection','TechSupport','StreamingTV',
    'StreamingMovies','Contract','PaperlessBilling','PaymentMethod',
    'MonthlyCharges','TotalCharges'
]

class Client(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int
    MonthlyCharges: float
    TotalCharges: float
    model_version: Optional[str] = "v1"

def risque(p):
    if p >= 0.7: return "Risque élevé"
    if p >= 0.4: return "Risque modéré"
    return "Risque faible"

@app.get("/health")
def health():
    return {"status": "API opérationnelle", "version": "1.0.0"}

@app.get("/model/info")
def info():
    return {
        "modele": "LightGBM",
        "AUC_ROC": 0.8439,
        "Accuracy": "78.5%",
        "Recall_churn": "69%",
        "dataset": "IBM Telco 7043 clients",
        "horizon": "J+30"
    }

@app.post("/predict")
def predict(c: Client):
    d = c.dict()
    d.pop("model_version", None)
    df = pd.DataFrame([d], columns=FEATURES)
    proba = float(model.predict_proba(df)[0][1])
    return {
        "probabilite_churn": round(proba, 4),
        "prediction": int(proba >= 0.5),
        "risque": risque(proba),
        "version_modele": c.model_version
    }

@app.post("/explain/shap")
def explain(c: Client):
    d = c.dict()
    d.pop("model_version", None)
    df = pd.DataFrame([d], columns=FEATURES)
    sv = explainer.shap_values(df)
    vals = sv[1][0] if isinstance(sv, list) else sv[0]
    contribs = {f: round(float(v), 4) for f, v in zip(FEATURES, vals)}
    top5 = sorted(contribs.items(), key=lambda x: abs(x[1]), reverse=True)[:5]
    return {
        "shap_values": contribs,
        "top_5_facteurs": [
            {"feature": k, "impact": v,
             "sens": "Augmente risque" if v > 0 else "Réduit risque"}
            for k, v in top5
        ]
    }

@app.post("/ab-test")
def ab_test(c: Client):
    version = "v2" if random.random() >= 0.5 else "v1"
    c.model_version = version
    result = predict(c)
    result["groupe_AB"] = version
    return result