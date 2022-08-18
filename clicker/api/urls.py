from django.urls import path

from .views import GetLink

urlpatterns = [
    path('get_link', GetLink)
]
