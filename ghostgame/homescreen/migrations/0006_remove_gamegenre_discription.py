# Generated by Django 5.0.7 on 2024-09-15 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homescreen', '0005_gamegenre_suggestion_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamegenre',
            name='discription',
        ),
    ]
