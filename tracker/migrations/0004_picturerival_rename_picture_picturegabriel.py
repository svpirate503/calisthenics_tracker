# Generated by Django 4.2.6 on 2024-11-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_picture_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureRival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='profile_pictures')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Picture',
            new_name='PictureGabriel',
        ),
    ]
