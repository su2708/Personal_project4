from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다')
        email = self.normalize_email(email)  # 공백 제거, 소문자로 변환 
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
    profile_image = models.ImageField('프로필 이미지', upload_to='profile_images/', blank=True, null=True)
    birthday = models.DateField('생일(YYYY-MM-DD)', auto_now=False, blank=True, null=True)
    

    USERNAME_FIELD = 'username'    # 로그인 시 닉네임 사용
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()
    

    def __str__(self):
        return self.email
