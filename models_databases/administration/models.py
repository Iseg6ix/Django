from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    graduated = models.BooleanField(default=False)

    def __str__(self):
        return f"User: {self.name}"