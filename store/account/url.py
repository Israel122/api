from django.urls import path

from account.views import CreateUser, AddressView, UpdateAddressView, Paymentview, UpdatePaymentview, GetAddressview, \
    AddressViewUser

urlpatterns = [
    path('user', CreateUser.as_view()),
    path('address', AddressView.as_view()),
    path('updateaddress/<int:pk>', UpdateAddressView.as_view()),
    path('payment', Paymentview.as_view()),
    path('updatepayment/<int:pk>', UpdatePaymentview.as_view()),
    path('getaddress/<int:pk>', GetAddressview.as_view()),
    path('address/<int:user>', AddressViewUser.as_view()),
]