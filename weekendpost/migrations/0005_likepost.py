# Generated by Django 4.1.1 on 2023-01-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weekendpost', '0004_posts_post_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('liked_by', models.CharField(max_length=100)),
            ],
        ),
    ]
