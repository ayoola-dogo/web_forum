# Generated by Django 3.0.5 on 2020-04-30 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200422_2239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': ['posted_date'], 'ordering': ['posted_date']},
        ),
    ]
