-- Active: 1744095323935@@127.0.0.1@3306
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    amount TEXT NOT NULL,
    transaction_date DATE NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES users(id)
);

INSERT INTO
    transactions (user_id, amount, transaction_date)
VALUES
    ('1', 500, '2024-03-15'),
    ('2', 700, '2024-03-16'),
    ('1', 200, '2024-03-17'),
    ('3', 1000, '2024-03-18');

SELECT
    first_name, last_name, amount, transaction_date
FROM
    users
INNER JOIN transactions
ON users.id = transactions.user_id;

SELECT
    first_name, last_name, amount, transaction_date
FROM
    users
INNER JOIN transactions
ON users.id = transactions.user_id
WHERE
    transaction_date > '2024-03-16';

SELECT
    first_name, last_name, sum(amount)
FROM
    users
INNER JOIN transactions
    ON users.id = transactions.user_id
GROUP BY
    transactions.user_id