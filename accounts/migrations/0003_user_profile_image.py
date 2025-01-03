# Generated by Django 4.2.8 on 2025-01-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_remove_user_followings_remove_user_profile_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="profile_images/",
                verbose_name="프로필 이미지",
            ),
        ),
    ]
