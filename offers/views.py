from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Offer, OfferItem
from products.models import Product
from customers.models import Customer
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from decimal import Decimal
from collections import Counter


@login_required
@require_http_methods(["GET"])
def offer_list(request):
    """
    View to list all offers.
    Supports HTML and JSON responses.
    """
    offers = Offer.objects.all()

    # JSON response
    if request.headers.get('Content-Type') == 'application/json':
        offers_data = [
            {
                "id": offer.id,
                "customer": offer.customer.name if offer.customer else "N/A",
                "creator": offer.created_by.username if offer.created_by else "N/A",
                "date": offer.date,
                "sub_total": float(offer.sub_total),
                "tax": float(offer.tax),
                "total": float(offer.total),
            }
            for offer in offers
        ]
        return JsonResponse(offers_data, safe=False)

    # HTML response
    return render(request,
                  'offers/offer_list.html',
                  {'offers': offers})


@login_required
@require_http_methods(["GET"])
def offer_detail(request, pk):
    """
    View to display details of a single offer.
    Supports HTML and JSON responses.
    """
    offer = get_object_or_404(Offer, pk=pk)
    items = OfferItem.objects.filter(offer=offer)

    # JSON response
    if request.headers.get('Content-Type') == 'application/json':
        offer_data = {
            "id": offer.id,
            "customer": offer.customer.name if offer.customer else "N/A",
            "creator": offer.created_by.username if offer.created_by else "N/A",
            "date": offer.date,
            "sub_total": float(offer.sub_total),
            "tax": float(offer.tax),
            "total": float(offer.total),
            "items": [
                {
                    "product": item.product.name,
                    "quantity": item.quantity,
                    "price": float(item.product.price),
                }
                for item in items
            ],
        }
        return JsonResponse(offer_data)

    # HTML response
    return render(request, 'offers/offer_detail.html', {'offer': offer, 'items': items})


@login_required
@require_http_methods(["GET", "POST"])
def offer_create(request):
    """
    View to create a new offer.
    """
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        date = request.POST.get('date')
        product_ids = request.POST.getlist('items')

        # Calculate sub_total, tax, and total dynamically
        product_ids = [int(pid) for pid in product_ids]
        products = Product.objects.filter(id__in=product_ids)
        product_map = {p.id: p for p in products}

        sub_total = sum(product_map[pid].price for pid in product_ids if pid in product_map)
        tax = sub_total * Decimal('0.2')  # Assuming a fixed 20% tax rate
        total = sub_total + tax

        customer = get_object_or_404(Customer, id=customer_id)
        offer = Offer.objects.create(
            created_by=request.user, 
            customer=customer, 
            date=date, 
            sub_total=sub_total, 
            tax=tax, 
            total=total
        )

        # Create OfferItems with quantities
        counts = Counter(product_ids)
        for pid, quantity in counts.items():
            if pid in product_map:
                OfferItem.objects.create(offer=offer, product=product_map[pid], quantity=quantity)

        return redirect('offer_list')

    # Render the create form template
    customers = Customer.objects.all()
    products = Product.objects.all()
    return render(request,
                  'offers/offer_create_form.html',
                  {'customers': customers,
                   'products': products})


@login_required
@require_http_methods(["GET", "POST"])
def offer_edit(request, pk):
    """
    View to edit an existing offer.
    """
    offer = get_object_or_404(Offer, pk=pk)
    offer_items = OfferItem.objects.filter(offer=offer)
    selected_product_ids = offer_items.values_list('product__id', flat=True)
    products = Product.objects.all()

    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        date = request.POST.get('date')
        selected_product_ids = request.POST.getlist('items')

        # Calculate sub_total, tax, and total dynamically
        selected_product_ids = [int(pid) for pid in selected_product_ids]
        selected_products = Product.objects.filter(id__in=selected_product_ids)
        product_map = {p.id: p for p in selected_products}

        sub_total = sum(product_map[pid].price for pid in selected_product_ids if pid in product_map)
        tax = sub_total * Decimal('0.2')  # Assuming a fixed 20% tax rate
        total = sub_total + tax

        # Update offer details
        offer.customer = get_object_or_404(Customer, id=customer_id)
        offer.date = date
        offer.sub_total = sub_total
        offer.tax = tax
        offer.total = total
        offer.save()

        # Update offer items
        OfferItem.objects.filter(offer=offer).delete()
        counts = Counter(selected_product_ids)
        for pid, quantity in counts.items():
            if pid in product_map:
                OfferItem.objects.create(offer=offer, product=product_map[pid], quantity=quantity)

        return redirect('offer_detail', pk=offer.id)

    # Render the edit form template
    customers = Customer.objects.all()
    return render(
        request,
        'offers/offer_edit_form.html',
        {
            'offer': offer,
            'customers': customers,
            'products': products,
            'selected_product_ids': list(selected_product_ids),
        },
    )
