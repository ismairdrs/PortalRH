# Generated by Django 2.2.17 on 2020-11-22 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=2500)),
                ('location', models.CharField(max_length=60)),
                ('salary', models.IntegerField()),
                ('name_company', models.CharField(max_length=60, null=True)),
                ('email_contact', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Resumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('github', models.CharField(max_length=250)),
                ('linkedin', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=2000)),
                ('experience', models.CharField(max_length=2000)),
                ('formations', models.CharField(max_length=2000)),
                ('skills', models.CharField(max_length=2000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]