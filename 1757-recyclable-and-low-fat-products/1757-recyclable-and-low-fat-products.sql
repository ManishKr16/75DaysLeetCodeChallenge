# Write your MySQL query statement below
select product_id 
from products
where low_fats = 'y' and recyclable = 'y' 
order by product_id ;