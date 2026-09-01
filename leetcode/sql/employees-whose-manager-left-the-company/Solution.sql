# Write your MySQL query statement below

select employee_id 
from Employees 
where  salary < 30000 and manager_id in (
    select e.manager_id
    from Employees e
    left join Employees l
    on e.manager_id = l.employee_id
    where e.manager_id is not null and l.employee_id is null
)
order by employee_id;
