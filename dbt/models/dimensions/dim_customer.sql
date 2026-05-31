with base as (
    select * from `thinking-field-468009-s0.churn_telecom.fact_churn`
)
select
    customerID,
    gender,
    SeniorCitizen,
    tenure,
    MonthlyCharges,
    case when Churn = true then 'Churner' else 'Fidèle' end as statut_client
from base