# Generated by Django 2.0.3 on 2018-05-07 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_floor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='floor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='kinds',
            name='to_category',
        ),
        migrations.AddField(
            model_name='category',
            name='to_kinds',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='k_category', to='category.Kinds'),
            preserve_default=False,
        ),
    ]