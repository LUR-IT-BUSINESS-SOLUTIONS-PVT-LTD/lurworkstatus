# Generated by Django 4.2.5 on 2023-12-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lur_monitor', '0012_alter_company_clogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='cName',
            field=models.CharField(max_length=50, primary_key='true', serialize=False),
        ),
        migrations.AlterField(
            model_name='empid',
            name='Empid',
            field=models.CharField(max_length=50, primary_key='true', serialize=False),
        ),
    ]