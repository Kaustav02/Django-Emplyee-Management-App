# Generated by Django 4.2.2 on 2023-07-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employ', '0002_remove_emp_depertment_alter_emp_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='depertment',
            field=models.CharField(default='CSE', max_length=10),
        ),
    ]