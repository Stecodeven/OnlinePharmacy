# Generated by Django 2.0.3 on 2018-05-07 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0009_auto_20180507_1653'),
        ('product', '0004_product_to_kind'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='to_kind',
        ),
        migrations.AddField(
            model_name='product',
            name='to_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='c_products', to='category.Category'),
            preserve_default=False,
        ),
    ]
