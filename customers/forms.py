from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'vat_id', 'street', 'city', 'country']
        # Dodajemo CSS klase da bi izgledalo lijepo s Bootstrapom
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unesite naziv tvrtke'}),
            'vat_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unesite OIB (11 znamenki)'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'vat_id': 'VAT ID (OIB)',
            'name': 'Company Name'
        }

    def clean_vat_id(self):
        """
        Validacija za OIB - mora biti 11 znamenki i samo brojevi.
        """
        vat_id = self.cleaned_data.get('vat_id')
        
        if not vat_id.isdigit():
            raise forms.ValidationError("OIB mora sadržavati samo brojeve.")
            
        if len(vat_id) != 11:
            raise forms.ValidationError("OIB mora imati točno 11 znamenki.")
            
        return vat_id
