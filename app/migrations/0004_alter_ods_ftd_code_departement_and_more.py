# Generated by Django 5.0.2 on 2024-03-04 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_f_dose_nb_dose_alter_f_dose_nb_ucd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ods_ftd',
            name='code_departement',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='ods_ftd',
            name='code_region',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='ods_ftd',
            name='date_fin_semaine',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='ods_ftd',
            name='libelle_departement',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='ods_ftd',
            name='libelle_region',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='ods_ftd',
            name='nb_doses',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='ods_ftd',
            name='nb_ucd',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='ods_ftd',
            name='type_de_vaccin',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
