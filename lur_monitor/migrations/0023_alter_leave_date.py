# Generated by Django 4.2.5 on 2023-12-28 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lur_monitor', '0022_leave_date_alter_leave_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]