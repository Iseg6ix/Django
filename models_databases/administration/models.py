from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"User: {self.name}"