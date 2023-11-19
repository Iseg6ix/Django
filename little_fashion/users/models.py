from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default='foo@email.com')
    address = models.TextField()

    def __str__(self) -> str:
        return f"Hello {self.first_name} {self.last_name}, welcome to your profile"