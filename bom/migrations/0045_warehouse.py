# Generated by Django 3.2.4 on 2022-05-27 07:25

import bom.base_classes
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0044_auto_20220524_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('location', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bom.organization')),
            ],
            options={
                'unique_together': {('name', 'location')},
            },
            bases=(models.Model, bom.base_classes.AsDictModel),
        ),
    ]
