from django.urls import path
from authentication import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
]
