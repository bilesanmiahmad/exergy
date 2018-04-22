from django.urls import path
from exergy_app import views


urlpatterns = [
    path('?<float:lat>&<float:lon>/results', views.index, name='index'),
]
