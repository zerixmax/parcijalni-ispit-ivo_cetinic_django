from django.test import TestCase, Client
from django.contrib.auth.models import User
from customers.models import Customer
from products.models import Product
from offers.models import Offer, OfferItem
from decimal import Decimal

class OfferCreationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='testadmin', password='password')
        self.client.force_login(self.user)

        self.customer = Customer.objects.create(
            name="Test Customer",
            vat_id="123456789",
            street="Test Street",
            city="Test City",
            country="Test Country"
        )

        self.product = Product.objects.create(
            name="Test Product",
            description="Description",
            price=Decimal('100.00')
        )

    def test_offer_create_with_duplicates(self):
        """
        Test creating an offer with duplicate products (should increase quantity).
        """
        # Select the same product twice
        post_data = {
            'customer': self.customer.id,
            'date': '2023-10-27',
            'items': [self.product.id, self.product.id]
        }

        response = self.client.post('/offers/create/', post_data, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check if offer was created
        self.assertEqual(Offer.objects.count(), 1)
        offer = Offer.objects.first()

        # Expected calculation:
        # Subtotal: 100 + 100 = 200
        # Tax: 200 * 0.2 = 40
        # Total: 240

        # Current implementation (buggy) likely does:
        # Subtotal: 100 (deduplicated)
        # Tax: 20
        # Total: 120

        self.assertEqual(offer.sub_total, Decimal('200.00'), "Subtotal should account for duplicate items")
        self.assertEqual(offer.total, Decimal('240.00'), "Total should account for duplicate items")

        # Check items
        items = OfferItem.objects.filter(offer=offer)
        self.assertEqual(items.count(), 1, "Should have 1 OfferItem for the product")
        self.assertEqual(items.first().quantity, 2, "Quantity should be 2")

    def test_offer_edit_with_duplicates(self):
        """
        Test editing an offer to have duplicate products.
        """
        # Create an initial offer
        offer = Offer.objects.create(
            created_by=self.user,
            customer=self.customer,
            date='2023-10-27',
            sub_total=self.product.price,
            tax=self.product.price * Decimal('0.2'),
            total=self.product.price * Decimal('1.2')
        )
        OfferItem.objects.create(offer=offer, product=self.product, quantity=1)

        # Edit to have 2 items
        post_data = {
            'customer': self.customer.id,
            'date': '2023-10-28',
            'items': [self.product.id, self.product.id]
        }

        response = self.client.post(f'/offers/{offer.id}/edit/', post_data, follow=True)
        self.assertEqual(response.status_code, 200)

        offer.refresh_from_db()

        self.assertEqual(offer.sub_total, Decimal('200.00'), "Subtotal should account for duplicate items after edit")
        self.assertEqual(offer.total, Decimal('240.00'), "Total should account for duplicate items after edit")

        items = OfferItem.objects.filter(offer=offer)
        self.assertEqual(items.count(), 1, "Should have 1 OfferItem")
        self.assertEqual(items.first().quantity, 2, "Quantity should be 2")

