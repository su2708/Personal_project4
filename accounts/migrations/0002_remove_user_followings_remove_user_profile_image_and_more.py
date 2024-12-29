# Generated by Django 4.2.8 on 2024-12-29 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="followings",
        ),
        migrations.RemoveField(
            model_name="user",
            name="profile_image",
        ),
        migrations.AddField(
            model_name="user",
            name="birthday",
            field=models.DateField(auto_now=True, verbose_name="생일(YYYY-MM-DD)"),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=150, unique=True, verbose_name="닉네임"),
        ),
        migrations.DeleteModel(
            name="Follow",
        ),
    ]