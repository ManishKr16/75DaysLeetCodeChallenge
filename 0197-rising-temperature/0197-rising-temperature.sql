# Write your MySQL query statement below
SELECT W1.ID 
FROM WEATHER W1
JOIN Weather w2 
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;