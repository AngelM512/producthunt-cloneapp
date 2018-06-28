from django.urls import path
from . import views

urlpatterns = [
    path('sign/', views.sign, name="sign"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
