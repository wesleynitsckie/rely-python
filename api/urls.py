from django.urls import path
from . import views

urlpatterns = [
    path('transaction_list', views.transaction_list, name="tranaction"),
    path('status', views.check_status, name="status"),
    path('confirm_sanction', views.confirm_sanction, name="status"),
    path('confirm_pep', views.confirm_pep, name="status"),
]