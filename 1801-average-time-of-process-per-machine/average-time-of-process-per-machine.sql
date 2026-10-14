# Write your MySQL query statement below
select s.machine_id,ROUND(AVG(e.timestamp-s.timestamp),3) AS processing_time
from Activity s
join Activity e
ON s.machine_id = e.machine_id                             -- fix 3: real matching rule
AND s.process_id = e.process_id
where s.activity_type='start'
AND e.activity_type='end'
group by s.machine_id;