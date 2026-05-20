# Write your MySQL query statement below
Select e2.name AS Employee from employee e1
INNER JOIN employee e2 on e1.id = e2.managerID
where e1.salary < e2.salary