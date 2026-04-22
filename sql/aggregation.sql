-- Summarising data using GROUP BY and aggregate functions


-- How many appointments does each patient have?
select 
    patient_id,
    COUNT(*)          as total_appointments

from healthcare.appointments
GROUP BY patient_id;


-- How many appointments per status? (completed, cancelled etc)
select 
    status,
    COUNT(*)        as total

from healthcare.appointments
GROUP BY status

