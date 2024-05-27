from django.urls import path

from checkout.views import (
    DeliveryInfo,
    checkout_view,
    initialize_payment_view,
    verify_payment_view,
)

urlpatterns = [
    path("", checkout_view, name="checkout"),
    path("delivery-info", DeliveryInfo.as_view(), name="delivery_info"),
    path("initialize/payment/", initialize_payment_view, name="payment_init"),
    path("verify/", verify_payment_view, name="verify_payment"),
]
