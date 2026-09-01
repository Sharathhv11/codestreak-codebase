# Write your MySQL query statement below
select distinct e.id,
case 
    when e.p_id is null 
    then "Root"
    when l.p_id is not null
    then "Inner"
    else "Leaf"
end as type 
from Tree e
left join Tree l
on e.id = l.p_id;


