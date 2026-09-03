# Write your MySQL query statement below
select t.person_name
from (
    select person_name,
    turn,
    sum(weight) over (order by turn) as cumm
    from Queue
) t

where t.cumm <= 1000
order by t.cumm desc
limit 1;