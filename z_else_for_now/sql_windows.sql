--* play with Win Function


-- example 1 - Calculate Running Totals - no partition
SELECT date, sales, sum(sales) OVER (ORDER BY date) AS running_total
FROM sales_data;

-- example 2 - Find the top N values 
-- first get the info precursor to displaying
WITH RankedEmployees AS (
    SELECT name, dept, salary, RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS emp_rank
    FROM employees
)git pull 
-- now just display what we want to see end result
SELECT name, dept, salary
FROM RankedEmployees
WHERE rank <= 3;     


-- another
SELECT name, dept, salary, AVG(salary) OVER (PARTITION BY dept) AS avg_dept_salary
FROM employees;

-- another
SELECT name, dept, salary, RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS emp_rank
FROM employees;

-- generally I prefer DENSE_RANK

-- a row number one
SELECT name, dept, salary, ROW_NUMBER() OVER (PARTITION by dept ORDER BY salary DESC) AS emp_row_no
FROM employees;


