# Generated by Django 3.1.5 on 2021-05-27 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Departments', '0001_initial'),
        ('teachers', '0008_post_year_taken'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpPostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='teacher',
            unique_together={('first_name', 'last_name', 'dept')},
        ),
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='review_dislikes', to='teachers.IpPostModel'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='review_likes', to='teachers.IpPostModel'),
        ),
    ]