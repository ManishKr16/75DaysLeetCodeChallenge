# Write your MySQL query statement below
select max(salary) as secondHighestsalary
    from employee
    where salary=(select max(salary) from employee
    where salary<(select max(salary) from employee));