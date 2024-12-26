from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name", "content")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)