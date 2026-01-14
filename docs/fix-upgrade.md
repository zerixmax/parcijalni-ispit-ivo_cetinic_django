# Rekapitulacija rada - 14. siječnja 2026.

Danas smo uspješno implementirali napredne funkcionalnosti u aplikaciji `customers` unutar Django projekta. Glavni fokus bio je na poboljšanju validacije podataka i refaktoriranju koda prema najboljim praksama.

## 1. Implementacija Formi i Validacija
- Kreirana je datoteka `customers/forms.py`.
- Definirana je klasa `CustomerForm` temeljena na modelu `Customer`.
- **OIB Validacija:** Dodana je prilagođena logika u metodu `clean_vat_id` koja osigurava da:
    - OIB ima točno 11 znamenki.
    - Sadrži isključivo brojeve.
- Dodane su Bootstrap CSS klase (`form-control`) direktno u definiciju widgeta radi boljeg vizualnog izgleda.

## 2. Refaktoriranje View-ova (Class-Based Views)
- Funkcionalni view-ovi u `customers/views.py` zamijenjeni su Django generičkim klasama:
    - `CustomerListView` (za prikaz popisa).
    - `CustomerCreateView` (za dodavanje novih kupaca).
    - `CustomerUpdateView` (za uređivanje postojećih).
- Korišten je `LoginRequiredMixin` kako bi se osigurala autorizacija pristupa.
- Korišten je `reverse_lazy` za sigurno preusmjeravanje nakon uspješnih akcija.

## 3. Ažuriranje URL Konfiguracije
- Datoteka `customers/urls.py` ažurirana je kako bi podržala Class-Based View-ove koristeći metodu `.as_view()`.

## 4. Poboljšanje HTML Predložaka
- Ažurirani su `customer_create_form.html` i `customer_edit_form.html`.
- Predlošci sada dinamički iscrtavaju polja forme.
- Dodan je prikaz poruka o greškama direktno uz polja (npr. ako OIB nije ispravan), što značajno poboljšava korisničko iskustvo (UX).

## 5. Tehnička Provjera
- Aktivirano je virtualno okruženje (`venv`).
- Izvršena je provjera sintakse koda pomoću `py_compile`, čime je potvrđeno da nema grešaka u implementiranim Python datotekama.

---
*Ovim promjenama sustav je postao stabilniji, kod je čišći (DRY princip), a unos podataka je siguran zahvaljujući strogoj validaciji.*
