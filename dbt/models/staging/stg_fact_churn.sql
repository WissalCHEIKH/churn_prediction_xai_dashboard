with source as (
    select * from `thinking-field-468009-s0.churn_telecom.fact_churn`
),
cleaned as (
    select
        customerID,
        gender,
        SeniorCitizen,
        tenure,
        MonthlyCharges,
        cast(TotalCharges as FLOAT64) as TotalCharges,
        Contract,
        InternetService,
        PaymentMethod,
        case when Churn = true then 1 else 0 end as churn_label
    from source
)
select * from cleaned