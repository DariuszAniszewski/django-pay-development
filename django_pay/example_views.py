from django.http.response import HttpResponse
from django.shortcuts import render
from payments.models import Product, PayuPayment

__author__ = 'dariusz'


def index(request):
    data = {
        "logged": request.user.is_authenticated(),
        "products": Product.objects.all(),
    }
    return render(request, "index.html", data)


def payment_completed(request):
    payment_id = request.session["payment_id"]
    payment = PayuPayment.objects.get(pk=payment_id)
    return HttpResponse(payment.status)