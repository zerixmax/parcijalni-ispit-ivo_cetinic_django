# products/views.py
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import JsonResponse
from .models import Product
from .forms import ProductForm

# 1. LIST VIEW
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def render_to_response(self, context, **response_kwargs):
        """ Omogućuje JSON response ako se zatraži (za API) """
        if self.request.headers.get('Content-Type') == 'application/json':
            data = list(self.object_list.values('id', 'name', 'description', 'price'))
            return JsonResponse(data, safe=False)
        return super().render_to_response(context, **response_kwargs)

# 2. DETAIL VIEW
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('Content-Type') == 'application/json':
            p = self.object
            return JsonResponse({'id': p.id, 'name': p.name, 'description': p.description, 'price': float(p.price)})
        return super().render_to_response(context, **response_kwargs)

# 3. CREATE VIEW
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create_form.html'
    success_url = reverse_lazy('product_list')

# 4. UPDATE VIEW
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_edit_form.html'
    success_url = reverse_lazy('product_list')
