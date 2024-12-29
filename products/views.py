# articles/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer
from django.core.cache import cache


class ProductListCreate(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        """상품 목록 조회"""
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)  # 목록용 Serializer 사용
        return Response(serializer.data)

    def post(self, request):
        """상품 등록"""
        serializer = ProductDetailSerializer(data=request.data)  # 상세 Serializer 사용
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_object(self, productId):
        return get_object_or_404(Product, pk=productId)

    def get(self, request, productId):
        """상품 상세 조회"""
        product = self.get_object(productId)
        
        # 로그인한 사용자이고 작성자가 아닌 경우에만 조회수 증가 처리
        # 24시간 동안 같은 IP에서 같은 게시글 조회 시 조회수가 증가하지 않음
        if request.user != product.author:
            # 해당 사용자의 IP와 게시글 ID로 캐시 키를 생성
            cache_key = f"view_count_{request.META.get('REMOTE_ADDR')}_{productId}"
            
            # 캐시에 없는 경우에만 조회수 증가
            if not cache.get(cache_key):
                product.view_count += 1
                product.save()
                # 캐시 저장 (24시간 유효)
                cache.set(cache_key, True, 60*60*24)
        
        # product.view_count += 1
        # product.save()
        
        serializer = ProductDetailSerializer(product)  # 상세 Serializer 사용
        return Response(serializer.data)
    
    def put(self, request, productId):
        """상품 수정"""
        product = self.get_object(productId)
        serializer = ProductDetailSerializer(product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, productId):
        """상품 삭제"""
        product = self.get_object(productId)
        product.delete()
        data = {"pk": f"{productId} is deleted."}
        return Response(data, status=status.HTTP_200_OK)
