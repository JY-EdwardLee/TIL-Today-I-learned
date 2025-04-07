-- Active: 1743994382062@@127.0.0.1@3306
SELECT
    genre, duration, COUNT(genre)
FROM
    songs
GROUP BY
    genre;