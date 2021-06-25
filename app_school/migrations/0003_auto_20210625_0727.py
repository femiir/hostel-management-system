# Generated by Django 3.2.4 on 2021-06-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_school', '0002_schooladmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='schooladmin',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='school',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='schooladmin',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='schooladmin',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
