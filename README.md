# Offers Calculator - PyZ3R Edition

```text
    ____      ______ _____ ____ 
   / __ \__  /__  /|__  /|  _ \
  / /_/ / / / / / /  /_ < | |_) |
 / ____/ /_/ / / /____/ / |  _ < 
/_/    \__, / /____/____/ |_| \_\
      /____/                     

    pyz3r | 2026 | Algebra
```

## 🚀 O Projektu
**Offers Calculator** je moderna Django web aplikacija za upravljanje ponudama, proizvodima i kupcima. Inicijalno razvijen kao parcijalni ispit za Algebru, projekt je proširen naprednim funkcionalnostima i premium dizajnom.

## ✨ Ključne Značajke
- **Upravljanje Kupcima (`Customers`)**: Potpuni CRUD sustav za vođenje podataka o tvrtkama (OIB, adresa, grad).
- **Sustav Ponuda (`Offers`)**: 
  - Kreiranje ponuda s dinamičkim odabirom proizvoda.
  - Povezivanje ponuda s konkretnim kupcima.
  - Automatsko praćenje kreatora ponude (`created_by`).
- **Premium UI**: 
  - Moderni "Glassmorphism" navbar.
  - Responzivan dizajn baziran na Bootstrapu.
  - Poboljšana tipografija i vizualni identitet.
- **Data Seeding**: Uključena skripta za automatsko popunjavanje baze testnim podacima.

## 🛠️ Tehnologije
- **Backend**: Python / Django 5.1.3
- **Frontend**: HTML5, Vanilla CSS (Custom Hooks & Variables), Bootstrap 5.3
- **Baza**: SQLite3
- **Alati**: Django Extensions, FIGlet branding

## 🚦 Brzi Početak

1. **Aktivacija okruženja**:
   ```ps1
   .\venv\Scripts\activate
   ```

2. **Pokretanje servera**:
   ```bash
   python manage.py runserver
   ```

3. **Prijava (Superuser)**:
   - **Korisnik**: `admin`
   - **Lozinka**: `admin123`

## 📁 Struktura i Dokumentacija
- `customers/` - Aplikacija za upravljanje kupcima.
- `offers/` - Core logika za kalkulaciju i izradu ponuda.
- `docs/PROGRESS_REPORT.md` - Detaljan izvještaj o svim fazama implementacije.
- `static/css/style.css` - Custom premium styling.

---
**Build by PyZ3R | 2026 | Algebra Project**
