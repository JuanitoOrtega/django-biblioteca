# Generated by Django 4.1.5 on 2023-01-26 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_book', to='book.category', verbose_name='Categoría'),
        ),
    ]
