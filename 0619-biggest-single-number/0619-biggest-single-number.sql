# Write your MySQL query statement below
select max(num) as num
from mynumbers
where num in (
    select num
    from mynumbers
    group by num 
    having count(*) = 1
);

#2nd solutation
/*
SELECT MAX(num) AS num
FROM (
    SELECT DISTINCT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS UniqueNumbers;*/