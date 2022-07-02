from django.urls import path
from . import views

urlpatterns = [
    path('admin',views.AdminSignUpView.as_view()),
    path('client',views.ClientSignUpView.as_view())
]