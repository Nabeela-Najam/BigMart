# Generated by Django 5.0.4 on 2024-05-17 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='register_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(max_length=100, null=True)),
                ('remail', models.EmailField(max_length=100, null=True)),
                ('rpassword', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
