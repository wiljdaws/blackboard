# Generated by Django 5.0.2 on 2024-04-12 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_dayofweek_remove_course_days_of_week_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='days_of_week',
        ),
    ]
