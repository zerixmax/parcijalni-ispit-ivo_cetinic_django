from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer
from .forms import CustomerForm  # Tvoja forma s OIB validacijom

# Zamjena za def customer_list
class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'

    # Opcionalno: ako želiš koristiti svoju metodu get_all(), možeš overrideati get_queryset
    # def get_queryset(self):
    #     return Customer.get_all()

# Zamjena za def customer_create
class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_create_form.html'
    success_url = reverse_lazy('customer_list') # Kamo preusmjeriti nakon uspjeha

    # Ovdje ne trebaš pisati logiku za POST/GET niti form.save(), Django to radi sam!

# Zamjena za def customer_update
class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_edit_form.html'
    success_url = reverse_lazy('customer_list')
