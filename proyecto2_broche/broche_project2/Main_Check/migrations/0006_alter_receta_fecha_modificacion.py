# Generated by Django 3.2.2 on 2021-05-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Check', '0005_auto_20210512_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
