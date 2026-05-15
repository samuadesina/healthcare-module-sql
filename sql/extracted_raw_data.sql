WITH patient_spend AS (
    SELECT
        p.patient_id,
        p.first_name || ' ' || p.last_name  AS patient_name,
        SUM(b.amount_charged)               AS total_billed
    FROM healthcare.patients p
    JOIN healthcare.appointments a  ON a.patient_id     = p.patient_id
    JOIN healthcare.billing b       ON b.appointment_id = a.appointment_id
    GROUP BY p.patient_id, p.first_name, p.last_name
),

patient_ranked AS (
    SELECT
        patient_name,
        total_billed,
        RANK() OVER (ORDER BY total_billed DESC) AS spend_rank
    FROM patient_spend
),

running_total AS (
    SELECT
        p.first_name || ' ' || p.last_name  AS patient_name,
        a.appointment_date,
        b.amount_charged                    AS billed_amount,
        b.payment_status,
        SUM(b.amount_charged) OVER (
            ORDER BY a.appointment_date
        )                                   AS running_total
    FROM healthcare.patients p
    JOIN healthcare.appointments a  ON a.patient_id     = p.patient_id
    JOIN healthcare.billing b       ON b.appointment_id = a.appointment_id
    ORDER BY a.appointment_date
)

SELECT
    rt.patient_name,
    rt.appointment_date,
    rt.billed_amount,
    rt.payment_status,
    rt.running_total,
    pr.total_billed,
    pr.spend_rank
FROM running_total rt
JOIN patient_ranked pr ON pr.patient_name = rt.patient_name
ORDER BY rt.appointment_date;