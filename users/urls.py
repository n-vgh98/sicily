from django.urls import path
from .views import owner_dashboard
urlpatterns = [
    path('owner/', owner_dashboard, name='owner_dashboard')
]