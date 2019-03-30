from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<firstName>/', views.hello, name='hello'),
    path('<firstName>/answer/', views.answer, name='answer'),
]