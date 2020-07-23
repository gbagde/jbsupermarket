from django.urls import path
from homepage.views import DefaultPage

urlpatterns = [
    path('', DefaultPage.as_view(), name= 'defaultpage'),
]
