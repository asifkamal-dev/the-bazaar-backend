# Generated by Django 3.2.7 on 2021-09-14 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0002_auto_20210912_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default='This is going to be the basic description for current category units.', max_length=2550),
            preserve_default=False,
        ),
    ]