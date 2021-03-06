# Generated by Django 2.2.10 on 2020-08-18 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('market', '0004_auto_20200818_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Товар')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Цена')),
                ('product_number', models.IntegerField(unique=True, verbose_name='Артикул товара')),
                ('img', models.ImageField(blank=True, upload_to='media/img/', verbose_name='Изображение')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=512, verbose_name='Описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products',
                                               to='market.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
