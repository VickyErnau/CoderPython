# Generated by Django 5.1.4 on 2025-01-12 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0006_remove_posteo_categorias_posteo_categoria_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteo',
            name='categoria',
        ),
        migrations.AddField(
            model_name='posteo',
            name='categorias',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='posteo',
            name='autor',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
