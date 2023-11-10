# Generated by Django 4.2.6 on 2023-10-13 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_name', models.CharField(max_length=25)),
                ('picture', models.ImageField(upload_to='')),
                ('post_by', models.CharField(max_length=25)),
                ('post', models.DateField(auto_now=True)),
            ],
        ),
    ]