from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )  # symmetrical=True이면 누군가를 팔로우 하자마자 맞팔이 됨. default는 True 