from django.conf.urls import handler404, handler500
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>', views.single),
]

hander404 = 'views.handler404'
