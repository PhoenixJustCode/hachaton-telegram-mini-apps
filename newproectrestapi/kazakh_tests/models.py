from django.db import models
from django.contrib.auth.models import User


class KazakhTest(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='kazakh_tests')  # Связываем с встроенной моделью User
    score = models.IntegerField(default=0)
    test_date = models.DateTimeField(auto_now_add=True)
    language_level = models.IntegerField(default=1)

    def __str__(self):
        return f'Test for {self.user.username} - Score: {self.score}'
