-- Active: 1743999050042@@127.0.0.1@3306
-- 001.
SELECT
    *
FROM
    users
WHERE
    age < 18
ORDER BY
    age DESC;

-- 002.
SELECT
    last_name, age
FROM
    users
WHERE
    age < 18
ORDER BY
    last_name,
    age DESC

-- 003.
SELECT DISTINCT
    last_name, age
FROM
    users
WHERE
    age < 18
ORDER BY
    last_name,
    age DESC
