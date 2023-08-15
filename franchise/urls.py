from django.urls import path, include
from rest_framework import routers
from .views import FranchiseView

router = routers.DefaultRouter()
router.register(r'collection', FranchiseView)

urlpatterns = [
    path('', include(router.urls))

]
