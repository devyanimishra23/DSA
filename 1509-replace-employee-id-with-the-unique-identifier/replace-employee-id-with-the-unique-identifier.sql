# Write your MySQL query statement below
SELECT unique_id,name
From employees e
left join EmployeeUNI eu
ON e.id=eu.id;