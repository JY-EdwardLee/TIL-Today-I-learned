-- 001.
SELECT 
    *
FROM
    tracks
WHERE
    name LIKE '%love%';

-- 002.
SELECT
    *
FROM
    tracks
WHERE
    GenreId = 1
    AND Milliseconds >= 300000
ORDER BY
    UnitPrice;

-- 003.
SELECT
    GenreId, SUM(GenreId) AS 'TotalTracks'
FROM
    tracks
GROUP BY
    GenreId

-- 004.
SELECT
    GenreId,
    SUM(UnitPrice) AS 'TotalPrice'
FROM
    tracks
GROUP BY
    GenreId
HAVING
    TotalPrice >= 100;