# Generated by Django 4.1.1 on 2022-11-10 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weekendpost', '0002_remove_posts_like_commends_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commends',
            name='like',
        ),
    ]
