from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
)
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserChangeForm, CustomUserCreationForm

@require_http_methods(["GET", "POST"])  # GET과 POST가 들어올 때만 login 실행 
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())  # 실제 로그인 처리를 진행하는 부분 
            
            # 로그인 성공하면 가려던 곳(next)으로 가고, 아니면 index로 이동 
            next_path = request.GET.get("next") or "index"
            return redirect(next_path)
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)

@require_POST  # POST 요청이 들어올 때만 logout 함수 실행 
def logout(request):
    if request.user.is_authenticated:  # user가 로그인 된 상태일 때 실행 
        auth_logout(request)  # 실제 로그아웃 처리를 진행하는 부분 
    return redirect("products:index")

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # 새로운 유저 회원가입 정보 저장 
            auth_login(request, user)  # 회원가입과 동시에 새 회원 정보로 로그인 
            return redirect("products:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()  # 회원 탈퇴 
        auth_logout(request)  # 세션 지우기 
    return redirect("products:index")

@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("products:index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("products:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)