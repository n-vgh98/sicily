from django.urls import path
from .views import owner_dashboard, \
    owner_profile, \
    user_login, \
    user_logout, \
    SignUp, \
    edit_owner_profile, \
    owner_game, \
    edit_owner_game

urlpatterns = [
    path('owner/dashboard/', owner_dashboard, name='owner_dashboard'),
    path('owner/profile', owner_profile, name='owner_profile'),
    path('owner/profile/<int:pk>', edit_owner_profile, name='edit_owner_profile'),
    path('login/', user_login, name='user_login'),
    path('logout', user_logout, name='user_logout'),
    path('sign_up', SignUp.as_view(), name="sign_up"),
    path('owner/games/', owner_game, name='owner_game'),
    path('owner/game/<int:pk>', edit_owner_game, name='edit_owner_game')
]
