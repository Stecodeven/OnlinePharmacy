# Generated by Django 2.0.3 on 2018-05-07 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_auto_20180507_1627'),
        ('product', '0003_remove_product_to_floor'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='to_kind',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='k_products', to='category.Kinds'),
            preserve_default=False,
        ),
    ]