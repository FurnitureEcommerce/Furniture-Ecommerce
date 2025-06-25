from django.urls import path
from .views import RegisterView
from django.http import JsonResponse
from .views import LoginAPIView,UserProfileView,AddressListCreateView

def home_view(request):
    return JsonResponse({"message": "Welcome to the Store API"})

urlpatterns = [
    path('', home_view), 
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('addresses/', AddressListCreateView.as_view(), name='addresses'),

]
