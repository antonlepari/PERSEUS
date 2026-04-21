# 🗺️ PortSwigger Learning Roadmap

> *"Perseus didn't fight all monsters at once. He chose his battles wisely."*

Ini adalah roadmap progresif untuk menyelesaikan semua PortSwigger labs. Ikuti phase demi phase — jangan loncat ke phase berikutnya sebelum nyaman di phase sekarang.

---

## 🟢 Phase 1 — Awakening (Pemula)

**Goal:** Pahami cara kerja web dan vulnerability paling fundamental.  
**Tools yang dibutuhkan:** Browser + Burp Suite Community Edition  
**Estimasi:** 2–4 minggu

### Week 1-2: SQL Injection Foundation
- [ ] Baca [SQLi Monster](../monsters/web/sqli/intro.md)
- [ ] Lab: SQL injection — hidden data retrieval
- [ ] Lab: SQL injection — login bypass
- [ ] Baca [SQLi Cheatsheet](../codex/sqli.md)

### Week 3: XSS Basics
- [ ] Baca [XSS Monster](../monsters/web/xss/intro.md)
- [ ] Lab: Reflected XSS — HTML context, nothing encoded
- [ ] Lab: Stored XSS — HTML context, nothing encoded
- [ ] Lab: DOM XSS — document.write + location.search

### Week 4: Access Control & Auth Basics
- [ ] Lab: Unprotected admin functionality
- [ ] Lab: User role controlled by request parameter
- [ ] Lab: Username enumeration via different responses
- [ ] Lab: 2FA simple bypass

**Phase 1 Boss:** Selesaikan semua 🟢 Apprentice labs di SQLi, XSS, dan Access Control.

---

## 🔵 Phase 2 — Awakening the Hunter (Intermediate)

**Goal:** Kuasai vulnerability yang membutuhkan pemahaman HTTP lebih dalam.  
**Tools:** Burp Suite Pro (atau Community dengan sabar), Python scripts  
**Estimasi:** 1–2 bulan

### CSRF & Clickjacking
- [ ] Baca teori CSRF
- [ ] Lab: CSRF — no defenses
- [ ] Lab: Basic clickjacking dengan CSRF token
- [ ] Lab: CSRF where token not tied to user session

### SSRF & XXE
- [ ] Baca teori SSRF
- [ ] Lab: Basic SSRF — local server
- [ ] Lab: Basic SSRF — back-end system
- [ ] Lab: Exploiting XXE — external entities
- [ ] Lab: Exploiting XXE — SSRF attacks

### File Upload & Path Traversal
- [ ] Lab: File path traversal — simple case
- [ ] Lab: Remote code execution via web shell upload
- [ ] Lab: Web shell via Content-Type restriction bypass

### Authentication Deep Dive
- [ ] Lab: Blind brute-force protection — IP block
- [ ] Lab: 2FA broken logic
- [ ] Lab: Password reset poisoning via middleware

**Phase 2 Boss:** Selesaikan semua Practitioner labs di SSRF, Path Traversal, dan File Upload.

---

## 🔴 Phase 3 — Monster Slayer (Advanced)

**Goal:** Teknik-teknik advanced yang butuh pemahaman mendalam tentang HTTP internals.  
**Estimasi:** 2–3 bulan

### JWT Attacks
- [ ] Lab: JWT bypass — unverified signature
- [ ] Lab: JWT bypass — weak signing key
- [ ] Lab: JWT bypass — jwk header injection
- [ ] Lab: JWT bypass — algorithm confusion

### HTTP Request Smuggling
- [ ] Baca teori HTTP smuggling dengan sangat teliti
- [ ] Lab: Basic CL.TE vulnerability
- [ ] Lab: Basic TE.CL vulnerability
- [ ] Lanjutkan ke lab Practitioner

### Prototype Pollution
- [ ] Lab: Client-side prototype pollution — browser APIs
- [ ] Lab: DOM XSS via client-side prototype pollution
- [ ] Lab: Privilege escalation via server-side prototype pollution

### Web Cache Poisoning
- [ ] Lab: Web cache poisoning — unkeyed header
- [ ] Lab: Parameter cloaking

**Phase 3 Boss:** Selesaikan semua Practitioner labs di JWT, Request Smuggling, dan Cache Poisoning.

---

## 💀 Phase 4 — Legend (Expert)

**Goal:** Expert-level labs yang menggabungkan multiple vulnerabilities.  
**Estimasi:** Open-ended

### Topics to Conquer
- [ ] HTTP Request Smuggling — Expert labs
- [ ] OAuth — stealing tokens via proxy page
- [ ] Race Conditions — partial construction
- [ ] Web LLM Attacks — insecure output handling
- [ ] Web Cache Deception — exact-match cache rules

**Phase 4 Boss:** Selesaikan semua Expert labs. You are the hunter.

---

## 📌 Tips Umum

1. **Selalu gunakan Burp Suite** — intercept semua traffic, pahami setiap request
2. **Baca teori dulu, baru lab** — PortSwigger punya dokumentasi excellent
3. **Catat di writeup** — format ada di [`hunts/portswigger/_template.md`](../hunts/portswigger/_template.md)
4. **Jangan langsung lihat solusi** — paling tidak coba 30 menit sendiri
5. **Ulangi lab yang gagal** — memahami *kenapa* gagal lebih penting dari hint

---

## 📈 Progress Tracker

Update tabel ini setiap kali kamu selesai phase:

| Phase | Started | Completed | Notes |
|---|---|---|---|
| 🟢 Phase 1 | — | — | |
| 🔵 Phase 2 | — | — | |
| 🔴 Phase 3 | — | — | |
| 💀 Phase 4 | — | — | |

---

*"The monster you understand is the monster you can defeat."*
