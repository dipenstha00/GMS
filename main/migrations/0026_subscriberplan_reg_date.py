# Generated by Django 4.1.7 on 2023-02-25 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_subscription_validity_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriberplan',
            name='reg_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
