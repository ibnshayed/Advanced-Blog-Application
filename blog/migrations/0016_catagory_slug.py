# Generated by Django 3.1.5 on 2021-05-18 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20210517_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
