from django.urls import path
from exergy_app import views


urlpatterns = [
    path('', views.index, name='index'),
]
