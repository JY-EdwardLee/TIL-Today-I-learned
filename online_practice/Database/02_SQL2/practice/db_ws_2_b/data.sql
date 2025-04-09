-- Active: 1744086670007@@127.0.0.1@3306
-- 001.
SELECT
    Invoiceid, InvoiceDate
FROM
    invoices;

-- 002.
SELECT
    *
FROM
    invoices
WHERE
    "BillingCountry" = 'USA'
    AND "Total" > 10;

-- 003.
SELECT
    *
FROM
    invoices
WHERE
    "BillingCity" IN ('London', 'Berlin');

-- 004.
SELECT
    *
FROM
    invoices
ORDER BY
    "Total" DESC
LIMIT 1;

-- 005.
SELECT
    *
FROM
    invoices
WHERE
    "InvoiceDate" > '2013-03-31'
    AND "Total" > 3;

-- 006.
SELECT
    *
FROM
    invoices
WHERE
    "BillingCountry" = 'USA'
    AND "BillingState" = 'CA'
    AND "Total" > 10;

-- 007.
SELECT
    *
FROM
    invoices
WHERE
    "BillingCountry" = 'Canada'
    AND "BillingState" = 'ON'
    AND "BillingCity" = 'Toronto';

-- 008.
SELECT
    *
FROM
    invoices
WHERE
    "InvoiceDate" < '2023-01-01'
    AND ("Total" >= 50
    OR "BillingCountry" = 'Brazil');