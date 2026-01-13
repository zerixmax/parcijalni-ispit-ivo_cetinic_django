# Izvještaj o Implementaciji - Parcijalni Ispit

Ovaj dokument sadrži pregled svih promjena i implementacija izvršenih u sklopu parcijalnog ispita.

## 1. Priprema Okruženja
- Kreirano je virtualno okruženje (`venv`).
- Instalirane su sve potrebne zavisnosti iz `requirements.txt`.
- Kreiran je direktorij `docs` za dokumentaciju.
- Kreiran je **superuser** račun:
  - **Korisničko ime:** `admin`
  - **Lozinka:** `admin123`

## 2. Aplikacija `customers`
Nova aplikacija kreirana je za upravljanje podacima o tvrtkama/kupcima.
- **Model `Customer`**: Sadrži polja `name`, `vat_id` (OIB), `street`, `city` i `country`.
- **Funkcionalnosti (CRUD)**:
    - Pregled svih kupaca u tabličnom prikazu.
    - Dodavanje novih kupaca putem forme.
    - Uređivanje postojećih podataka o kupcima.
- **URL-ovi**: Registrirani pod putanjom `/customers/`.

## 3. Ažuriranje Aplikacije `offers`
Postojeći sustav ponuda prilagođen je novim zahtjevima:
- **Model `Offer`**:
    - Polje `customer` sada pokazuje na model `Customer` (tvrtku).
    - Dodano polje `created_by` koje pokazuje na korisnika (`User`) koji je kreirao ponudu.
- **Pogledi (Views)**:
    - Prilikom kreiranja ponude, korisnik sada bira tvrtku s popisa kupaca.
    - Pogledi za popis i detalje ponude uključuju informaciju o kupcu i kreatoru.
- **Predlošci (Templates)**:
    - Osvježen dizajn tablica i detaljnih prikaza.

## 4. Baza Podataka
- Izvršene su sve migracije za nove modele i promjene u shemi.
- Baza je popunjena testnim podacima pomoću skripte `seed_database.py`:
    - 50 proizvoda.
    - 5 kupaca.
    - 15 ponuda.

## 5. Navigacija
- U glavnu navigaciju (`base.html`) dodana je poveznica **Customers** za lakši pristup upravljanju kupcima.

## 6. Estetska Poboljšanja i ASCII Art
- **Premium Dizajn**: Implementiran je moderan CSS s "glassmorphism" efektima na navigaciji, boljom tipografijom (Inter/Roboto) i suptilnim hover animacijama na tablicama.
- **ASCII Art i Brending**: U datoteku `manage.py` dodan je specifičan "PyZ3R" ASCII art u *slant* fontu, zajedno s potpisom "pyz3r | 2026 | Algebra", koji se prikazuje prilikom svakog pokretanja skripte.

---
**Datum:** 13.01.2026.
**Status:** Potpuno završeno.
