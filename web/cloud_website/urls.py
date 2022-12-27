
from django.urls import path, include
from . import views
from rest_framework import routers


"""
The below paths described are the urls we use for the website and are directly linked to the
views.py file. These will allow the user to navigate to different pages on the website.
"""

router = routers.DefaultRouter()
router.register('cloud_website', views.InformationView)
urlpatterns = [
    path('', views.home, name='home-page'),
    path('diagnosis/', views.cxcontact, name='diagnosis-page'),
    path('results-positive/', views.results_positive, name='results-positive-page'),
    path('results-negative/', views.results_negative, name='results-negative-page'),
    path('how-it-works/', views.information, name='information-page'),
    path('api/', include(router.urls), name='api-page'),
]

