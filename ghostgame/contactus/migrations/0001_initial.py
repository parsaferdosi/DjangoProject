# Generated by Django 5.0.7 on 2024-09-17 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=16)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=256)),
                ('subject', models.CharField(max_length=16)),
                ('message', models.TextField()),
                ('timecreat', models.TimeField()),
            ],
        ),
    ]
