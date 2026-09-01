# Write your MySQL query statement below
select s.id,e.student
from Seat s
left join Seat e
on (s.id%2=1 and s.id+1 = e.id ) or (s.id%2=0 and s.id-1 = e.id)
where e.student is not null

union all


select id,student 
from Seat
where id = (select max(id) from Seat) and (select count(*) from Seat) %2 = 1;
