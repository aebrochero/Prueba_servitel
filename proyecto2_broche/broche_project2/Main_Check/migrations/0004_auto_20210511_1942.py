# Generated by Django 3.2.2 on 2021-05-11 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Check', '0003_receta_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='calorias',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receta',
            name='origen',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='receta',
            name='valor',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
