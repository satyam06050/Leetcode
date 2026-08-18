# Write your MySQL query statement below
select e.name
from Employee e inner join Employee em
on e.id=em.managerId
group by em.managerId 
having count(em.managerId)>=5
