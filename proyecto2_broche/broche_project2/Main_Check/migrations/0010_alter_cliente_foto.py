# Generated by Django 3.2.2 on 2021-05-12 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Check', '0009_cliente_segundo_apellido_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
