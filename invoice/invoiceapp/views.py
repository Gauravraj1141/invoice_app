from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from datetime import datetime
from rest_framework import status


class CreateInvoice(APIView):
    def post(self, request):
        input_json = request.data
        today = datetime.now().date()
        print(today, '>>')

        create_invoice = Invoice.objects.create(
            date=today, customer_name=input_json['name'])
        print(create_invoice, '>>>>')
        print(create_invoice.id, '>>create invoice>>')
        quantity = input_json['quantity']
        unit_price = input_json['unit_price']
        price = quantity*unit_price

        req_data = dict(zip(['invoice', 'description', 'quantity', 'unit_price', 'price'], [
                        create_invoice.id, input_json['description'], quantity, unit_price, price]))

        invoice_details_serializer = InvoiceDetailSerializer(data=req_data)
        if invoice_details_serializer.is_valid():
            invoice_details_serializer.save()
            print(invoice_details_serializer.data, ">>>>data")
            return Response(invoice_details_serializer.data, status=status.HTTP_201_CREATED)
        return Response(invoice_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllInvoices(APIView):
    def get(self, request):
        invoices = Invoice.objects.all()
        invoice_serializer = InvoiceSerializer(invoices, many=True).data
        for details in invoice_serializer:
            invoice_id = details['id']
            invoice_deatils = InvoiceDetail.objects.filter(
                invoice=invoice_id).values()
            details["invoice_details"] = list(invoice_deatils)
        return Response(invoice_serializer,status=status.HTTP_200_OK)
