# Generated by Django 4.1.7 on 2023-02-25 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_gallery_options_alter_notify_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='instagram',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='twitter',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='youtube',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
