# Generated by Django 5.0.2 on 2024-03-10 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Default Course Name', max_length=50)),
                ('description', models.CharField(default='Default Description', max_length=200)),
                ('semester', models.CharField(default='Default Semester', max_length=50)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='main.professor')),
            ],
        ),
    ]
