--Key tables:** `patients`, `appointments`, `billing`, `doctors`, `departments`
select * from healthcare.patients

select * from healthcare.doctors

select * from healthcare.billing

select * from healthcare.departments

select * from healthcare.appointments
where status = 'Completed';

--Patients registered after 2023

select * from healthcare.patients
where registered_at > '2023-01-01'
