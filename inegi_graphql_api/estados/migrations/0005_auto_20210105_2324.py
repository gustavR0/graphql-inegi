# Generated by Django 3.1.3 on 2021-01-05 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estados', '0004_auto_20210105_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]