#accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'email', 'password', 'password2', 'username', 'birthday'
        )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                "password": "비밀번호가 일치하지 않습니다."
            })
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # password2 제거
        return User.objects.create_user(**validated_data)

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'profile_image']  # 반환할 필드

class UserProfileSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ['email', 'username', 'birthday']  # 반환할 필드



class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'birthday')  # 수정 가능한 필드
