# Generated by Django 3.2.18 on 2023-02-22 21:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CnpjCei',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ccm', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('identification_number', models.CharField(max_length=14, verbose_name='Numero de Identificação')),
                ('type_identification', models.IntegerField(choices=[(0, 'CNPJ'), (1, 'CEI'), (2, 'CAEPF')], verbose_name='Tipo')),
                ('address', models.TextField(verbose_name='Endereço')),
                ('cnae', models.CharField(max_length=9)),
            ],
            options={
                'verbose_name': 'CnpjCei',
                'verbose_name_plural': 'CnpjCeis',
                'managed': True,
            },
        ),
    ]