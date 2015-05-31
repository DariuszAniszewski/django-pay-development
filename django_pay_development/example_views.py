from django.shortcuts import render

__author__ = 'dariusz'


def index(request):
    data = {
        "logged": request.user.is_authenticated(),
    }
    return render(request, "index.html", data)


def payment_completed(request):
    payment_id = request.session["payment_id"]
    data = {
        "payment_id": payment_id,
    }
    return render(request, "status.html", data)