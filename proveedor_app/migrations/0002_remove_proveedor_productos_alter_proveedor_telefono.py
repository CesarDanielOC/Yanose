# Generated by Django 5.1 on 2024-11-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='productos',
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(max_length=100),
        ),
    ]
