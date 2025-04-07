-- 001.
SELECT 
    *
FROM
    tracks;

-- 002.
SELECT
    Name, Milliseconds, UnitPrice
FROM
    tracks;

-- 003.
SELECT
    *
FROM
    tracks
WHERE
    "GenreId" = 1;

-- 004.
SELECT
    *
FROM
    tracks
ORDER BY
    name;

-- 005.
SELECT
    *
FROM
    tracks
LIMIT 10;