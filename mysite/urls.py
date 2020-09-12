"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from banksys import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/add', views.addClient),
    path('client/delete', views.deleteClient),
    path('client/modify', views.modifyClient),
    path('client/search', views.searchClient),
    path('account/create', views.createAcc),
    path('account/delete', views.deleteAcc),
    path('account/modify', views.modifyAcc),
    path('account/search', views.searchAcc),
    path('loan/add', views.addLoan),
    path('loan/delete', views.deleteLoan),
    path('loan/pay', views.payLoan),
    path('loan/search', views.searchLoan),
    path('statistics/search', views.search)
]
