from django.urls import path
from .views import OwnerView

urlpatterns = [
    path('register/', OwnerView.as_view(), name='register'),
]