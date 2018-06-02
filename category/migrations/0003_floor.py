# Generated by Django 2.0.3 on 2018-05-07 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180506_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('to_kinds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='k_floor', to='category.Kinds')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]