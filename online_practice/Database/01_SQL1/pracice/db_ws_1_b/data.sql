-- 001.
SELECT
    *
FROM
    songs;

-- 002.
SELECT
    *
FROM
    songs
ORDER BY
    title;

-- 003.
SELECT
    *
FROM
    songs
WHERE
    genre = 'Pop';

-- 004.
SELECT
    *
FROM
    songs
WHERE
    duration >= 3*60;
