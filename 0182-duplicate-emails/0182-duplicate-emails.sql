# Write your MySQL query statement below
SELECT email
FROm Person
Group by (email)
HAVING COUNT(email) > 1;