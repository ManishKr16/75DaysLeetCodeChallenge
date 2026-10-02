# Write your MySQL query statement below

# Method 1
-- select max(salary) as secondHighestsalary
--     from employee
--     where salary=(select max(salary) from employee
--     where salary<(select max(salary) from employee));

# Method 2

SELECT (
    SELECT DISTINCT salary
    FROM employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS secondhighestsalary;