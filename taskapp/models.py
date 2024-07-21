from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=10000)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

