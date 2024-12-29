from django.db import models
from django.conf import settings

# products/models.py
class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    title = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)
    view_count = models.PositiveIntegerField('조회수', default=0)  # 조회수 필드 추가
    
    def __str__(self):
        return self.title
