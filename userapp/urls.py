from django.urls import path
from userapp import views

urlpatterns = [
    path('list/', views.UserList.as_view(), name='games_list'),

]
