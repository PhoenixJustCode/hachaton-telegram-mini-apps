from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    language_level = models.IntegerField(default=1)
    current_level = models.IntegerField(default=1)
    energy = models.IntegerField(default=3)

    def __str__(self):
        return self.name


class KazakhTest(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='kazakh_tests') 
    score = models.IntegerField(default=0)
    test_date = models.DateTimeField(auto_now_add=True)
    language_level = models.IntegerField(default=1)

    def __str__(self):
        return f'Test for {self.user.name} - Score: {self.score}'
