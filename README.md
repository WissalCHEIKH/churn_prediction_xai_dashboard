# 📊 Projet  : Tableau de Bord Prédictif de Churn avec Explainable AI (XAI)

## 🎯 Contexte et Objectifs Stratégiques
Ce projet de bout en bout (End-to-End) est conçu pour un opérateur de télécommunications majeur afin de réduire l'attrition client (*Churn*) à J+30. L'objectif final est de fournir un outil d'aide à la décision visuel, interactif et explicable destiné à la **Direction Générale** pour identifier les revenus à risque et piloter les plans de rétention.

---

## 🏗️ L'Architecture du Pipeline Global (Utilité de chaque étape)

Le projet est structuré selon un pipeline de données professionnel où chaque technologie remplit un rôle unique et non-redondant :

1. **Google BigQuery (L'Entrepôt de stockage Cloud) :** C'est le coffre-fort centralisé dans le Cloud. Son but est de stocker et centraliser de manière sécurisée et scalable les millions de lignes de données brutes (logs d'appels, réclamations, données socio-démographiques).
2. **Jupyter Notebook (Le Laboratoire R&D) :** C'est l'espace d'expérimentation de l'ingénieur IA. C'est ici que l'on explore les données (EDA), que l'on entraîne et compare les modèles de Machine Learning (**Random Forest** & **LightGBM**), et que l'on extrait l'explicabilité globale et individuelle (**SHAP / LIME**).
3. **dbt Core (L'Usine de Nettoyage et d'Industrialisation) :** Une fois les règles de données validées dans le notebook, dbt permet d'industrialiser les transformations directement dans BigQuery en SQL. Il transforme la donnée brute en tables propres, documentées et prêtes à l'emploi.
4. **Power BI (La Vitrine Décisionnelle) :** C'est le tableau de bord interactif final. Connecté à la couche de données dbt, il permet au Directeur Général de filtrer par segment client et de manipuler des simulations *What-If* en temps réel.
5. **Vertex AI / MLOps (Cycle de vie & Monitoring) :** Cadre architectural permettant d'automatiser le déploiement des modèles, de réaliser de l'A/B Testing en production et de monitorer le vieillissement des données (*Data/Concept Drift*).

---

## 🗂️ Structure et Organisation du Dépôt
Pour maintenir une collaboration propre en équipe, les fichiers sont organisés comme suit :
* 📁 `models/` & `dbt_project.yml` ➡️ Code des transformations de l'usine de données **dbt**.
* 📄 `chrun-analysis.ipynb` ➡️ Notebook de recherche IA (**Random Forest**, **LightGBM**, **SHAP**).
* 📁 `dashboard/` ➡️ Emplacement du fichier de conception de l'application **Power BI**.




Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
