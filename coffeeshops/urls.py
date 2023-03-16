from django.urls import path
from .views import coffeeshops_list
urlpatterns = [
    path('', coffeeshops_list, name='coffeeshops_list')
]
