# Generated by Django 4.1.7 on 2023-02-21 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_subscriptionfeature_subs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='max_member',
            field=models.IntegerField(null=True),
        ),
    ]