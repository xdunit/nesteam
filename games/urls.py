from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api-studio', StudioViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'game-test', GameViewTest)


urlpatterns = [


    path('list-create/', GamesView.as_view()),

    path('studio-router/', include(router.urls)),

    path('create-game-api/', GameCreateAPIView.as_view(), name='create_game'),

    path('sorter/', GameListView.as_view()),

    path('', include(router.urls)),

]
