# Generated by Django 3.1.2 on 2020-11-27 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_asset_downloadable'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]