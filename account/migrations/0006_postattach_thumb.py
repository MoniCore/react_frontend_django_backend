# Generated by Django 3.1.2 on 2020-10-31 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20201030_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='postattach',
            name='thumb',
            field=models.FileField(default='', null=True, upload_to='thumb'),
        ),
    ]