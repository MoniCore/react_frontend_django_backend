# Generated by Django 3.1.2 on 2020-10-31 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_postattach_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]
