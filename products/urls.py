from django.urls import path
from . import views

app_name = "products"  # namespace 추가

urlpatterns = [
    path('', views.ProductListCreate.as_view(), name='product_list_create'),
    path('<int:productId>/', views.ProductDetail.as_view(), name='product_detail'),
]