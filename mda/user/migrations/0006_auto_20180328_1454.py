# Generated by Django 2.0.3 on 2018-03-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
