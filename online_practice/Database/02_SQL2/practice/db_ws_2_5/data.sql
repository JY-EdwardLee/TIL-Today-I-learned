-- Active: 1744096054622@@127.0.0.1@3306
-- 001.
SELECT
    departments.name,
    employees.name,
    max(age),
    avg(age)
FROM
    employees
INNER JOIN
    departments
    ON employees."departmentId" = departments.id
GROUP BY
    departments.name;

-- 002.
SELECT
    departments.name, employees.name, max(salary)
FROM
    employees
INNER JOIN
    departments
    ON employees."departmentId" = departments.id
GROUP BY
    departments.name;

-- 003.
SELECT
    'age_group', count(employees.id)
FROM
    employees
INNER JOIN
    departments
    ON employees."departmentId" = departments.id
GROUP BY
    CASE 
     WHEN age < 30 THEN 'Under 30'
     WHEN 30 <= age AND age < 40 THEN 'BETWEEN 30-40'
     ELSE 'Over 40'
    END AS 'age_group';

SELECT
    CASE 
        WHEN age < 30 THEN 'Under 30'
        WHEN age >= 30 AND age < 40 THEN 'BETWEEN 30-39'
        ELSE 'Over 40'
    END AS age_group,
    COUNT(employees.id) AS employee_count
FROM
    employees
INNER JOIN
    departments
    ON employees."departmentId" = departments.id
GROUP BY age_group
ORDER BY age_group;


