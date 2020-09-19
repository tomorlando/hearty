
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('cloud_website', views.InformationView)
urlpatterns = [
    path('', views.home, name='home-page'),
    path('model/', views.model, name='model-page'),
    path('output/', views.output, name='output-page'),
    path('api/', include(router.urls), name='api-page'),
]


