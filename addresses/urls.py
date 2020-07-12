from django.urls import path
from . import views

urlpatterns = [
    path('', views.address_list),
    path('<int:pk>/', views.address),
    path('login/', views.login)
]