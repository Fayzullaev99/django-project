# Generated by Django 5.1.4 on 2025-04-12 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='shop.category')),
            ],
            options={
                'verbose_name': 'SubCategory',
                'verbose_name_plural': 'SubCategories',
            },
        ),
    ]
