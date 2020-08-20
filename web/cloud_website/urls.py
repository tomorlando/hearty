
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('model/', views.model, name='model-page'),
    path('output/', views.output, name='output-page'),
]


