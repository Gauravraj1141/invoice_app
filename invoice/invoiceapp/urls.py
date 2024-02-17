
from django.urls import path
from .views import CreateInvoice, AllInvoices

urlpatterns = [
    path("create_invoice/",CreateInvoice.as_view(),name="create_invoice"),
    path("all_invoices/",AllInvoices.as_view(),name='all_invoices'),
]
