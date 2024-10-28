
from django.urls import path

from . import views

urlpatterns = [
    path('', views.atm_menu, name="atm_menu"),
    path('withdrawal', views.withdrawal, name = "withdrawal"),
    path('get_balance', views.get_balance, name="get_balance"),
    path('deposit', views.deposit, name="deposit"),
    path('exit_atm', views.exit_atm, name="exit_atm"),
]