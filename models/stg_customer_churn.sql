{{ config(materialized='view') }}

with source_data as (
    select * from `telecom-churn-xai.raw_telecom.customer_churn_raw`
)

select
    customerID as customer_id,
    gender,
    SeniorCitizen as is_senior_citizen,
    Partner as has_partner,
    Dependents as has_dependents,
    tenure as tenure_months,
    PhoneService as has_phone_service,
    MultipleLines as multiple_lines,
    InternetService as internet_service,
    OnlineSecurity as online_security,
    OnlineBackup as online_backup,
    DeviceProtection as device_protection,
    TechSupport as tech_support,
    StreamingTV as streaming_tv,
    StreamingMovies as streaming_movies,
    Contract as contract_type,
    PaperlessBilling as has_paperless_billing,
    PaymentMethod as payment_method,
    MonthlyCharges as monthly_charges,
    -- Gestion propre des espaces vides dans TotalCharges
    case 
        when TotalCharges = ' ' then 0.0 
        else cast(TotalCharges as float64) 
    end as total_charges,
    case 
        when Churn = true then 1 
        else 0 
    end as has_churned
from source_data