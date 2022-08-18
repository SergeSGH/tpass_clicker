from django.urls import path

from .views import RedirectLink

urlpatterns = (path('<str:short_link>/', RedirectLink),)
