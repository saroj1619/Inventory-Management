# Generated by Django 2.2.2 on 2019-06-12 17:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=1000)),
                ('vendor', models.CharField(max_length=100)),
                ('mrp', models.FloatField(blank=True, default=None, null=True)),
                ('batch_no', models.IntegerField()),
                ('batch_date', models.DateField(null=True)),
                ('quantity', models.IntegerField()),
                ('status', models.IntegerField(max_length=1)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]