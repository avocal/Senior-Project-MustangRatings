# Generated by Django 3.1.5 on 2021-05-21 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='staffreview',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='review_dislikes', to='faculty_staff.IpModel'),
        ),
        migrations.AddField(
            model_name='staffreview',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='review_likes', to='faculty_staff.IpModel'),
        ),
    ]