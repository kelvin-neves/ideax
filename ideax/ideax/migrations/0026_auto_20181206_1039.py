# Generated by Django 2.0.9 on 2018-12-06 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideax', '0025_auto_20181108_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='init_date',
            field=models.DateTimeField(),
        ),
    ]