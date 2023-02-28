# Generated by Django 3.2.18 on 2023-02-28 14:59

import codata_dw.base_models.base_spreedsheets
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnpj', '0010_auto_20230227_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='spreedsheets',
            name='errors',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='spreedsheets',
            name='spreedsheet',
            field=models.FileField(upload_to=codata_dw.base_models.base_spreedsheets.file_name),
        ),
    ]