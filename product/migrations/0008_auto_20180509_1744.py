# Generated by Django 2.0.3 on 2018-05-09 09:44

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0009_auto_20180507_1653'),
        ('taggit', '0002_auto_20150616_2121'),
        ('product', '0007_auto_20180507_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='product',
            name='display',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.RemoveField(
            model_name='product',
            name='to_category',
        ),
        migrations.AddField(
            model_name='product',
            name='to_category',
            field=models.ManyToManyField(blank=True, null=True, related_name='c_products', to='category.Category'),
        ),
    ]
