-- Active: 1744086125512@@127.0.0.1@3306
-- 001.
SELECT *
FROM artists;

-- 002.
SELECT Name, count(Name)
FROM artists
GROUP BY Name;

-- 003.
SELECT *
FROM artists
WHERE artists.Name = 'AC/DC';

-- 004.
SELECT artistid, Name
FROM artists;

-- 005.
SELECT *
FROM artists
WHERE
    Name in ('Gilberto Gil', 'Ed Motta');

-- 006.
SELECT *
FROM artists
ORDER BY
    Name DESC;

-- 007.
SELECT *
FROM artists
WHERE
    Name like 'Vinicius%'
LIMIT 2;

-- 008.
SELECT "ArtistId"
FROM artists
ORDER BY
    "ArtistId"
LIMIT 49, 21;