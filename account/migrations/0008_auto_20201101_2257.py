# Generated by Django 3.1.2 on 2020-11-01 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20201031_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='public_birth',
            field=models.CharField(default='1', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='public_email',
            field=models.CharField(default='1', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='public_phone',
            field=models.CharField(default='1', max_length=1, null=True),
        ),
    ]