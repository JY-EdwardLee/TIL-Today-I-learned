-- Active: 1744090414868@@127.0.0.1@3306
-- 001.
SELECT
    *
FROM
    hotels;

-- 002.
UPDATE
    hotels
SET
    grade = UPPER(grade)
WHERE
    True;

-- 003.
SELECT
    grade
FROM
    hotels

-- 004.
CREATE TABLE customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);

-- 005.
CREATE TABLE reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    room_num TEXT NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    FOREIGN KEY (customer_id)
        REFERENCES customers(id)
    FOREIGN KEY (room_num)
        REFERENCES hotels(room_num)
);

INSERT INTO
    customers (name, email)
VALUES
    ('홍길동', 'john@exampl.com'),
    ('박지영', 'jane@exampl.com'),
    ('김미영', 'alice@exampl.com'),
    ('이철수', 'bob@exampl.com');

INSERT INTO
reservations (customer_id, room_num, check_in, check_out) 
VALUES 
    ('1', '101', '2024-03-20', '2024-03-25'),
    ('2', '202', '2024-03-21', '2024-03-24'),
    ('3', '303', '2024-03-22', '2024-03-26'),
    ('4', '404', '2024-03-23', '2024-03-27');

SELECT
    *
FROM
    customers;
SELECT
    *
FROM
    reservations;
