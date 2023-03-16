from django.urls import path
from .views import coffeeshops_list, games_list
urlpatterns = [
    path('', coffeeshops_list, name='coffeeshops_list'),
    path('<int:pk>/games', games_list, name='games_list'),
]
