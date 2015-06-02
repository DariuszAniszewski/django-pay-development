from django.conf import settings
from django.core.urlresolvers import reverse

from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponseBadRequest

from django_payu.core import DjangoPayU, Buyer, Product
from django_payu.forms import PayuPaymentForm
from django_payu.helpers import DjangoPayException


__author__ = 'dariusz'


def index(request):
    if request.method == "POST":
        form = PayuPaymentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            buyer = Buyer(cd["buyer_first_name"], cd["buyer_last_name"], cd["buyer_email"], cd["buyer_ip_address"])
            product = Product(cd["product_name"], cd["product_unit_price"], cd["product_quantity"])
            description = cd["purchase_description"]
            continue_url = cd["continue_url"]
            payment_id, follow = DjangoPayU.create_payu_payment(buyer, product, description, continue_url)
            request.session["payment_id"] = payment_id

            return redirect(follow)
    else:
        form = PayuPaymentForm(initial={
            "buyer_ip_address": request.META["REMOTE_ADDR"],
            "continue_url": "{}{}".format(
                settings.BASE_URL,
                reverse("payment_flow_done"),
            )
        })
    data = {
        "form": form,
    }
    return render(request, "index.html", data)


def payment_completed(request):
    payment_id = request.session["payment_id"]
    data = {
        "payment_id": payment_id,
    }
    return render(request, "status.html", data)


def get_status(request, payment_id):
    try:
        payment_status = DjangoPayU.get_payment_status(payment_id)
    except DjangoPayException:
        return HttpResponseBadRequest()

    data = {
        "status": payment_status
    }
    return JsonResponse(data)

    #
    # def start_payment(request):
    # json_str = request.body.decode('utf-8')
    # data = json.loads(json_str)
    #
    # user_id = data.get("user_id")
    # quantity = data.get("quantity")
    #     price = data.get("price")
    #     title = data.get("title")
    #
    #     try:
    #         User.objects.get(pk=user_id)
    #     except User.DoesNotExist:
    #         raise BadParamValueException(ErrorMessages.USER_NOT_FOUND)
    #
    #     user = User.objects.get(pk=user_id)
    #
    #
    #     response = {
    #         "order_id": new_payment.uid,
    #         "payu_id": new_payment.payu_id,
    #         "follow": new_payment.payu_url,
    #     }
    #     return JsonResponse(response)