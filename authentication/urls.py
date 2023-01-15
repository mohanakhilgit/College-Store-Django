from django.urls import path

from . import views


app_name = 'authentication'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.signin, name='signin'),
    path('logout/', views.sign_out, name='sign_out')
]