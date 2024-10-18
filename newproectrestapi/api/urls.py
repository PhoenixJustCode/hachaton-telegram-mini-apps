from django.urls import path
from .views import get_users, create_user, set_language_level, set_energy

urlpatterns = [
    path('users/', get_users, name='get_user'),
    path('users/create', create_user, name='create_user'),
    path('users/<int:user_id>/set_level', set_language_level, name='set_language_level'),
    path('users/<int:user_id>/set_energy', set_energy, name='set_energy'),
]
