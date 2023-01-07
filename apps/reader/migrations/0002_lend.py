# Generated by Django 4.1.5 on 2023-01-06 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_published'),
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lend_date', models.DateTimeField(verbose_name='Fecha de préstamo')),
                ('return_date', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de devolución')),
                ('returned', models.BooleanField(default=False, verbose_name='Devuelto')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book', verbose_name='Libro')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader.reader', verbose_name='Lector')),
            ],
            options={
                'verbose_name': 'Préstamo',
                'verbose_name_plural': 'Préstamos',
            },
        ),
    ]