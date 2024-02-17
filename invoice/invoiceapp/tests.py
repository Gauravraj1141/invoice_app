from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice

class InvoiceTestCase(TestCase):
    def setUp(self):
        Invoice.objects.create(date='2024-02-17', customer_name='Test Customer')
        self.client = APIClient()

    def test_fetch_all_invoices(self):
        url = reverse('all_invoices')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming one invoice is created in setUp()

    def test_create_invoice(self):
        url = reverse('create_invoice')
        data = {
            'name': 'Test Customer',
            'description': 'Test Description',
            'quantity': 2,
            'unit_price': 10
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
