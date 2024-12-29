from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
# Create your models here.
class User(AbstractUser):
    username = models.CharField('닉네임', max_length=150, unique=True)
    email = models.EmailField('이메일', unique=True)
    birthday = models.DateField('생일(YYYY-MM-DD)', auto_now=True)
    

    USERNAME_FIELD = 'email'    # 로그인 시 이메일 사용
    REQUIRED_FIELDS = ["username","birthday"]        # email은 자동으로 필수

    objects = CustomUserManager()
    

    def __str__(self):
        return self.email
