# Write your MySQL query statement below
SELECT class from Courses
group By (class)
HAVING Count(class)>=5;