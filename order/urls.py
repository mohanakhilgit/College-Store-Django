from django.urls import path

from . import views


app_name = 'order'

urlpatterns = [
    path('home/<username>/', views.order_home, name='order_home'),
    path('form/', views.order_form, name='order_form'),

    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),  # AJAX
]
