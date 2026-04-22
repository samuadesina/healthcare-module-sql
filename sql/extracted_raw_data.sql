SELECT
    p.first_name || ' ' || p.last_name  AS patient_name,
    a.appointment_date,
    a.status,
    d.first_name || ' ' || d.last_name  AS doctor_name,
    d.specialization,
    b.amount_charged                    AS billed_amount,
    b.patient_paid,
    b.payment_status,
    dep.dept_name                       AS department
FROM healthcare.patients p
JOIN healthcare.appointments a  ON a.patient_id     = p.patient_id
JOIN healthcare.doctors d       ON d.doctor_id      = a.doctor_id
JOIN healthcare.departments dep ON dep.dept_id      = d.dept_id
LEFT JOIN healthcare.billing b  ON b.appointment_id = a.appointment_id
ORDER BY a.appointment_date;