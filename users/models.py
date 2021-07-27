from django.db import models
from django.contrib.auth.models import AbstractUser

user_type2 = (
    ("partner", "partner"),
    ("employee", "employee"),
    ("customer", "customer"),
)

class CustomUser(AbstractUser):
    is_director = models.BooleanField(default=False)
    is_producer = models.BooleanField(default=True)
    user_type = models.CharField(
        max_length = 20,
        choices = user_type2,
        default='partner'
        )

# Create your models here.
