# Generated by Django 5.1 on 2024-08-13 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RollerSkate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('size', models.IntegerField(blank=True, choices=[(28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34')])),
                ('barcode', models.IntegerField(blank=True)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rollerskates', to='RollerSkateInventory.inventory')),
            ],
        ),
    ]
