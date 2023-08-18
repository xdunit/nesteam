from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'collection', FranchiseView)

urlpatterns = [
    path('', include(router.urls)),
    path('game-collection/', GameCollectionAPIView.as_view())

]
