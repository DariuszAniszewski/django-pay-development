from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from payments.models import Product

__author__ = 'dariusz'


def index(request):
    data = {
        "logged": request.user.is_authenticated(),
        "products": Product.objects.all(),
    }
    return render(request, "index.html", data)