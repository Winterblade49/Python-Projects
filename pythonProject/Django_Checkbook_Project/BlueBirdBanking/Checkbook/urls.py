from django.shortcuts import  render, redirect, get_object_or_404
from .forms import  AccountForm, TransactionForm
from .models import  Account, Transaction


urlpatterns = [
        path('',views.home, name='index'),
path('create/', views.create_account, name='create'),
    path('<int:pk>/balance/', views.balance, name='balance'),
path('transaction/', views.transaction, name='transaction'),
               ]