# Generated by Django 3.1.5 on 2021-03-09 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Departments', '0001_initial'),
        ('teachers', '0005_auto_20210219_2112'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.AddField(
            model_name='teacher',
            name='dept',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, to='Departments.department'),
        ),
    ]
