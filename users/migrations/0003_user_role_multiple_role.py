# Generated by Django 2.2.2 on 2019-06-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190611_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_role',
            name='multiple_role',
            field=models.BooleanField(default=False),
        ),
    ]
