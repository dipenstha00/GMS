# Generated by Django 4.1.7 on 2023-02-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
    ]
