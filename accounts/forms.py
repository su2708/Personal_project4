from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.urls import reverse

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # 현재 활성화된 user model인 User를 model로 사용 
        fields = UserCreationForm.Meta.fields + ()

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()  # 현재 프로젝트에서 활성화 되어있는 유저를 반환 
        fields = [
            "first_name",
            "last_name",
            "email",
        ]
    
    #  비밀번호 수정 경로를 커스텀 할 수 있도록 UserChangeForm의 __init__을 Overriding
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields.get("password"):
            # reverse: url_name으로부터 url을 찾아가는 함수 
            password_help_text = (
                "You can change the password " '<a href="{}">here</a>.'
            ).format(f"{reverse('accounts:change_password')}")
            self.fields["password"].help_text = password_help_text