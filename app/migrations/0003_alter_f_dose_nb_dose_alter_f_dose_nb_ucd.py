# Generated by Django 5.0.2 on 2024-02-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_d_depart_code_depart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f_dose',
            name='nb_dose',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='f_dose',
            name='nb_ucd',
            field=models.FloatField(),
        ),
    ]
