# Generated by Django 4.2.5 on 2023-12-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lur_monitor', '0024_remove_leave_date_remove_leave_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='leave',
            name='end_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='leave',
            name='start_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]