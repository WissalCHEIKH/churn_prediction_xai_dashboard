with base as (
    select * from `thinking-field-468009-s0.churn_telecom.fact_churn`
)
select
    customerID,
    gender,
    SeniorCitizen,
    tenure,
    MonthlyCharges,
    Contract,
    InternetService,
    PaymentMethod,
    case when Churn = true then 1 else 0 end as churn_label,
    case
        when tenure <= 12 then 'Nouveau (0-12 mois)'
        when tenure <= 36 then 'Intermédiaire (1-3 ans)'
        when tenure <= 60 then 'Fidèle (3-5 ans)'
        else 'Très fidèle (5+ ans)'
    end as tenure_segment,
    case
        when MonthlyCharges < 35 then 'Faible'
        when MonthlyCharges < 65 then 'Moyen'
        when MonthlyCharges < 85 then 'Élevé'
        else 'Premium'
    end as charge_segment,
    case
        when Contract = 'Month-to-month' then 'Risque élevé'
        when Contract = 'One year' then 'Risque modéré'
        else 'Risque faible'
    end as contract_risk
from base