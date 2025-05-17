from django.urls import path
from .views import index, user_signup, user_login

urlpatterns = [
    path('', index, name='home'),
    path('login/', user_login, name='login'),
    path('register/', user_signup, name='register'),
]
