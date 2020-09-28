
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('cloud_website', views.InformationView)
urlpatterns = [
    path('', views.home, name='home-page'),
    path('information/', views.model, name='information-page'),
    path('result/', views.result, name='result-page'),
    path('api/', include(router.urls), name='api-page'),
]


