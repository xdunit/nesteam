from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api-users', UserViewSet)

urlpatterns = [
    path('list/', UserList.as_view(), name='games_list'),
    path('user-router/', include(router.urls)),

    path('players/', PlayerListAPIView.as_view(), name='players'),

    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('authorization/', AuthorizationAPIView.as_view(), name='authorization'),
    path('auth-drf/', AuthDRFAPIView.as_view(), name='auth-drf'),

]
