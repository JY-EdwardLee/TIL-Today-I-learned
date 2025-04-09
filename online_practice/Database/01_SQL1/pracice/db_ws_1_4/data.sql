-- Active: 1743999927151@@127.0.0.1@3306
-- 001.
SELECT
    AVG(age) AS 'average_age'
FROM
    users;

-- 002.
SELECT
    country, COUNT(country)
FROM
    users
GROUP BY
    country;

-- 003.
SELECT
    *
FROM
    users
ORDER BY
    balance DESC
LIMIT 1;

-- 004.
SELECT
    country, AVG(balance)
FROM
    users
GROUP BY
    country;

-- 005.
SELECT
    MAX(balance) - MIN(balance) as 'balance_diff'
FROM
    users;