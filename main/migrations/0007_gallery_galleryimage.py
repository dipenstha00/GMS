# Generated by Django 4.1.7 on 2023-02-21 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('detail', models.TextField()),
                ('img', models.ImageField(upload_to='gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_text', models.CharField(max_length=150)),
                ('img', models.ImageField(upload_to='gallery_imgs/')),
            ],
        ),
    ]
