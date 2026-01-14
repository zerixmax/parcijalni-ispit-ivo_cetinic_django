# Tehnička Dokumentacija - Nadogradnja Sustava

Ovaj dokument opisuje ključne promjene i poboljšanja implementirana u Django aplikacijama `customers` i `products`.

## Opći ciljevi refaktoriranja
1. **Standardizacija koda:** Prijelaz s funkcionalnih view-ova na ugrađene Django klasne view-ove (CBV).
2. **Sigurnost podataka:** Implementacija stroge validacije ulaznih podataka putem Django formi.
3. **Poboljšanje UX-a:** Automatski prikaz grešaka korisniku i korištenje Bootstrap komponenti.
4. **API kompatibilnost:** Dodana podrška za JSON odgovore u postojećim view-ovima.

---

## 1. Aplikacija `customers`

### Forme (`customers/forms.py`)
- Kreirana `CustomerForm` klasa.
- **Validacija OIB-a:** Implementirana provjera duljine (točno 11 znamenki) i formata (samo brojevi).
- Widgeti su obogaćeni `form-control` klasama za Bootstrap 5.

### View-ovi (`customers/views.py`)
- **Implementirani CBV:**
  - `CustomerListView`: Popis svih kupaca (zahtijeva prijavu).
  - `CustomerCreateView`: Forma za unos novog kupca.
  - `CustomerUpdateView`: Forma za promjenu podataka postojećeg kupca.

### URL-ovi (`customers/urls.py`)
- Putanje prilagođene za rad s `.as_view()` metodom.

---

## 2. Aplikacija `products`

### Forme (`products/forms.py`)
- Kreirana `ProductForm` klasa za upravljanje katalogom proizvoda.

### View-ovi (`products/views.py`)
- **Implementirani CBV:**
  - `ProductListView`: Popis proizvoda s podrškom za `application/json` zaglavlje.
  - `ProductDetailView`: Detalji pojedinog proizvoda (također podržava JSON).
  - `ProductCreateView` i `ProductUpdateView`.

---

## 3. Predlošci (Templates)
- Svi HTML predlošci za unos podataka (`*_form.html`) ažurirani su da koriste:
  ```html
  {% for field in form %}
      {{ field.label }}
      {{ field }}
      {{ field.errors }}
  {% endfor %}
  ```
- Ovime je postignuta konzistentnost u prikazu grešaka i vizualnom identitetu aplikacije.

---

## 4. Provjera i Deployment
- **Virtualno okruženje:** Korišten `venv` za izolaciju ovisnosti.
- **Git:** Promjene su commit-ane i poslane na repozitorij pod porukama:
  - `Implement CustomerForm with OIB validation...`
  - `Refactor products app to use CBVs...`
- **Provjera koda:** Izvršen `py_compile` za sve ključne datoteke.

---
*Dokument izradio: Antigravity AI*
