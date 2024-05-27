import datetime
import json
import os

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, reverse
from django.views.generic import UpdateView

from account.models import Customer
from product.models import Order

PAYSTACK_API_KEY = os.environ.get("PAYSTACK_API_KEY")


class DeliveryInfo(UpdateView):
    template_name = "forms.html"

    def get_object(self):
        user = self.request.user
        deviceId = self.request.COOKIES["deviceId"]
        try:
            customer = Customer.objects.get(user=user)
        except:
            customer, created = Customer.objects.get_or_create(device_id=deviceId)
        return customer

    fields = [
        "first_name",
        "last_name",
        "email",
        "address_line_1",
        "address_line_2",
        "city",
        "state",
        "country",
        "postal_code",
        "phone_number",
    ]

    def get_success_url(self):
        return reverse("checkout")


def checkout_view(request):
    template = "checkout.html"
    try:
        customer = Customer.objects.get(user=request.user)
    except:
        deviceId = request.COOKIES["deviceId"]
        customer, created = Customer.objects.get_or_create(device_id=deviceId)
    order, created = Order.objects.get_or_create(customer=customer, completed=False)
    string = str(datetime.datetime.now().timestamp())
    order.transaction_id = string
    order.save()

    cartitems = order.cartitem_set.all()
    return render(request, template, {"order": order, "cartitems": cartitems})


def initialize_payment_view(request):
    data = json.loads(request.body)
    res = requests.post(
        "https://api.paystack.co/transaction/initialize",
        json=data,
        headers={"Authorization": f"Bearer {PAYSTACK_API_KEY}"},
    )
    response = res.json()
    return JsonResponse(response)


def verify_payment_view(request, *args, **kwargs):
    reference = request.GET["trxref"]
    order = Order.objects.get(transaction_id=reference)
    url = "https://api.paystack.co/transaction/verify/"
    verify_url = url + reference
    res = requests.get(
        verify_url, headers={"Authorization": f"Bearer {PAYSTACK_API_KEY}"}
    )

    if res.ok == True:
        content = json.loads(res.content)
        message = content["message"]
        if message == "Verification successful":
            order.completed = True
            order.save()
    else:
        message = "Operation failed"
    return HttpResponse(message)
