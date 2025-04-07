-- Active: 1743999410801@@127.0.0.1@3306
-- 001.
SELECT
    *
FROM
    users
WHERE
    first_name LIKE '하%';

-- 002.
SELECT
    *
FROM
    users
WHERE
    phone LIKE '%555';    

-- 003.
SELECT
    *
FROM
    users
WHERE
    country LIKE '경상%';

-- 004.
SELECT
    *
FROM
    users
WHERE
    country LIKE '경_남_'
    OR country LIKE '충_남_'