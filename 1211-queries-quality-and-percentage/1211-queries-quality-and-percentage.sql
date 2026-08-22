# Write your MySQL query statement below
select q.query_name,round(avg(q.rating/q.position),2) as quality,
ROUND(
        SUM(q.rating < 3) / COUNT(*) * 100,
        2
    ) AS poor_query_percentage
from Queries q
group by q.query_name