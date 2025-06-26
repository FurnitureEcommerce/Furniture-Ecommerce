from django.urls import path
from .views import CreateDummyPaymentAPIView, VerifyDummyPaymentAPIView

urlpatterns = [
    path('create/', CreateDummyPaymentAPIView.as_view(), name='create-payment'),
    path('verify/', VerifyDummyPaymentAPIView.as_view(), name='verify-payment'),
]
