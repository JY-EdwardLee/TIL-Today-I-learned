-- Active: 1744089306504@@127.0.0.1@3306
-- 001.
ALTER TABLE
    zoo
ADD COLUMN
    species VARCHAR;

--002.
UPDATE ZOO
SET species = CASE name
    WHEN 'Lion' THEN 'Panthera leo'
    WHEN 'Elephant' THEN 'Loxodonta africana'
    WHEN 'Giraffe' THEN 'Giraffa camelopardails'
    WHEN 'Monkey' THEN 'Cebus capucinus'
    ELSE species
END
WHERE name IN ('Lion', 'Elephant', 'Giraffe', 'Monkey');
-- UPDATE
--     ZOO
-- SET
--     species = 'Panthera leo'
-- WHERE
--     name = 'Lion';

-- UPDATE
--     ZOO
-- SET
--     species = 'Loxodonta africana'
-- WHERE
--     name = 'Elephant';

-- UPDATE
--     ZOO
-- SET
--     species = 'Giraffa camelopardails'
-- WHERE
--     name = 'Giraffe';

-- UPDATE
--     ZOO
-- SET
--     species = 'Cebus capucinus'
-- WHERE
--     name = 'Monkey';

-- 003.
UPDATE
    zoo
SET
    height = height * 2.54
WHERE
    name IN ('Lion', 'Elephant', 'Giraffe', 'Monkey');

-- 004.
SELECT
    *
FROM
    zoo;