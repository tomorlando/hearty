
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('cloud_website', views.InformationView)
urlpatterns = [
    path('', views.home, name='home-page'),
    path('diagnosis/', views.cxcontact, name='diagnosis-page'),
    path('results/', views.results, name='results-page'),
    path('how-it-works/', views.information, name='information-page'),
    path('api/', include(router.urls), name='api-page'),
]


