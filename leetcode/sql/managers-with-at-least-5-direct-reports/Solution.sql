# Write your MySQL query statement below
select e.name
from Employee e
inner join Employee l
on e.id = l.managerId
group by e.id
having count(*) >= 5;