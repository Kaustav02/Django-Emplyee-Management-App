# Generated by Django 4.2.2 on 2023-06-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employ', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='depertment',
        ),
        migrations.AlterField(
            model_name='emp',
            name='adress',
            field=models.CharField(default='', max_length=200),
        ),
    ]
