# Generated by Django 4.2.8 on 2025-01-01 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_user_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthday",
            field=models.DateField(
                blank=True, null=True, verbose_name="생일(YYYY-MM-DD)"
            ),
        ),
    ]
