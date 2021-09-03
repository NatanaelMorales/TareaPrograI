from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('detalles/', detalles, name='detalles'),
    path('detalles2/', detalles2, name='detalles2'),


]