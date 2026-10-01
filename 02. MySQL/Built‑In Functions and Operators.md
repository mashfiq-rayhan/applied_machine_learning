<img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" alt="MySQL Logo" width="240" />

# 🐬 Built-In Functions and Operators

## 📑 Table of Contents

- [⚙️ Operators](#operators)
- [🔤 String Functions](#string-functions)
- [🔢 Numeric Functions](#numeric-functions)
- [📅 Date and Time Functions](#date-and-time-functions)
- [📊 Aggregate Functions](#aggregate-functions)
- [🪟 Window Functions](#window-functions)
- [📋 JSON Functions](#json-functions)
- [🌍 Spatial Functions](#spatial-functions)
- [⚖️ Comparison Functions](#comparison-functions)
- [🔀 Control Flow Functions](#control-flow-functions)
- [ℹ️ Information Functions](#information-functions)
- [🔐 Encryption and Compression](#encryption-and-compression)
- [🔒 Locking Functions](#locking-functions)
- [🔍 Regular Expression Functions](#regular-expression-functions)
- [🔄 Replication Functions](#replication-functions)
- [📄 XML Functions](#xml-functions)
- [🛠️ Miscellaneous Functions](#miscellaneous-functions)

---

## ⚙️ Operators

| Name                    | Description                                                                                                               | Usage Example                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| &                       | Bitwise AND                                                                                                               | `SELECT a & b;`                                    |
| >                       | Greater than operator                                                                                                     | `SELECT a > b;`                                    |
| >>                      | Right shift                                                                                                               | `SELECT a >> b;`                                   |
| >=                      | Greater than or equal operator                                                                                            | `SELECT a >= b;`                                   |
| <                       | Less than operator                                                                                                        | `SELECT a < b;`                                    |
| <>, !=                  | Not equal operator                                                                                                        | `SELECT a <> b;`                                   |
| <<                      | Left shift                                                                                                                | `SELECT a << b;`                                   |
| <=                      | Less than or equal operator                                                                                               | `SELECT a <= b;`                                   |
| <=>                     | NULL-safe equal to operator                                                                                               | `SELECT a <=> b;`                                  |
| %, MOD                  | Modulo operator                                                                                                           | `SELECT a % b;`                                    |
| \*                      | Multiplication operator                                                                                                   | `SELECT a * b;`                                    |
| +                       | Addition operator                                                                                                         | `SELECT a + b;`                                    |
| -                       | Minus operator                                                                                                            | `SELECT a - b;`                                    |
| - (unary)               | Change the sign of the argument                                                                                           | `SELECT -a;`                                       |
| ->                      | Return value from JSON column after evaluating path; equivalent to JSON_EXTRACT().                                        | `SELECT a -> '$.x';`                               |
| ->>                     | Return value from JSON column after evaluating path and unquoting the result; equivalent to JSON_UNQUOTE(JSON_EXTRACT()). | `SELECT a ->> '$.x';`                              |
| /                       | Division operator                                                                                                         | `SELECT a / b;`                                    |
| :=                      | Assign a value                                                                                                            | `SET @a := 1;`                                     |
| =                       | Assign a value (as part of a SET statement, or as part of the SET clause in an UPDATE statement)                          | `UPDATE my_table SET col = 1 WHERE id = 1;`        |
| =                       | Equal operator                                                                                                            | `SELECT a = b;`                                    |
| ^                       | Bitwise XOR                                                                                                               | `SELECT a ^ b;`                                    |
| \|                      | Bitwise OR                                                                                                                | `SELECT a \| b;`                                    |
| ~                       | Bitwise inversion                                                                                                         | `SELECT ~a;`                                       |
| AND, &&                 | Logical AND                                                                                                               | `SELECT a AND b;`                                  |
| OR, \|\|                | Logical OR                                                                                                                | `SELECT a OR b;`                                   |
| NOT, !                  | Negates value                                                                                                             | `SELECT NOT a;`                                    |
| XOR                     | Logical XOR                                                                                                               | `SELECT a XOR b;`                                  |
| BETWEEN ... AND ...     | Whether a value is within a range of values                                                                               | `SELECT * FROM t WHERE x BETWEEN 1 AND 10;`        |
| NOT BETWEEN ... AND ... | Whether a value is not within a range of values                                                                           | `SELECT * FROM t WHERE x NOT BETWEEN 1 AND 10;`    |
| IN()                    | Whether a value is within a set of values                                                                                 | `SELECT * FROM t WHERE x IN (1,2,3);`              |
| NOT IN()                | Whether a value is not within a set of values                                                                             | `SELECT * FROM t WHERE x NOT IN (1,2,3);`          |
| IS                      | Test a value against a boolean                                                                                            | `SELECT a IS TRUE;`                                |
| IS NOT                  | Test a value against a boolean                                                                                            | `SELECT a IS NOT TRUE;`                            |
| IS NULL                 | NULL value test                                                                                                           | `SELECT * FROM t WHERE col IS NULL;`               |
| IS NOT NULL             | NOT NULL value test                                                                                                       | `SELECT * FROM t WHERE col IS NOT NULL;`           |
| LIKE                    | Simple pattern matching                                                                                                   | `SELECT * FROM t WHERE col LIKE 'abc%';`           |
| NOT LIKE                | Negation of simple pattern matching                                                                                       | `SELECT * FROM t WHERE col NOT LIKE 'abc%';`       |
| REGEXP                  | Whether string matches regular expression                                                                                 | `SELECT col REGEXP '^[0-9]+$';`                    |
| NOT REGEXP              | Negation of REGEXP                                                                                                        | `SELECT col NOT REGEXP '^[0-9]+$';`                |
| RLIKE                   | Whether string matches regular expression                                                                                 | `SELECT col RLIKE '^[0-9]+$';`                     |
| DIV                     | Integer division                                                                                                          | `SELECT 7 DIV 2;`                                  |
| CASE                    | Case operator                                                                                                             | `SELECT CASE WHEN a > 0 THEN 'yes' ELSE 'no' END;` |
| INTERVAL()              | Return the index of the argument that is less than the first argument                                                     | `SELECT INTERVAL(10, 1, 5, 15);`                   |
| MEMBER OF()             | Returns true (1) if first operand matches any element of JSON array passed as second operand, otherwise returns false (0) | `SELECT 'a' MEMBER OF (JSON_ARRAY('a','b'));`      |

---

## 🔤 String Functions

| Name               | Description                                                                                                                        | Usage Example                            |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| ASCII()            | Return numeric value of left-most character                                                                                        | `SELECT ASCII('A');`                     |
| BIN()              | Return a string containing binary representation of a number                                                                       | `SELECT BIN(7);`                         |
| BIT_LENGTH()       | Return length of argument in bits                                                                                                  | `SELECT BIT_LENGTH('abc');`              |
| CHAR()             | Return the character for each integer passed                                                                                       | `SELECT CHAR(65);`                       |
| CHAR_LENGTH()      | Return number of characters in argument                                                                                            | `SELECT CHAR_LENGTH('abc');`             |
| CHARACTER_LENGTH() | Synonym for CHAR_LENGTH()                                                                                                          | `SELECT CHARACTER_LENGTH('abc');`        |
| CHARSET()          | Return the character set of the argument                                                                                           | `SELECT CHARSET('abc');`                 |
| COERCIBILITY()     | Return the collation coercibility value of the string argument                                                                     | `SELECT COERCIBILITY('abc');`            |
| COLLATION()        | Return the collation of the string argument                                                                                        | `SELECT COLLATION('abc');`               |
| CONCAT()           | Return concatenated string                                                                                                         | `SELECT CONCAT('a','b');`                |
| CONCAT_WS()        | Return concatenate with separator                                                                                                  | `SELECT CONCAT_WS('-', 'a', 'b');`       |
| ELT()              | Return string at index number                                                                                                      | `SELECT ELT(2, 'a','b','c');`            |
| EXPORT_SET()       | Return a string such that for every bit set in the value bits, you get an on string and for every unset bit, you get an off string | `SELECT EXPORT_SET(5,'Y','N');`          |
| FIELD()            | Index (position) of first argument in subsequent arguments                                                                         | `SELECT FIELD('b','a','b','c');`         |
| FIND_IN_SET()      | Index (position) of first argument within second argument                                                                          | `SELECT FIND_IN_SET('b','a,b,c');`       |
| FORMAT()           | Return a number formatted to specified number of decimal places                                                                    | `SELECT FORMAT(1234.56,2);`              |
| HEX()              | Hexadecimal representation of decimal or string value                                                                              | `SELECT HEX('abc');`                     |
| INSERT()           | Insert substring at specified position up to specified number of characters                                                        | `SELECT INSERT('abc',2,1,'Z');`          |
| INSTR()            | Return the index of the first occurrence of substring                                                                              | `SELECT INSTR('abc','b');`               |
| LCASE()            | Synonym for LOWER()                                                                                                                | `SELECT LCASE('ABC');`                   |
| LEFT()             | Return the leftmost number of characters as specified                                                                              | `SELECT LEFT('abc',2);`                  |
| LENGTH()           | Return the length of a string in bytes                                                                                             | `SELECT LENGTH('abc');`                  |
| LOAD_FILE()        | Load the named file                                                                                                                | `SELECT LOAD_FILE('/path/file');`        |
| LOCATE()           | Return the position of the first occurrence of substring                                                                           | `SELECT LOCATE('b','abc');`              |
| LOWER()            | Return the argument in lowercase                                                                                                   | `SELECT LOWER('ABC');`                   |
| LPAD()             | Return the string argument, left-padded with the specified string                                                                  | `SELECT LPAD('abc',5,'0');`              |
| LTRIM()            | Remove leading spaces                                                                                                              | `SELECT LTRIM('  abc');`                 |
| MAKE_SET()         | Return a set of comma-separated strings that have the corresponding bit in bits set                                                | `SELECT MAKE_SET(5,'a','b','c');`        |
| MID()              | Return a substring starting from the specified position                                                                            | `SELECT MID('abc',2,1);`                 |
| OCT()              | Return a string containing octal representation of a number                                                                        | `SELECT OCT(8);`                         |
| OCTET_LENGTH()     | Synonym for LENGTH()                                                                                                               | `SELECT OCTET_LENGTH('abc');`            |
| ORD()              | Return character code for leftmost character of the argument                                                                       | `SELECT ORD('A');`                       |
| POSITION()         | Synonym for LOCATE()                                                                                                               | `SELECT POSITION('b' IN 'abc');`         |
| QUOTE()            | Escape the argument for use in an SQL statement                                                                                    | `SELECT QUOTE("I'm");`                   |
| REPEAT()           | Repeat a string the specified number of times                                                                                      | `SELECT REPEAT('a',3);`                  |
| REPLACE()          | Replace occurrences of a specified string                                                                                          | `SELECT REPLACE('abc','b','Z');`         |
| REVERSE()          | Reverse the characters in a string                                                                                                 | `SELECT REVERSE('abc');`                 |
| RIGHT()            | Return the specified rightmost number of characters                                                                                | `SELECT RIGHT('abc',2);`                 |
| RPAD()             | Append string the specified number of times                                                                                        | `SELECT RPAD('abc',5,'0');`              |
| RTRIM()            | Remove trailing spaces                                                                                                             | `SELECT RTRIM('abc  ');`                 |
| SOUNDEX()          | Return a soundex string                                                                                                            | `SELECT SOUNDEX('abc');`                 |
| SOUNDS LIKE        | Compare sounds                                                                                                                     | `SELECT 'Robert' SOUNDS LIKE 'Rupert';`  |
| SPACE()            | Return a string of the specified number of spaces                                                                                  | `SELECT SPACE(3);`                       |
| STRCMP()           | Compare two strings                                                                                                                | `SELECT STRCMP('a','b');`                |
| SUBSTR()           | Return the substring as specified                                                                                                  | `SELECT SUBSTR('abc',2);`                |
| SUBSTRING()        | Return the substring as specified                                                                                                  | `SELECT SUBSTRING('abc',2);`             |
| SUBSTRING_INDEX()  | Return a substring from a string before the specified number of occurrences of the delimiter                                       | `SELECT SUBSTRING_INDEX('a,b,c',',',2);` |
| TRIM()             | Remove leading and trailing spaces                                                                                                 | `SELECT TRIM('  abc  ');`                |
| UCASE()            | Synonym for UPPER()                                                                                                                | `SELECT UCASE('abc');`                   |
| UNHEX()            | Return a string containing hex representation of a number                                                                          | `SELECT UNHEX('4D');`                    |
| UPPER()            | Convert to uppercase                                                                                                               | `SELECT UPPER('abc');`                   |
| WEIGHT_STRING()    | Return the weight string for a string                                                                                              | `SELECT WEIGHT_STRING('abc');`           |

---

## 🔢 Numeric Functions

| Name       | Description                                               | Usage Example               |
| ---------- | --------------------------------------------------------- | --------------------------- |
| ABS()      | Return the absolute value                                 | `SELECT ABS(-5);`           |
| ACOS()     | Return the arc cosine                                     | `SELECT ACOS(0.5);`         |
| ASIN()     | Return the arc sine                                       | `SELECT ASIN(0.5);`         |
| ATAN()     | Return the arc tangent                                    | `SELECT ATAN(1);`           |
| ATAN2()    | Return the arc tangent of the two arguments               | `SELECT ATAN2(1,1);`        |
| CEIL()     | Return the smallest integer value not less than the arg   | `SELECT CEIL(1.2);`         |
| CEILING()  | Return the smallest integer value not less than the arg   | `SELECT CEILING(1.2);`      |
| CONV()     | Convert numbers between different number bases            | `SELECT CONV('a',16,10);`   |
| COS()      | Return the cosine                                         | `SELECT COS(0);`            |
| COT()      | Return the cotangent                                      | `SELECT COT(1);`            |
| CRC32()    | Compute a cyclic redundancy check value                   | `SELECT CRC32('abc');`      |
| DEGREES()  | Convert radians to degrees                                | `SELECT DEGREES(PI());`     |
| DISTANCE() | Calculates the distance between two vectors               | `SELECT DISTANCE(v1, v2);`  |
| EXP()      | Raise to the power of                                     | `SELECT EXP(1);`            |
| FLOOR()    | Return the largest integer value not greater than the arg | `SELECT FLOOR(1.9);`        |
| LN()       | Return the natural logarithm of the argument              | `SELECT LN(2);`             |
| LOG()      | Return the natural logarithm of the first argument        | `SELECT LOG(2);`            |
| LOG10()    | Return the base-10 logarithm of the argument              | `SELECT LOG10(100);`        |
| LOG2()     | Return the base-2 logarithm of the argument               | `SELECT LOG2(8);`           |
| MOD()      | Return the remainder                                      | `SELECT MOD(7,2);`          |
| PI()       | Return the value of pi                                    | `SELECT PI();`              |
| POW()      | Return the argument raised to the specified power         | `SELECT POW(2,3);`          |
| POWER()    | Return the argument raised to the specified power         | `SELECT POWER(2,3);`        |
| RADIANS()  | Return argument converted to radians                      | `SELECT RADIANS(180);`      |
| RAND()     | Return a random floating-point value                      | `SELECT RAND();`            |
| ROUND()    | Round the argument                                        | `SELECT ROUND(1.234,2);`    |
| SIGN()     | Return the sign of the argument                           | `SELECT SIGN(-5);`          |
| SIN()      | Return the sine of the argument                           | `SELECT SIN(0);`            |
| SQRT()     | Return the square root of the argument                    | `SELECT SQRT(9);`           |
| TAN()      | Return the tangent of the argument                        | `SELECT TAN(1);`            |
| TRUNCATE() | Truncate to specified number of decimal places            | `SELECT TRUNCATE(1.234,2);` |

---

## 📅 Date and Time Functions

| Name                                   | Description                                                                       | Usage Example                                            |
| -------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------- |
| ADDDATE()                              | Add time values (intervals) to a date value                                       | `SELECT ADDDATE('2024-01-01', INTERVAL 1 DAY);`          |
| ADDTIME()                              | Add time                                                                          | `SELECT ADDTIME('10:00:00','01:00:00');`                 |
| CURDATE()                              | Return the current date                                                           | `SELECT CURDATE();`                                      |
| CURRENT_DATE(), CURRENT_DATE           | Synonyms for CURDATE()                                                            | `SELECT CURRENT_DATE();`                                 |
| CURRENT_TIME(), CURRENT_TIME           | Synonyms for CURTIME()                                                            | `SELECT CURRENT_TIME();`                                 |
| CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP | Synonyms for NOW()                                                                | `SELECT CURRENT_TIMESTAMP();`                            |
| CURTIME()                              | Return the current time                                                           | `SELECT CURTIME();`                                      |
| DATE()                                 | Extract the date part of a date or datetime expression                            | `SELECT DATE(NOW());`                                    |
| DATE_ADD()                             | Add time values (intervals) to a date value                                       | `SELECT DATE_ADD('2024-01-01', INTERVAL 7 DAY);`         |
| DATE_FORMAT()                          | Format date as specified                                                          | `SELECT DATE_FORMAT(NOW(), '%Y-%m-%d');`                 |
| DATE_SUB()                             | Subtract a time value (interval) from a date                                      | `SELECT DATE_SUB('2024-01-01', INTERVAL 7 DAY);`         |
| DATEDIFF()                             | Subtract two dates                                                                | `SELECT DATEDIFF('2024-01-10','2024-01-01');`            |
| DAY()                                  | Synonym for DAYOFMONTH()                                                          | `SELECT DAY('2024-01-05');`                              |
| DAYNAME()                              | Return the name of the weekday                                                    | `SELECT DAYNAME('2024-01-05');`                          |
| DAYOFMONTH()                           | Return the day of the month (0-31)                                                | `SELECT DAYOFMONTH('2024-01-05');`                       |
| DAYOFWEEK()                            | Return the weekday index of the argument                                          | `SELECT DAYOFWEEK('2024-01-05');`                        |
| DAYOFYEAR()                            | Return the day of the year (1-366)                                                | `SELECT DAYOFYEAR('2024-01-05');`                        |
| EXTRACT()                              | Extract part of a date                                                            | `SELECT EXTRACT(YEAR FROM NOW());`                       |
| FROM_DAYS()                            | Convert a day number to a date                                                    | `SELECT FROM_DAYS(738885);`                              |
| FROM_UNIXTIME()                        | Format Unix timestamp as a date                                                   | `SELECT FROM_UNIXTIME(1700000000);`                      |
| GET_FORMAT()                           | Return a date format string                                                       | `SELECT GET_FORMAT(DATE,'ISO');`                         |
| HOUR()                                 | Extract the hour                                                                  | `SELECT HOUR('10:11:12');`                               |
| LAST_DAY()                             | Return the last day of the month for the argument                                 | `SELECT LAST_DAY('2024-01-05');`                         |
| LOCALTIME(), LOCALTIME                 | Synonym for NOW()                                                                 | `SELECT LOCALTIME();`                                    |
| LOCALTIMESTAMP, LOCALTIMESTAMP()       | Synonym for NOW()                                                                 | `SELECT LOCALTIMESTAMP();`                               |
| MAKEDATE()                             | Create a date from the year and day of year                                       | `SELECT MAKEDATE(2024, 100);`                            |
| MAKETIME()                             | Create time from hour, minute, second                                             | `SELECT MAKETIME(10,11,12);`                             |
| MICROSECOND()                          | Return the microseconds from argument                                             | `SELECT MICROSECOND('10:11:12.123456');`                 |
| MINUTE()                               | Return the minute from the argument                                               | `SELECT MINUTE('10:11:12');`                             |
| MONTH()                                | Return the month from the date passed                                             | `SELECT MONTH('2024-01-05');`                            |
| MONTHNAME()                            | Return the name of the month                                                      | `SELECT MONTHNAME('2024-01-05');`                        |
| NOW()                                  | Return the current date and time                                                  | `SELECT NOW();`                                          |
| PERIOD_ADD()                           | Add a period to a year-month                                                      | `SELECT PERIOD_ADD(202401, 2);`                          |
| PERIOD_DIFF()                          | Return the number of months between periods                                       | `SELECT PERIOD_DIFF(202403, 202401);`                    |
| QUARTER()                              | Return the quarter from a date argument                                           | `SELECT QUARTER('2024-01-05');`                          |
| SEC_TO_TIME()                          | Converts seconds to 'hh:mm:ss' format                                             | `SELECT SEC_TO_TIME(3661);`                              |
| SECOND()                               | Return the second (0-59)                                                          | `SELECT SECOND('10:11:12');`                             |
| STR_TO_DATE()                          | Convert a string to a date                                                        | `SELECT STR_TO_DATE('2024-01-05','%Y-%m-%d');`           |
| SUBDATE()                              | Synonym for DATE_SUB() when invoked with three arguments                          | `SELECT SUBDATE('2024-01-05', INTERVAL 1 DAY);`          |
| SUBTIME()                              | Subtract times                                                                    | `SELECT SUBTIME('10:11:12','00:10:00');`                 |
| SYSDATE()                              | Return the time at which the function executes                                    | `SELECT SYSDATE();`                                      |
| TIME()                                 | Extract the time portion of the expression passed                                 | `SELECT TIME(NOW());`                                    |
| TIME_FORMAT()                          | Format as time                                                                    | `SELECT TIME_FORMAT(NOW(), '%H:%i:%s');`                 |
| TIME_TO_SEC()                          | Return the argument converted to seconds                                          | `SELECT TIME_TO_SEC('01:01:01');`                        |
| TIMEDIFF()                             | Subtract time                                                                     | `SELECT TIMEDIFF('10:11:12','10:10:10');`                |
| TIMESTAMP()                            | With a single argument, returns date/datetime; with two, the sum of the arguments | `SELECT TIMESTAMP('2024-01-01','10:00:00');`             |
| TIMESTAMPADD()                         | Add an interval to a datetime expression                                          | `SELECT TIMESTAMPADD(DAY, 1, NOW());`                    |
| TIMESTAMPDIFF()                        | Return the difference of two datetime expressions, using the units specified      | `SELECT TIMESTAMPDIFF(DAY, '2024-01-01', '2024-01-05');` |
| TO_DAYS()                              | Return the date argument converted to days                                        | `SELECT TO_DAYS('2024-01-05');`                          |
| TO_SECONDS()                           | Return the date or datetime argument converted to seconds since Year 0            | `SELECT TO_SECONDS('2024-01-05');`                       |
| UNIX_TIMESTAMP()                       | Return a Unix timestamp                                                           | `SELECT UNIX_TIMESTAMP();`                               |
| UTC_DATE()                             | Return the current UTC date                                                       | `SELECT UTC_DATE();`                                     |
| UTC_TIME()                             | Return the current UTC time                                                       | `SELECT UTC_TIME();`                                     |
| UTC_TIMESTAMP()                        | Return the current UTC date and time                                              | `SELECT UTC_TIMESTAMP();`                                |
| WEEK()                                 | Return the week number                                                            | `SELECT WEEK('2024-01-05');`                             |
| WEEKDAY()                              | Return the weekday index                                                          | `SELECT WEEKDAY('2024-01-05');`                          |
| WEEKOFYEAR()                           | Return the calendar week of the date (1-53)                                       | `SELECT WEEKOFYEAR('2024-01-05');`                       |
| YEAR()                                 | Return the year                                                                   | `SELECT YEAR('2024-01-05');`                             |
| YEARWEEK()                             | Return the year and week                                                          | `SELECT YEARWEEK('2024-01-05');`                         |

---

## 📊 Aggregate Functions

| Name            | Description                                      | Usage Example                             |
| --------------- | ------------------------------------------------ | ----------------------------------------- |
| AVG()           | Return the average value of the argument         | `SELECT AVG(col) FROM my_table;`          |
| BIT_AND()       | Return bitwise AND                               | `SELECT BIT_AND(col) FROM my_table;`      |
| BIT_OR()        | Return bitwise OR                                | `SELECT BIT_OR(col) FROM my_table;`       |
| BIT_XOR()       | Return bitwise XOR                               | `SELECT BIT_XOR(col) FROM my_table;`      |
| COUNT()         | Return a count of the number of rows returned    | `SELECT COUNT(*) FROM my_table;`          |
| COUNT(DISTINCT) | Return the count of a number of different values | `SELECT COUNT(DISTINCT col) FROM t;`      |
| GROUP_CONCAT()  | Return a concatenated string                     | `SELECT GROUP_CONCAT(col) FROM my_table;` |
| MAX()           | Return the maximum value                         | `SELECT MAX(col) FROM my_table;`          |
| MIN()           | Return the minimum value                         | `SELECT MIN(col) FROM my_table;`          |
| STD()           | Return the population standard deviation         | `SELECT STD(col) FROM my_table;`          |
| STDDEV()        | Return the population standard deviation         | `SELECT STDDEV(col) FROM my_table;`       |
| STDDEV_POP()    | Return the population standard deviation         | `SELECT STDDEV_POP(col) FROM my_table;`   |
| STDDEV_SAMP()   | Return the sample standard deviation             | `SELECT STDDEV_SAMP(col) FROM my_table;`  |
| SUM()           | Return the sum                                   | `SELECT SUM(col) FROM my_table;`          |
| VAR_POP()       | Return the population standard variance          | `SELECT VAR_POP(col) FROM my_table;`      |
| VAR_SAMP()      | Return the sample variance                       | `SELECT VAR_SAMP(col) FROM my_table;`     |
| VARIANCE()      | Return the population standard variance          | `SELECT VARIANCE(col) FROM my_table;`     |

---

## 🪟 Window Functions

| Name           | Description                                                     | Usage Example                                           |
| -------------- | --------------------------------------------------------------- | ------------------------------------------------------- |
| CUME_DIST()    | Cumulative distribution value                                   | `SELECT CUME_DIST() OVER ();`                           |
| DENSE_RANK()   | Rank of current row within its partition, without gaps          | `SELECT DENSE_RANK() OVER ();`                          |
| FIRST_VALUE()  | Value of argument from first row of window frame                | `SELECT FIRST_VALUE(col) OVER ();`                      |
| GROUPING()     | Distinguish super-aggregate ROLLUP rows from regular rows       | `SELECT GROUPING(col) FROM t GROUP BY col WITH ROLLUP;` |
| LAG()          | Value of argument from row lagging current row within partition | `SELECT LAG(col) OVER ();`                              |
| LAST_VALUE()   | Value of argument from last row of window frame                 | `SELECT LAST_VALUE(col) OVER ();`                       |
| LEAD()         | Value of argument from row leading current row within partition | `SELECT LEAD(col) OVER ();`                             |
| NTH_VALUE()    | Value of argument from N-th row of window frame                 | `SELECT NTH_VALUE(col,2) OVER ();`                      |
| NTILE()        | Bucket number of current row within its partition.              | `SELECT NTILE(4) OVER ();`                              |
| PERCENT_RANK() | Percentage rank value                                           | `SELECT PERCENT_RANK() OVER ();`                        |
| RANK()         | Rank of current row within its partition, with gaps             | `SELECT RANK() OVER ();`                                |
| ROW_NUMBER()   | Number of current row within its partition                      | `SELECT ROW_NUMBER() OVER ();`                          |

---

## 📋 JSON Functions

| Name                            | Description                                                                                   | Usage Example                                                          |
| ------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| JSON_ARRAY()                    | Create JSON array                                                                             | `SELECT JSON_ARRAY(1,2,3);`                                            |
| JSON_ARRAY_APPEND()             | Append data to JSON document                                                                  | `SELECT JSON_ARRAY_APPEND('[1]', '$', 2);`                             |
| JSON_ARRAY_INSERT()             | Insert into JSON array                                                                        | `SELECT JSON_ARRAY_INSERT('[1]', '$[1]', 2);`                          |
| JSON_ARRAYAGG()                 | Return result set as a single JSON array                                                      | `SELECT JSON_ARRAYAGG(col) FROM t;`                                    |
| JSON_CONTAINS()                 | Whether JSON document contains specific object at path                                        | `SELECT JSON_CONTAINS('{"a":1}','1','$.a');`                           |
| JSON_CONTAINS_PATH()            | Whether JSON document contains any data at path                                               | `SELECT JSON_CONTAINS_PATH('{"a":1}','one','$.a');`                    |
| JSON_DEPTH()                    | Maximum depth of JSON document                                                                | `SELECT JSON_DEPTH('{"a":1}');`                                        |
| JSON_DUALITY_OBJECT()           | Create JSON duality object                                                                    | `SELECT JSON_DUALITY_OBJECT();`                                        |
| JSON_EXTRACT()                  | Return data from JSON document                                                                | `SELECT JSON_EXTRACT('{"a":1}','$.a');`                                |
| JSON_INSERT()                   | Insert data into JSON document                                                                | `SELECT JSON_INSERT('{"a":1}','$.b',2);`                               |
| JSON_KEYS()                     | Array of keys from JSON document                                                              | `SELECT JSON_KEYS('{"a":1,"b":2}');`                                   |
| JSON_LENGTH()                   | Number of elements in JSON document                                                           | `SELECT JSON_LENGTH('[1,2,3]');`                                       |
| JSON_MERGE()                    | Merge JSON documents, preserving duplicate keys. Deprecated synonym for JSON_MERGE_PRESERVE() | `SELECT JSON_MERGE('{"a":1}','{"a":2}');`                              |
| JSON_MERGE_PATCH()              | Merge JSON documents, replacing values of duplicate keys                                      | `SELECT JSON_MERGE_PATCH('{"a":1}','{"a":2}');`                        |
| JSON_MERGE_PRESERVE()           | Merge JSON documents, preserving duplicate keys                                               | `SELECT JSON_MERGE_PRESERVE('{"a":1}','{"a":2}');`                     |
| JSON_OBJECT()                   | Create JSON object                                                                            | `SELECT JSON_OBJECT('a',1);`                                           |
| JSON_OBJECTAGG()                | Return result set as a single JSON object                                                     | `SELECT JSON_OBJECTAGG(k,v) FROM t;`                                   |
| JSON_OVERLAPS()                 | Compare JSON documents; return TRUE if they overlap                                           | `SELECT JSON_OVERLAPS('{"a":1}','{"a":2}');`                           |
| JSON_PRETTY()                   | Print a JSON document in human-readable format                                                | `SELECT JSON_PRETTY('{"a":1}');`                                       |
| JSON_QUOTE()                    | Quote JSON document                                                                           | `SELECT JSON_QUOTE('abc');`                                            |
| JSON_REMOVE()                   | Remove data from JSON document                                                                | `SELECT JSON_REMOVE('{"a":1}','$.a');`                                 |
| JSON_REPLACE()                  | Replace values in JSON document                                                               | `SELECT JSON_REPLACE('{"a":1}','$.a',2);`                              |
| JSON_SCHEMA_VALID()             | Validate JSON document against JSON schema                                                    | `SELECT JSON_SCHEMA_VALID('{"type":"object"}','{"a":1}');`             |
| JSON_SCHEMA_VALIDATION_REPORT() | Validate JSON document against JSON schema; returns report                                    | `SELECT JSON_SCHEMA_VALIDATION_REPORT('{"type":"object"}','{"a":1}');` |
| JSON_SEARCH()                   | Path to value within JSON document                                                            | `SELECT JSON_SEARCH('{"a":1}','one',1);`                               |
| JSON_SET()                      | Insert data into JSON document                                                                | `SELECT JSON_SET('{"a":1}','$.b',2);`                                  |
| JSON_STORAGE_FREE()             | Freed space within binary representation of JSON column value following partial update        | `SELECT JSON_STORAGE_FREE('{}');`                                      |
| JSON_STORAGE_SIZE()             | Space used for storage of binary representation of a JSON document                            | `SELECT JSON_STORAGE_SIZE('{}');`                                      |
| JSON_TABLE()                    | Return data from a JSON expression as a relational table                                      | `SELECT * FROM JSON_TABLE('[1,2]','$[*]' COLUMNS (x INT PATH '$'));`   |
| JSON_TYPE()                     | Type of JSON value                                                                            | `SELECT JSON_TYPE('{"a":1}');`                                         |
| JSON_UNQUOTE()                  | Unquote JSON value                                                                            | `SELECT JSON_UNQUOTE('"a"');`                                          |
| JSON_VALID()                    | Whether JSON value is valid                                                                   | `SELECT JSON_VALID('{"a":1}');`                                        |
| JSON_VALUE()                    | Extract value from JSON document at path; return as VARCHAR(512) or specified type            | `SELECT JSON_VALUE('{"a":1}','$.a');`                                  |

---

## 🌍 Spatial Functions

| Name                                                                         | Description                                                   | Usage Example                                                        |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------- |
| GeomCollection()                                                             | Construct geometry collection from geometries                 | `SELECT GeomCollection();`                                           |
| GeometryCollection()                                                         | Construct geometry collection from geometries                 | `SELECT GeometryCollection();`                                       |
| LineString()                                                                 | Construct LineString from Point values                        | `SELECT LineString();`                                               |
| MultiLineString()                                                            | Construct MultiLineString from LineString values              | `SELECT MultiLineString();`                                          |
| MultiPoint()                                                                 | Construct MultiPoint from Point values                        | `SELECT MultiPoint();`                                               |
| MultiPolygon()                                                               | Construct MultiPolygon from Polygon values                    | `SELECT MultiPolygon();`                                             |
| Point()                                                                      | Construct Point from coordinates                              | `SELECT Point(1,1);`                                                 |
| Polygon()                                                                    | Construct Polygon from LineString arguments                   | `SELECT Polygon();`                                                  |
| MBRContains()                                                                | Whether MBR of one geometry contains MBR of another           | `SELECT MBRContains(a,b);`                                           |
| MBRCoveredBy()                                                               | Whether one MBR is covered by another                         | `SELECT MBRCoveredBy(a,b);`                                          |
| MBRCovers()                                                                  | Whether one MBR covers another                                | `SELECT MBRCovers(a,b);`                                             |
| MBRDisjoint()                                                                | Whether MBRs of two geometries are disjoint                   | `SELECT MBRDisjoint(a,b);`                                           |
| MBREquals()                                                                  | Whether MBRs of two geometries are equal                      | `SELECT MBREquals(a,b);`                                             |
| MBRIntersects()                                                              | Whether MBRs of two geometries intersect                      | `SELECT MBRIntersects(a,b);`                                         |
| MBROverlaps()                                                                | Whether MBRs of two geometries overlap                        | `SELECT MBROverlaps(a,b);`                                           |
| MBRTouches()                                                                 | Whether MBRs of two geometries touch                          | `SELECT MBRTouches(a,b);`                                            |
| MBRWithin()                                                                  | Whether MBR of one geometry is within MBR of another          | `SELECT MBRWithin(a,b);`                                             |
| ST_Area()                                                                    | Return Polygon or MultiPolygon area                           | `SELECT ST_Area(g);`                                                 |
| ST_AsBinary(), ST_AsWKB()                                                    | Convert from internal geometry format to WKB                  | `SELECT ST_AsBinary(g);`                                             |
| ST_AsGeoJSON()                                                               | Generate GeoJSON object from geometry                         | `SELECT ST_AsGeoJSON(g);`                                            |
| ST_AsText(), ST_AsWKT()                                                      | Convert from internal geometry format to WKT                  | `SELECT ST_AsText(g);`                                               |
| ST_Buffer()                                                                  | Return geometry of points within given distance from geometry | `SELECT ST_Buffer(g, 10);`                                           |
| ST_Buffer_Strategy()                                                         | Produce strategy option for ST_Buffer()                       | `SELECT ST_Buffer_Strategy('quad_segs=8');`                          |
| ST_Centroid()                                                                | Return centroid as a point                                    | `SELECT ST_Centroid(g);`                                             |
| ST_Collect()                                                                 | Aggregate spatial values into collection                      | `SELECT ST_Collect(g);`                                              |
| ST_Contains()                                                                | Whether one geometry contains another                         | `SELECT ST_Contains(a,b);`                                           |
| ST_ConvexHull()                                                              | Return convex hull of geometry                                | `SELECT ST_ConvexHull(g);`                                           |
| ST_Crosses()                                                                 | Whether one geometry crosses another                          | `SELECT ST_Crosses(a,b);`                                            |
| ST_Difference()                                                              | Return point set difference of two geometries                 | `SELECT ST_Difference(a,b);`                                         |
| ST_Dimension()                                                               | Dimension of geometry                                         | `SELECT ST_Dimension(g);`                                            |
| ST_Disjoint()                                                                | Whether one geometry is disjoint from another                 | `SELECT ST_Disjoint(a,b);`                                           |
| ST_Distance()                                                                | The distance of one geometry from another                     | `SELECT ST_Distance(a,b);`                                           |
| ST_Distance_Sphere()                                                         | Minimum distance on earth between two geometries              | `SELECT ST_Distance_Sphere(a,b);`                                    |
| ST_EndPoint()                                                                | End Point of LineString                                       | `SELECT ST_EndPoint(g);`                                             |
| ST_Envelope()                                                                | Return MBR of geometry                                        | `SELECT ST_Envelope(g);`                                             |
| ST_Equals()                                                                  | Whether one geometry is equal to another                      | `SELECT ST_Equals(a,b);`                                             |
| ST_ExteriorRing()                                                            | Return exterior ring of Polygon                               | `SELECT ST_ExteriorRing(g);`                                         |
| ST_FrechetDistance()                                                         | The discrete Fréchet distance of one geometry from another    | `SELECT ST_FrechetDistance(a,b);`                                    |
| ST_GeoHash()                                                                 | Produce a geohash value                                       | `SELECT ST_GeoHash(g);`                                              |
| ST_GeomCollFromText(), ST_GeometryCollectionFromText(), ST_GeomCollFromTxt() | Return geometry collection from WKT                           | `SELECT ST_GeomCollFromText('GEOMETRYCOLLECTION()');`                |
| ST_GeomCollFromWKB(), ST_GeometryCollectionFromWKB()                         | Return geometry collection from WKB                           | `SELECT ST_GeomCollFromWKB(g);`                                      |
| ST_GeometryN()                                                               | Return N-th geometry from geometry collection                 | `SELECT ST_GeometryN(g,1);`                                          |
| ST_GeometryType()                                                            | Return name of geometry type                                  | `SELECT ST_GeometryType(g);`                                         |
| ST_GeomFromGeoJSON()                                                         | Generate geometry from GeoJSON object                         | `SELECT ST_GeomFromGeoJSON('{"type":"Point","coordinates":[0,0]}');` |
| ST_GeomFromText(), ST_GeometryFromText()                                     | Return geometry from WKT                                      | `SELECT ST_GeomFromText('POINT(0 0)');`                              |
| ST_GeomFromWKB(), ST_GeometryFromWKB()                                       | Return geometry from WKB                                      | `SELECT ST_GeomFromWKB(g);`                                          |
| ST_HausdorffDistance()                                                       | The discrete Hausdorff distance of one geometry from another  | `SELECT ST_HausdorffDistance(a,b);`                                  |
| ST_InteriorRingN()                                                           | Return N-th interior ring of Polygon                          | `SELECT ST_InteriorRingN(g,1);`                                      |
| ST_Intersection()                                                            | Return point set intersection of two geometries               | `SELECT ST_Intersection(a,b);`                                       |
| ST_Intersects()                                                              | Whether one geometry intersects another                       | `SELECT ST_Intersects(a,b);`                                         |
| ST_IsClosed()                                                                | Whether a geometry is closed and simple                       | `SELECT ST_IsClosed(g);`                                             |
| ST_IsEmpty()                                                                 | Whether a geometry is empty                                   | `SELECT ST_IsEmpty(g);`                                              |
| ST_IsSimple()                                                                | Whether a geometry is simple                                  | `SELECT ST_IsSimple(g);`                                             |
| ST_IsValid()                                                                 | Whether a geometry is valid                                   | `SELECT ST_IsValid(g);`                                              |
| ST_LatFromGeoHash()                                                          | Return latitude from geohash value                            | `SELECT ST_LatFromGeoHash('ezs42');`                                 |
| ST_Latitude()                                                                | Return latitude of Point                                      | `SELECT ST_Latitude(g);`                                             |
| ST_Length()                                                                  | Return length of LineString                                   | `SELECT ST_Length(g);`                                               |
| ST_LineFromText(), ST_LineStringFromText()                                   | Construct LineString from WKT                                 | `SELECT ST_LineFromText('LINESTRING(0 0,1 1)');`                     |
| ST_LineFromWKB(), ST_LineStringFromWKB()                                     | Construct LineString from WKB                                 | `SELECT ST_LineFromWKB(g);`                                          |
| ST_LineInterpolatePoint()                                                    | The point a given percentage along a LineString               | `SELECT ST_LineInterpolatePoint(g,0.5);`                             |
| ST_LineInterpolatePoints()                                                   | The points a given percentage along a LineString              | `SELECT ST_LineInterpolatePoints(g,0.5);`                            |
| ST_LongFromGeoHash()                                                         | Return longitude from geohash value                           | `SELECT ST_LongFromGeoHash('ezs42');`                                |
| ST_Longitude()                                                               | Return longitude of Point                                     | `SELECT ST_Longitude(g);`                                            |
| ST_MakeEnvelope()                                                            | Rectangle around two points                                   | `SELECT ST_MakeEnvelope(0,0,1,1,4326);`                              |
| ST_MLineFromText(), ST_MultiLineStringFromText()                             | Construct MultiLineString from WKT                            | `SELECT ST_MLineFromText('MULTILINESTRING()');`                      |
| ST_MLineFromWKB(), ST_MultiLineStringFromWKB()                               | Construct MultiLineString from WKB                            | `SELECT ST_MLineFromWKB(g);`                                         |
| ST_MPointFromText(), ST_MultiPointFromText()                                 | Construct MultiPoint from WKT                                 | `SELECT ST_MPointFromText('MULTIPOINT()');`                          |
| ST_MPointFromWKB(), ST_MultiPointFromWKB()                                   | Construct MultiPoint from WKB                                 | `SELECT ST_MPointFromWKB(g);`                                        |
| ST_MPolyFromText(), ST_MultiPolygonFromText()                                | Construct MultiPolygon from WKT                               | `SELECT ST_MPolyFromText('MULTIPOLYGON()');`                         |
| ST_MPolyFromWKB(), ST_MultiPolygonFromWKB()                                  | Construct MultiPolygon from WKB                               | `SELECT ST_MPolyFromWKB(g);`                                         |
| ST_NumGeometries()                                                           | Return number of geometries in geometry collection            | `SELECT ST_NumGeometries(g);`                                        |
| ST_NumInteriorRing(), ST_NumInteriorRings()                                  | Return number of interior rings in Polygon                    | `SELECT ST_NumInteriorRing(g);`                                      |
| ST_NumPoints()                                                               | Return number of points in LineString                         | `SELECT ST_NumPoints(g);`                                            |
| ST_Overlaps()                                                                | Whether one geometry overlaps another                         | `SELECT ST_Overlaps(a,b);`                                           |
| ST_PointAtDistance()                                                         | The point a given distance along a LineString                 | `SELECT ST_PointAtDistance(g,10);`                                   |
| ST_PointFromGeoHash()                                                        | Convert geohash value to POINT value                          | `SELECT ST_PointFromGeoHash('ezs42');`                               |
| ST_PointFromText()                                                           | Construct Point from WKT                                      | `SELECT ST_PointFromText('POINT(0 0)');`                             |
| ST_PointFromWKB()                                                            | Construct Point from WKB                                      | `SELECT ST_PointFromWKB(g);`                                         |
| ST_PointN()                                                                  | Return N-th point from LineString                             | `SELECT ST_PointN(g,1);`                                             |
| ST_PolyFromText(), ST_PolygonFromText()                                      | Construct Polygon from WKT                                    | `SELECT ST_PolyFromText('POLYGON()');`                               |
| ST_PolyFromWKB(), ST_PolygonFromWKB()                                        | Construct Polygon from WKB                                    | `SELECT ST_PolyFromWKB(g);`                                          |
| ST_Simplify()                                                                | Return simplified geometry                                    | `SELECT ST_Simplify(g);`                                             |
| ST_SRID()                                                                    | Return spatial reference system ID for geometry               | `SELECT ST_SRID(g);`                                                 |
| ST_StartPoint()                                                              | Start Point of LineString                                     | `SELECT ST_StartPoint(g);`                                           |
| ST_SwapXY()                                                                  | Return argument with X/Y coordinates swapped                  | `SELECT ST_SwapXY(g);`                                               |
| ST_SymDifference()                                                           | Return point set symmetric difference of two geometries       | `SELECT ST_SymDifference(a,b);`                                      |
| ST_Touches()                                                                 | Whether one geometry touches another                          | `SELECT ST_Touches(a,b);`                                            |
| ST_Transform()                                                               | Transform coordinates of geometry                             | `SELECT ST_Transform(g,4326);`                                       |
| ST_Union()                                                                   | Return point set union of two geometries                      | `SELECT ST_Union(a,b);`                                              |
| ST_Validate()                                                                | Return validated geometry                                     | `SELECT ST_Validate(g);`                                             |
| ST_Within()                                                                  | Whether one geometry is within another                        | `SELECT ST_Within(a,b);`                                             |
| ST_X()                                                                       | Return X coordinate of Point                                  | `SELECT ST_X(g);`                                                    |
| ST_Y()                                                                       | Return Y coordinate of Point                                  | `SELECT ST_Y(g);`                                                    |

---

## ⚖️ Comparison Functions

| Name         | Description                                     | Usage Example                         |
| ------------ | ----------------------------------------------- | ------------------------------------- |
| COALESCE()   | Return the first non-NULL argument              | `SELECT COALESCE(col1, col2) FROM t;` |
| EXISTS()     | Whether the result of a query contains any rows | `SELECT EXISTS(SELECT 1);`            |
| NOT EXISTS() | Whether the result of a query contains no rows  | `SELECT NOT EXISTS(SELECT 1);`        |
| GREATEST()   | Return the largest argument                     | `SELECT GREATEST(1,2,3);`             |
| ISNULL()     | Test whether the argument is NULL               | `SELECT ISNULL(NULL);`                |
| LEAST()      | Return the smallest argument                    | `SELECT LEAST(1,2,3);`                |
| NULLIF()     | Return NULL if expr1 = expr2                    | `SELECT NULLIF(1,1);`                 |

---

## 🔀 Control Flow Functions

| Name     | Description            | Usage Example                                      |
| -------- | ---------------------- | -------------------------------------------------- |
| CASE     | Case operator          | `SELECT CASE WHEN a > 0 THEN 'yes' ELSE 'no' END;` |
| IF()     | If/else construct      | `SELECT IF(a > 0, 'yes', 'no');`                   |
| IFNULL() | Null if/else construct | `SELECT IFNULL(a, 0);`                             |

---

## ℹ️ Information Functions

| Name                         | Description                                                                                            | Usage Example                              |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| BENCHMARK()                  | Repeatedly execute an expression                                                                       | `SELECT BENCHMARK(100000, MD5('a'));`      |
| BIN_TO_UUID()                | Convert binary UUID to string                                                                          | `SELECT BIN_TO_UUID(UUID_TO_BIN(UUID()));` |
| BIT_COUNT()                  | Return the number of bits that are set                                                                 | `SELECT BIT_COUNT(7);`                     |
| CONNECTION_ID()              | Return the connection ID (thread ID) for the connection                                                | `SELECT CONNECTION_ID();`                  |
| CURRENT_ROLE()               | Return the current active roles                                                                        | `SELECT CURRENT_ROLE();`                   |
| CURRENT_USER(), CURRENT_USER | The authenticated user name and host name                                                              | `SELECT CURRENT_USER();`                   |
| DATABASE()                   | Return the default (current) database name                                                             | `SELECT DATABASE();`                       |
| DEFAULT()                    | Return the default value for a table column                                                            | `SELECT DEFAULT(col);`                     |
| FOUND_ROWS()                 | For a SELECT with a LIMIT clause, the number of rows that would be returned were there no LIMIT clause | `SELECT FOUND_ROWS();`                     |
| ICU_VERSION()                | ICU library version                                                                                    | `SELECT ICU_VERSION();`                    |
| LAST_INSERT_ID()             | Value of the AUTOINCREMENT column for the last INSERT                                                  | `SELECT LAST_INSERT_ID();`                 |
| PS_CURRENT_THREAD_ID()       | Performance Schema thread ID for current thread                                                        | `SELECT PS_CURRENT_THREAD_ID();`           |
| PS_THREAD_ID()               | Performance Schema thread ID for given thread                                                          | `SELECT PS_THREAD_ID();`                   |
| ROW_COUNT()                  | The number of rows updated                                                                             | `SELECT ROW_COUNT();`                      |
| SCHEMA()                     | Synonym for DATABASE()                                                                                 | `SELECT SCHEMA();`                         |
| SESSION_USER()               | Synonym for USER()                                                                                     | `SELECT SESSION_USER();`                   |
| SYSTEM_USER()                | Synonym for USER()                                                                                     | `SELECT SYSTEM_USER();`                    |
| USER()                       | The user name and host name provided by the client                                                     | `SELECT USER();`                           |
| UUID()                       | Return a Universal Unique Identifier (UUID)                                                            | `SELECT UUID();`                           |
| UUID_SHORT()                 | Return an integer-valued universal identifier                                                          | `SELECT UUID_SHORT();`                     |
| UUID_TO_BIN()                | Convert string UUID to binary                                                                          | `SELECT UUID_TO_BIN(UUID());`              |
| VERSION()                    | Return a string that indicates the MySQL server version                                                | `SELECT VERSION();`                        |
| IS_UUID()                    | Whether argument is a valid UUID                                                                       | `SELECT IS_UUID(UUID());`                  |

---

## 🔐 Encryption and Compression

| Name                         | Description                                      | Usage Example                               |
| ---------------------------- | ------------------------------------------------ | ------------------------------------------- |
| AES_DECRYPT()                | Decrypt using AES                                | `SELECT AES_DECRYPT(col, 'key');`           |
| AES_ENCRYPT()                | Encrypt using AES                                | `SELECT AES_ENCRYPT('text', 'key');`        |
| COMPRESS()                   | Return result as a binary string                 | `SELECT COMPRESS('text');`                  |
| RANDOM_BYTES()               | Return a random byte vector                      | `SELECT RANDOM_BYTES(16);`                  |
| SHA2()                       | Calculate an SHA-2 checksum                      | `SELECT SHA2('text', 256);`                 |
| UNCOMPRESS()                 | Uncompress a string compressed                   | `SELECT UNCOMPRESS(col);`                   |
| UNCOMPRESSED_LENGTH()        | Return the length of a string before compression | `SELECT UNCOMPRESSED_LENGTH(col);`          |
| VALIDATE_PASSWORD_STRENGTH() | Determine strength of password                   | `SELECT VALIDATE_PASSWORD_STRENGTH('abc');` |

---

## 🔒 Locking Functions

| Name                | Description                                                            | Usage Example                     |
| ------------------- | ---------------------------------------------------------------------- | --------------------------------- |
| GET_LOCK()          | Get a named lock                                                       | `SELECT GET_LOCK('my_lock', 10);` |
| IS_FREE_LOCK()      | Whether the named lock is free                                         | `SELECT IS_FREE_LOCK('my_lock');` |
| IS_USED_LOCK()      | Whether the named lock is in use; return connection identifier if true | `SELECT IS_USED_LOCK('my_lock');` |
| RELEASE_ALL_LOCKS() | Release all current named locks                                        | `SELECT RELEASE_ALL_LOCKS();`     |
| RELEASE_LOCK()      | Release the named lock                                                 | `SELECT RELEASE_LOCK('my_lock');` |

---

## 🔍 Regular Expression Functions

| Name             | Description                                             | Usage Example                                 |
| ---------------- | ------------------------------------------------------- | --------------------------------------------- |
| REGEXP_INSTR()   | Starting index of substring matching regular expression | `SELECT REGEXP_INSTR('abc123','[0-9]');`      |
| REGEXP_LIKE()    | Whether string matches regular expression               | `SELECT REGEXP_LIKE('abc','^a');`             |
| REGEXP_REPLACE() | Replace substrings matching regular expression          | `SELECT REGEXP_REPLACE('abc123','[0-9]','');` |
| REGEXP_SUBSTR()  | Return substring matching regular expression            | `SELECT REGEXP_SUBSTR('abc123','[0-9]+');`    |

---

## 🔄 Replication Functions

| Name                                              | Description                                                                                   | Usage Example                                                        |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| asynchronous_connection_failover_add_managed()    | Add group member source server configuration information to a replication channel source list | `SELECT asynchronous_connection_failover_add_managed('example');`    |
| asynchronous_connection_failover_add_source()     | Add source server configuration information server to a replication channel source list       | `SELECT asynchronous_connection_failover_add_source('example');`     |
| asynchronous_connection_failover_delete_managed() | Remove a managed group from a replication channel source list                                 | `SELECT asynchronous_connection_failover_delete_managed('example');` |
| asynchronous_connection_failover_delete_source()  | Remove a source server from a replication channel source list                                 | `SELECT asynchronous_connection_failover_delete_source('example');`  |
| asynchronous_connection_failover_reset()          | Remove all settings relating to group replication asynchronous failover                       | `SELECT asynchronous_connection_failover_reset('example');`          |
| group_replication_disable_member_action()         | Disable member action for event specified                                                     | `SELECT group_replication_disable_member_action('example');`         |
| group_replication_enable_member_action()          | Enable member action for event specified                                                      | `SELECT group_replication_enable_member_action('example');`          |
| group_replication_get_communication_protocol()    | Get version of group replication communication protocol currently in use                      | `SELECT group_replication_get_communication_protocol('example');`    |
| group_replication_get_write_concurrency()         | Get maximum number of consensus instances currently set for group                             | `SELECT group_replication_get_write_concurrency('example');`         |
| group_replication_reset_member_actions()          | Reset all member actions to defaults and configuration version number to 1                    | `SELECT group_replication_reset_member_actions('example');`          |
| group_replication_set_as_primary()                | Make a specific group member the primary                                                      | `SELECT group_replication_set_as_primary('example');`                |
| group_replication_set_communication_protocol()    | Set version for group replication communication protocol to use                               | `SELECT group_replication_set_communication_protocol('example');`    |
| group_replication_set_write_concurrency()         | Set maximum number of consensus instances that can be executed in parallel                    | `SELECT group_replication_set_write_concurrency('example');`         |
| group_replication_switch_to_multi_primary_mode()  | Changes the mode of a group running in single-primary mode to multi-primary mode              | `SELECT group_replication_switch_to_multi_primary_mode('example');`  |
| group_replication_switch_to_single_primary_mode() | Changes the mode of a group running in multi-primary mode to single-primary mode              | `SELECT group_replication_switch_to_single_primary_mode('example');` |
| MASTER_POS_WAIT()                                 | Block until the replica has read and applied all updates up to the specified position         | `SELECT MASTER_POS_WAIT('example');`                                 |
| SOURCE_POS_WAIT()                                 | Block until the replica has read and applied all updates up to the specified position         | `SELECT SOURCE_POS_WAIT('example');`                                 |
| WAIT_FOR_EXECUTED_GTID_SET()                      | Wait until the given GTIDs have executed on the replica.                                      | `SELECT WAIT_FOR_EXECUTED_GTID_SET('example');`                      |

---

## 📄 XML Functions

| Name           | Description                                             | Usage Example                            |
| -------------- | ------------------------------------------------------- | ---------------------------------------- |
| ExtractValue() | Extract a value from an XML string using XPath notation | `SELECT ExtractValue('<a>1</a>','/a');`  |
| UpdateXML()    | Return replaced XML fragment                            | `SELECT UpdateXML('<a>1</a>','/a','2');` |

---

## 🛠️ Miscellaneous Functions

| Name                                 | Description                                                                          | Usage Example                                           |
| ------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| ANY_VALUE()                          | Suppress ONLY_FULL_GROUP_BY value rejection                                          | `SELECT ANY_VALUE(col) FROM t GROUP BY id;`             |
| BINARY                               | Cast a string to a binary string                                                     | `SELECT BINARY('abc');`                                 |
| CAST()                               | Cast a value as a certain type                                                       | `SELECT CAST('1' AS UNSIGNED);`                         |
| CONVERT()                            | Cast a value as a certain type                                                       | `SELECT CONVERT('1', UNSIGNED);`                        |
| CONVERT_TZ()                         | Convert from one time zone to another                                                | `SELECT CONVERT_TZ(NOW(),'UTC','SYSTEM');`              |
| ETAG()                               | Compute hash for each row, using one or more column or other values                  | `SELECT ETAG('a');`                                     |
| FORMAT_BYTES()                       | Convert byte count to value with units                                               | `SELECT FORMAT_BYTES(1024);`                            |
| FORMAT_PICO_TIME()                   | Convert time in picoseconds to value with units                                      | `SELECT FORMAT_PICO_TIME(1000);`                        |
| FROM_BASE64()                        | Decode base64 encoded string and return result                                       | `SELECT FROM_BASE64('YQ==');`                           |
| INET_ATON()                          | Return the numeric value of an IP address                                            | `SELECT INET_ATON('127.0.0.1');`                        |
| INET_NTOA()                          | Return the IP address from a numeric value                                           | `SELECT INET_NTOA(2130706433);`                         |
| MATCH()                              | Perform full-text search                                                             | `SELECT MATCH(col) AGAINST('term');`                    |
| NAME_CONST()                         | Cause the column to have the given name                                              | `SELECT NAME_CONST('a',1);`                             |
| ROLES_GRAPHML()                      | Return a GraphML document representing memory role subgraphs                         | `SELECT ROLES_GRAPHML();`                               |
| SLEEP()                              | Sleep for a number of seconds                                                        | `SELECT SLEEP(1);`                                      |
| STATEMENT_DIGEST()                   | Compute statement digest hash value                                                  | `SELECT STATEMENT_DIGEST('SELECT 1');`                  |
| STATEMENT_DIGEST_TEXT()              | Compute normalized statement digest                                                  | `SELECT STATEMENT_DIGEST_TEXT('SELECT 1');`             |
| STRING_TO_VECTOR()                   | Get the binary value of the VECTOR column represented by a conforming string         | `SELECT STRING_TO_VECTOR('[1,2,3]');`                   |
| TO_BASE64()                          | Return the argument converted to a base-64 string                                    | `SELECT TO_BASE64('a');`                                |
| VALUES()                             | Define the values to be used during an INSERT                                        | `INSERT INTO t (c) VALUES (1);`                         |
| VECTOR_DIM()                         | Get the length of a vector (number of entries)                                       | `SELECT VECTOR_DIM(vec);`                               |
| VECTOR_TO_STRING()                   | Get the string representation of a VECTOR column, given its value as a binary string | `SELECT VECTOR_TO_STRING(vec);`                         |
| CAN_ACCESS_COLUMN()                  | Internal use only                                                                    | `SELECT CAN_ACCESS_COLUMN('example');`                  |
| CAN_ACCESS_DATABASE()                | Internal use only                                                                    | `SELECT CAN_ACCESS_DATABASE('example');`                |
| CAN_ACCESS_TABLE()                   | Internal use only                                                                    | `SELECT CAN_ACCESS_TABLE('example');`                   |
| CAN_ACCESS_USER()                    | Internal use only                                                                    | `SELECT CAN_ACCESS_USER('example');`                    |
| CAN_ACCESS_VIEW()                    | Internal use only                                                                    | `SELECT CAN_ACCESS_VIEW('example');`                    |
| GET_DD_COLUMN_PRIVILEGES()           | Internal use only                                                                    | `SELECT GET_DD_COLUMN_PRIVILEGES('example');`           |
| GET_DD_CREATE_OPTIONS()              | Internal use only                                                                    | `SELECT GET_DD_CREATE_OPTIONS('example');`              |
| GET_DD_INDEX_SUB_PART_LENGTH()       | Internal use only                                                                    | `SELECT GET_DD_INDEX_SUB_PART_LENGTH('example');`       |
| INTERNAL_AUTO_INCREMENT()            | Internal use only                                                                    | `SELECT INTERNAL_AUTO_INCREMENT('example');`            |
| INTERNAL_AVG_ROW_LENGTH()            | Internal use only                                                                    | `SELECT INTERNAL_AVG_ROW_LENGTH('example');`            |
| INTERNAL_CHECK_TIME()                | Internal use only                                                                    | `SELECT INTERNAL_CHECK_TIME('example');`                |
| INTERNAL_CHECKSUM()                  | Internal use only                                                                    | `SELECT INTERNAL_CHECKSUM('example');`                  |
| INTERNAL_DATA_FREE()                 | Internal use only                                                                    | `SELECT INTERNAL_DATA_FREE('example');`                 |
| INTERNAL_DATA_LENGTH()               | Internal use only                                                                    | `SELECT INTERNAL_DATA_LENGTH('example');`               |
| INTERNAL_DD_CHAR_LENGTH()            | Internal use only                                                                    | `SELECT INTERNAL_DD_CHAR_LENGTH('example');`            |
| INTERNAL_GET_COMMENT_OR_ERROR()      | Internal use only                                                                    | `SELECT INTERNAL_GET_COMMENT_OR_ERROR('example');`      |
| INTERNAL_GET_ENABLED_ROLE_JSON()     | Internal use only                                                                    | `SELECT INTERNAL_GET_ENABLED_ROLE_JSON('example');`     |
| INTERNAL_GET_HOSTNAME()              | Internal use only                                                                    | `SELECT INTERNAL_GET_HOSTNAME('example');`              |
| INTERNAL_GET_USERNAME()              | Internal use only                                                                    | `SELECT INTERNAL_GET_USERNAME('example');`              |
| INTERNAL_GET_VIEW_WARNING_OR_ERROR() | Internal use only                                                                    | `SELECT INTERNAL_GET_VIEW_WARNING_OR_ERROR('example');` |
| INTERNAL_INDEX_COLUMN_CARDINALITY()  | Internal use only                                                                    | `SELECT INTERNAL_INDEX_COLUMN_CARDINALITY('example');`  |
| INTERNAL_INDEX_LENGTH()              | Internal use only                                                                    | `SELECT INTERNAL_INDEX_LENGTH('example');`              |
| INTERNAL_IS_ENABLED_ROLE()           | Internal use only                                                                    | `SELECT INTERNAL_IS_ENABLED_ROLE('example');`           |
| INTERNAL_IS_MANDATORY_ROLE()         | Internal use only                                                                    | `SELECT INTERNAL_IS_MANDATORY_ROLE('example');`         |
| INTERNAL_KEYS_DISABLED()             | Internal use only                                                                    | `SELECT INTERNAL_KEYS_DISABLED('example');`             |
| INTERNAL_MAX_DATA_LENGTH()           | Internal use only                                                                    | `SELECT INTERNAL_MAX_DATA_LENGTH('example');`           |
| INTERNAL_TABLE_ROWS()                | Internal use only                                                                    | `SELECT INTERNAL_TABLE_ROWS('example');`                |
| INTERNAL_UPDATE_TIME()               | Internal use only                                                                    | `SELECT INTERNAL_UPDATE_TIME('example');`               |
