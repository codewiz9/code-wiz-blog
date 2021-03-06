# Generated by Django 3.2 on 2022-04-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, max_length=1000, null=True)),
                ('post_title', models.CharField(max_length=100, null=True)),
                ('blog_content', models.TextField(max_length=10000, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to='blog_app.IpModel')),
            ],
        ),
    ]
