from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('make_coffee/', views.make_coffee, name='make_coffee'),
    path('refill/', views.refill, name='refill'),
    path('report/', views.report, name='report'),
    path('order/<str:drink_name>/', views.order, name='order'),  # corrected placement
]
