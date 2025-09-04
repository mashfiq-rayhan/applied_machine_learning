![MySQL Logo](https://www.mysql.com/common/logos/logo-mysql-170x115.png)

## 🔹 Database Basics

```sql
SHOW DATABASES;                       -- Show all databases
CREATE DATABASE db_name;              -- Create new database
USE db_name;                          -- Switch to database
DROP DATABASE db_name;                -- Delete database
```

---

## 🔹 Table Operations

```sql
SHOW TABLES;                          -- Show all tables

CREATE TABLE users (                  -- Create table
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DESCRIBE users;                       -- Show table structure

RENAME TABLE users TO customers;      -- Rename table
DROP TABLE users;                     -- Delete table

ALTER TABLE users ADD COLUMN age INT; -- Add column
ALTER TABLE users MODIFY age SMALLINT;-- Modify column
ALTER TABLE users DROP COLUMN age;    -- Drop column
```

---

## 🔹 CRUD Operations

```sql
INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com'), ('Bob', 'bob@example.com');

SELECT * FROM users;                  -- Select all
SELECT name, email FROM users;        -- Select specific columns
SELECT * FROM users WHERE age > 25;   -- With condition
SELECT * FROM users ORDER BY created_at DESC; -- Order by
SELECT * FROM users LIMIT 5 OFFSET 10;-- Pagination

UPDATE users SET age = 30 WHERE name = 'Alice'; -- Update
DELETE FROM users WHERE id = 1;                  -- Delete
TRUNCATE TABLE users;                            -- Delete all rows
```

---

## 🔹 Filtering & Conditions

```sql
SELECT * FROM users WHERE age >= 18;              -- WHERE
SELECT * FROM users WHERE age > 18 AND name = 'Alice'; -- AND/OR
SELECT * FROM users WHERE name IN ('Alice', 'Bob');    -- IN
SELECT * FROM users WHERE age BETWEEN 18 AND 30;       -- BETWEEN
SELECT * FROM users WHERE name LIKE 'A%';              -- Starts with A
SELECT * FROM users WHERE email IS NULL;               -- NULL check
```

---

## 🔹 DISTINCT

```sql
SELECT DISTINCT name FROM users;     -- Remove duplicates
```

---

## 🔹 Aggregate Functions

```sql
SELECT COUNT(*) FROM users;          -- Count
SELECT AVG(age) FROM users;          -- Average
SELECT SUM(age) FROM users;          -- Sum
SELECT MIN(age), MAX(age) FROM users;-- Min/Max
```

---

## 🔹 GROUPING & HAVING

```sql
SELECT age, COUNT(*) FROM users GROUP BY age;        -- Group by
SELECT age, COUNT(*) FROM users GROUP BY age HAVING COUNT(*) > 2; -- Having
```

---

## 🔹 Joins

```sql
-- Natural Join
SELECT * FROM users NATURAL JOIN orders;

-- Inner Join
SELECT u.name, o.order_date
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- Left Join
SELECT u.name, o.order_date
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- Right Join
SELECT u.name, o.order_date
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;

-- Outer Join (MySQL simulates with UNION)
SELECT u.name, o.order_date
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.name, o.order_date
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

---

## 🔹 Subqueries (Nested Queries)

```sql
-- Subquery in WHERE
SELECT name FROM users
WHERE id IN (SELECT user_id FROM orders WHERE order_total > 100);

-- Subquery in FROM
SELECT avg_age
FROM (SELECT AVG(age) AS avg_age FROM users) AS sub;

-- Subquery in SELECT
SELECT name, (SELECT COUNT(*) FROM orders o WHERE o.user_id = u.id) AS order_count
FROM users u;
```

---

## 🔹 SQL Execution Order (Keyword Order)

1. **FROM** (choose table)
2. **JOIN** (combine tables)
3. **WHERE** (filter rows)
4. **GROUP BY** (group rows)
5. **HAVING** (filter groups)
6. **SELECT** (choose columns)
7. **DISTINCT** (remove duplicates)
8. **ORDER BY** (sort results)
9. **LIMIT / OFFSET** (return subset)

---

## 🔹 DML (Data Manipulation Language)

```sql
INSERT INTO table_name VALUES (...); -- Insert
UPDATE table_name SET col = val WHERE condition; -- Update
DELETE FROM table_name WHERE condition; -- Delete
```

---

## 🔹 DDL (Data Definition Language)

```sql
CREATE TABLE table_name (...);       -- Create table
ALTER TABLE table_name ADD col_name datatype; -- Alter
DROP TABLE table_name;               -- Drop table
TRUNCATE TABLE table_name;           -- Truncate
```

---

## 🔹 DCL (Data Control Language)

```sql
GRANT ALL PRIVILEGES ON db_name.* TO 'user'@'localhost'; -- Grant
REVOKE ALL PRIVILEGES ON db_name.* FROM 'user'@'localhost'; -- Revoke
```

---

## 🔹 Indexes & Keys

```sql
CREATE INDEX idx_name ON users(name);              -- Index
CREATE UNIQUE INDEX idx_email ON users(email);     -- Unique Index
ALTER TABLE orders ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id);
DROP INDEX idx_name ON users;                      -- Drop index
```

---

## 🔹 User Management

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
SHOW GRANTS FOR 'username'@'localhost';
DROP USER 'username'@'localhost';
```

---

## 🔹 Useful Commands

```sql
SELECT DATABASE();   -- Current database
SELECT USER();       -- Current user
SHOW STATUS;         -- Server status
SHOW VARIABLES;      -- Server variables
```

---

## 🔹 Import & Export

```bash
mysql -u user -p db_name < file.sql      # Import
mysqldump -u user -p db_name > backup.sql # Export
```

```bash

```
