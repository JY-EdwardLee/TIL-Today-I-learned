-- Active: 1744012774245@@127.0.0.1@3306
-- Table 구조 확인
PRAGMA table_info('preview_copy');

-- 1. Create a table
CREATE TABLE preview(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);
-- 2. Modifying table fields
-- 2.1 ADD COLUMN
ALTER TABLE
    preview
ADD COLUMN
    additional_Name VARCHAR(50) NOT NULL;
ALTER TABLE
    preview
ADD COLUMN
    Country VARCHAR(100) NOT NULL;
ALTER TABLE
    preview
ADD COLUMN
    Age INTEGER NOT NULL DEFAULT 0;
ALTER TABLE
    preview
ADD COLUMN
    Adress VARCHAR(100) NOT NULL DEFAULT 'default';

-- sqlite는 단일 문을 사용하여 한번에 여러 열을 추가하는 것을 지원하지 않음

-- 2.2 RENAME COLUMN
ALTER TABLE
    preview
RENAME COLUMN
    country TO Country;
-- 2.3 RENAME TO

-- 3. Delete a table
ALTER TABLE
    preview
DROP COLUMN
    additional_Name;
ALTER TABLE
    preview
DROP COLUMN
    Adress;

-- sqlite는 컬럼 수정 불가
-- 대신 테이블의 이름을 바꾸고, 새 테이블을 만들고 데이터를 새 테이블에 복사하는 방식을 사용
ALTER TABLE
    preview
RENAME TO
    preview_copy

DROP TABLE preview_copy