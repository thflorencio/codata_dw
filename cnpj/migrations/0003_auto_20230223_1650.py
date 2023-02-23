# Generated by Django 3.2.18 on 2023-02-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnpj', '0002_auto_20230223_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnpjcei',
            name='complement_address',
            field=models.CharField(max_length=50, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='cnpjcei',
            name='main_cnae',
            field=models.CharField(max_length=10, verbose_name='Principal CNAE'),
        ),
        migrations.AlterField(
            model_name='cnpjcei',
            name='neighborhood',
            field=models.CharField(max_length=50, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='cnpjcei',
            name='state',
            field=models.CharField(max_length=2, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='cnpjcei',
            name='street',
            field=models.CharField(max_length=250, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='cnpjcei',
            name='street_number',
            field=models.CharField(max_length=10, verbose_name='Numero'),
        ),
        migrations.AlterField(
            model_name='cnpjcei',
            name='zipcode',
            field=models.CharField(max_length=8, verbose_name='Código Postal'),
        ),
    ]
