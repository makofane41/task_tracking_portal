from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=10000)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name