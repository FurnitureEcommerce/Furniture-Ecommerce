# shipping_app/urls.py
from django.urls import path
from .views import AddressListCreateView, AddressDetailView

urlpatterns = [
    path('', AddressListCreateView.as_view(), name='shipping-list-create'),
    path('<int:pk>/', AddressDetailView.as_view(), name='shipping-detail'),
]
