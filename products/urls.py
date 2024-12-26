from django.urls import path
from . import views

app_name = "products"  # namespace 추가

urlpatterns = [
    path("", views.products, name="products"),  # 물건 목록 
    path("create", views.create, name="create"),  # 물건 목록에 등록 
    path("<int:pk>/", views.product_detail, name="product_detail"),  # product 상세
    path("<int:pk>/update/", views.update, name="update"),  # product 수정
    path("<int:pk>/delete/", views.delete, name="delete"),  # product 삭제
    path("<int:pk>/like/", views.like, name="like"),  # 좋아요 
    #
    path("index/", views.index, name="index"),
]