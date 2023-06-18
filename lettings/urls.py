from django.urls import path

from . import views

app_name = 'lettings'
urlpatterns = [
    path('', views.lettings_index, name='index'),
    path('<str:username>/', views.letting, name='letting'),
]