from django.urls import path
from .views import *

urlpatterns = [
    path('list/', games_list, name='games_list'),
    path('studios/', studios, name='studios'),


]
