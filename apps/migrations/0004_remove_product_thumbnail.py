# Generated by Django 4.2.3 on 2023-07-07 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_product_thumbnail_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
    ]
