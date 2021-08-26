from django.urls import path

from . import views

urlpatterns = [
    path('' , views.home, name='home'),
    path('listing' , views.index, name='listings'),



]
