from .models import Product
from .forms import ProductForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

# Create your views here.
def index(request):
    return render(request, "products/index.html")

def products(request):
    products = Product.objects.all().order_by("-id")
    context = {"products": products}
    return render(request, "products/products.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "products/product_detail.html", context)

@login_required
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)  # 데이터가 바인딩된(값이 채워진) Form
        if form.is_valid():  # Form이 유효하다면 데이터를 저장하고 다른 곳으로 redirect
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect("products:product_detail", product.pk)
    # 기존 new 함수 부분
    else:
        form = ProductForm()

    context = {"form": form}
    return render(request, "products/create.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.author == request.user:
        if request.method == "POST":
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                product = form.save()
                return redirect("products:product_detail", product.pk)
        else:
            form = ProductForm(instance=product)
        context = {
            "form": form,
            "product": product,
        }
        return render(request, "products/update.html", context)
    else:
        return redirect("products:products")

@require_POST
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.is_authenticated:
        if product.author == request.user:
            product = get_object_or_404(Product, pk=pk)
            product.delete()
    return redirect("products:products")

@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
    else:
        return redirect("accounts:login")
    
    return redirect("products:products")