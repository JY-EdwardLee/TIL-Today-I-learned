-- 001.
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATE NOT NULL,
    total_amount REAL NOT NULL
);
INSERT INTO 
    orders (order_id, order_date, total_amount)
VALUES
    ('1', '2023-07-15', '50.99'),
    ('2', '2023-07-16', '75.5'),
    ('3', '2023-07-17', '30.25');

-- 002.
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    phone INTEGERNOT NULL
);

INSERT INTO 
    customers ('name', 'email', 'phone')
VALUES
    ('허균', 'hong.hilfong@examp.com', '010-2022-1010'),
    ('김영희', 'kim.tyokong@examp.com', '010-4356-2541'),
    ('이철수', 'lee.cheolsu@examp.com', '010-8461-4035');

-- 003.
DELETE FROM orders
WHERE
    order_id  = 3;

UPDATE customers
SET name = '홍길동'
WHERE
    customer_id = 1;

-- 004.
SELECT *
FROM orders;

SELECT *
FROM customers;