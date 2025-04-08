-- Active: 1744087694668@@127.0.0.1@3306
-- 001.
SELECT
    Billingcountry, SUM(total)
FROM
    invoices
GROUP BY
    "BillingCountry";

-- 002.
SELECT
    strftime('%Y', InvoiceDate), SUM(total)
FROM
    invoices
GROUP BY
    strftime('%Y', InvoiceDate);

-- 003.

SELECT
    "BillingState", sum(total)
FROM
    invoices
WHERE
    "InvoiceDate" > '2010-01-01'
    AND "BillingCountry" = 'USA'
GROUP BY
    "BillingState"
HAVING
    "BillingState" IS NOT NULL;

-- 004.
SELECT
    "BillingCountry", max(total)
FROM
    invoices
WHERE
    "BillingCountry" in ('Germany', 'France')
GROUP BY
    "BillingCountry"