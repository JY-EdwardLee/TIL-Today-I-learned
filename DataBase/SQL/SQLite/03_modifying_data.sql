-- 0. 사전 작업
-- 공통
SELECT * FROM articles;
DROP TABLE articles;

CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(100) NOT NULL,
    createdAt DATE NOT NULL 
);

PRAGMA table_info('articles');


-- 1. Insert data into table
INSERT INTO articles (title, content, createdAt)
VALUES ('test2', 'content_test2', '1');

INSERT INTO articles (title, content, createdAt)
VALUES
    ('test3', 'content_test3', DATE()),
    ('test4', 'content_test4', DATE());
-- 2. Update data in table
UPDATE articles
SET content = 'content_test_revision'
WHERE title = 'test2';

-- 3. Delete data from table
