from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    language_level = models.IntegerField(default=1)
    current_level = models.IntegerField(default=1)
    energy = models.IntegerField(default=3)

    def __str__(self):
        return self.name
