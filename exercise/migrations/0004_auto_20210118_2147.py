# Generated by Django 2.1 on 2021-01-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_auto_20201231_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinexercise',
            name='date',
            field=models.DateField(),
        ),
    ]