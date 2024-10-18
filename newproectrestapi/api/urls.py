from django.urls import path
from .views import (
    get_users, create_user, set_language_level, set_energy,
    create_kazakh_test, get_kazakh_tests
)

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:user_id>/language-level/', set_language_level, name='set_language_level'),
    path('users/<int:user_id>/energy/', set_energy, name='set_energy'),
    path('tests/create/', create_kazakh_test, name='create_kazakh_test'),
    path('tests/<int:user_id>/', get_kazakh_tests, name='get_kazakh_tests'),
]
