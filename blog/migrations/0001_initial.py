# Generated by Django 2.0.2 on 2018-06-20 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('blog_image', models.ImageField(upload_to='images/')),
                ('body', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
