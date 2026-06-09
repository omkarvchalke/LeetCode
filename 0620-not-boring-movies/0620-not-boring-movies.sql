# Write your MySQL query statement below
SELECT * from Cinema 
Where id%2 !=0 AND description != LOWER('boring')
ORDER BY rating DESC;