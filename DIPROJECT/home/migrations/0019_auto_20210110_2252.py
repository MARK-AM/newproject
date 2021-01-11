# Generated by Django 3.1.4 on 2021-01-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_news_img1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='news',
            name='link',
        ),
        migrations.AlterField(
            model_name='info',
            name='causes',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='info',
            name='overview',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='info',
            name='prev',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='info',
            name='risk',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='info',
            name='symptoms',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(default='', max_length=100),
        ),
    ]