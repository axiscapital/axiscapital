
from django.urls import path
from .views import CreateDepositView
urlpatterns = [
    path('deposit/', CreateDepositView.as_view(), name='create-deposit'),
]
