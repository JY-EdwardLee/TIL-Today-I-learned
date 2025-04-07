-- Active: 1744000362735@@127.0.0.1@3306
-- 001.
SELECT
    *
FROM
    users
WHERE
    age >= 30
    AND balance >= 1000;

-- 002.
SELECT
    *
FROM
    users
WHERE
    age <= 20
    AND balance <= 1000;

-- 003.
SELECT
    *
FROM
    users
WHERE
    first_name LIKE '현%'
    AND country = '제주특별자치도'
ORDER BY
    age DESC
LIMIT 1;

-- 004.
SELECT 
    *
FROM
    users
WHERE
    last_name = '박'
    AND age >= 25
ORDER BY
    age
LIMIT 1;

-- 005.
SELECT
    *
FROM
    users
WHERE
    first_name in ('재은', '영일')
ORDER BY
    age DESC
LIMIT 1;

-- 006.
SELECT
    *, max(balance)
FROM
    users
GROUP BY
    country
ORDER BY
    balance DESC;

-- 007.
SELECT
    *
FROM
    users
WHERE
    age >= 30
    AND balance > (
        SELECT avg(balance)
        FROM users
        WHERE age >= 30);
-- SELECT
--     first_name, last_name, age, country, phone, balance
-- FROM
--     users, (SELECT avg(balance) AS 'avg_bal_over_30'
--     FROM users
--     WHERE age >= 30) 
-- WHERE
--     age >= 30
--     AND balance > avg_bal_over_30;