-- Active: 1743994901517@@127.0.0.1@3306
-- 001.
SELECT *
FROM users;

-- 002.
SELECT
    *
FROM
    users
WHERE
    age < 18;

-- 003.
SELECT
    age, phone
FROM
    users
WHERE
    age < 18;
