from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Customer

class CustomerModelTest(TestCase):
    def test_customer_creation(self):
        customer = Customer.objects.create(
            name="Test Company",
            vat_id="12345678901",
            street="Test Street 1",
            city="Test City",
            country="Test Country"
        )
        self.assertEqual(customer.name, "Test Company")
        self.assertEqual(str(customer), "Test Company")
        self.assertEqual(Customer.objects.count(), 1)

class CustomerViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.customer = Customer.objects.create(
            name="Existing Company",
            vat_id="98765432109",
            street="Old Street",
            city="Old City",
            country="Old Country"
        )

    def test_customer_list_view(self):
        response = self.client.get(reverse('customer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Existing Company")

    def test_customer_create_view_get(self):
        response = self.client.get(reverse('customer_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customers/customer_create_form.html')

    def test_customer_create_view_post_success(self):
        data = {
            'name': "New Company",
            'vat_id': "11122233344",
            'street': "New Street",
            'city': "New City",
            'country': "New Country"
        }
        response = self.client.post(reverse('customer_create'), data)
        self.assertEqual(response.status_code, 302)  # Redirects to list
        self.assertEqual(Customer.objects.count(), 2)

    def test_customer_create_view_post_failure(self):
        # Missing name
        data = {
            'vat_id': "11122233344",
            'street': "New Street",
            'city': "New City",
            'country': "New Country"
        }
        response = self.client.post(reverse('customer_create'), data)
        self.assertEqual(response.status_code, 200)  # Re-renders form
        self.assertContains(response, "All fields are required.")
        self.assertEqual(Customer.objects.count(), 1)

    def test_customer_update_view_post(self):
        data = {
            'name': "Updated Company",
            'vat_id': "98765432109",
            'street': "Old Street",
            'city': "Old City",
            'country': "Old Country"
        }
        response = self.client.post(reverse('customer_update', args=[self.customer.id]), data)
        self.assertEqual(response.status_code, 302)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.name, "Updated Company")
