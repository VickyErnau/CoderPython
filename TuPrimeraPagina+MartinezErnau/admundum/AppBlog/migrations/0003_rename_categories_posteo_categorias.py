# Generated by Django 5.1.4 on 2025-01-12 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_remove_posteo_categoria_posteo_categories_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posteo',
            old_name='categories',
            new_name='categorias',
        ),
    ]
