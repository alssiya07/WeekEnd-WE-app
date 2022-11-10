# Generated by Django 4.1.1 on 2022-11-10 13:02

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
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('description', models.CharField(max_length=500)),
                ('posted_date', models.DateField(auto_now_add=True)),
                ('like', models.ManyToManyField(related_name='liked_by', to=settings.AUTH_USER_MODEL)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commend', models.CharField(max_length=500)),
                ('commeded_date', models.DateField(auto_now_add=True)),
                ('commeded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('commeds_like', models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weekendpost.posts')),
            ],
        ),
    ]
