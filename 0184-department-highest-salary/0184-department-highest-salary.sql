# Write your MySQL query statement below
SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM Employee E 
    JOIN Department D
    on E.departmentId = D.id
WHERE (E.departmentId, E.salary) IN (SELECT departmentId, MAX(salary) FROM Employee GROUP BY departmentId)