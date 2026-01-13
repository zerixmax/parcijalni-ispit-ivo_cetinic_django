from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Offer, OfferItem
from customers.models import Customer
from products.models import Product
from decimal import Decimal

class OfferModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.customer = Customer.objects.create(name="Test Customer", vat_id="123", street="St", city="Ct", country="Co")
        self.product = Product.objects.create(name="Test Product", price=100.00, description="Desc")

    def test_offer_creation(self):
        offer = Offer.objects.create(
            created_by=self.user,
            customer=self.customer,
            date="2023-01-01",
            sub_total=100.00,
            tax=20.00,
            total=120.00
        )
        self.assertEqual(offer.total, 120.00)
        self.assertEqual(str(offer), f"Offer #{offer.id} - Customer: Test Customer, Creator: testuser, Total: $120.0")

    def test_offer_str_with_none(self):
        offer = Offer.objects.create(
            date="2023-01-01",
            sub_total=100.00,
            tax=20.00,
            total=120.00
        )
        # Should not crash
        self.assertIn("N/A", str(offer))

class OfferViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        self.customer = Customer.objects.create(name="Test Customer", vat_id="123", street="St", city="Ct", country="Co")
        self.product1 = Product.objects.create(name="Product 1", price=100.00, description="Desc 1")
        self.product2 = Product.objects.create(name="Product 2", price=50.00, description="Desc 2")

        self.offer = Offer.objects.create(
            created_by=self.user,
            customer=self.customer,
            date="2023-01-01",
            sub_total=100.00,
            tax=20.00,
            total=120.00
        )
        OfferItem.objects.create(offer=self.offer, product=self.product1, quantity=1)

    def test_offer_list_view(self):
        response = self.client.get(reverse('offer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Customer")

        # Test JSON response
        response_json = self.client.get(reverse('offer_list'), HTTP_CONTENT_TYPE='application/json')
        self.assertEqual(response_json.status_code, 200)
        # We can't easily parse JsonResponse content in tests without calling .json(), but we can check content
        import json
        data = json.loads(response_json.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['customer'], "Test Customer")

    def test_offer_detail_view(self):
        response = self.client.get(reverse('offer_detail', args=[self.offer.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Product 1")

    def test_offer_create_view_post(self):
        data = {
            'customer': self.customer.id,
            'date': '2023-02-01',
            'items': [self.product1.id, self.product2.id]
        }
        response = self.client.post(reverse('offer_create'), data)
        self.assertEqual(response.status_code, 302)

        # Check if offer created
        new_offer = Offer.objects.latest('id')
        self.assertEqual(new_offer.sub_total, Decimal('150.00'))
        # Tax is 20% of 150 = 30
        self.assertEqual(new_offer.tax, Decimal('30.00'))
        self.assertEqual(new_offer.total, Decimal('180.00'))
        self.assertEqual(new_offer.items.count(), 2)

    def test_offer_edit_view_post(self):
        # Update offer to have only product 2
        data = {
            'customer': self.customer.id,
            'date': '2023-03-01',
            'items': [self.product2.id]
        }
        response = self.client.post(reverse('offer_edit', args=[self.offer.id]), data)
        self.assertEqual(response.status_code, 302)

        self.offer.refresh_from_db()
        self.assertEqual(self.offer.sub_total, Decimal('50.00'))
        self.assertEqual(self.offer.items.count(), 1)
        self.assertEqual(self.offer.items.first(), self.product2)
