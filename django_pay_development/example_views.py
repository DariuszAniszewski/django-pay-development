from django.shortcuts import render
from djangopay.models import Product

__author__ = 'dariusz'


def index(request):
    data = {
        "logged": request.user.is_authenticated(),
        "products": Product.objects.all(),
    }
    return render(request, "index.html", data)

def index_stripe(request):
    data = {
        "logged": request.user.is_authenticated(),
        "products": Product.objects.all(),
    }
    return render(request, "stripe.html", data)

def payment_completed(request):
    payment_id = request.session["payment_id"]
    data = {
        "payment_id": payment_id,
    }
    return render(request, "status.html", data)