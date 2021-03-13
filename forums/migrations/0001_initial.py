# Generated by Django 3.0.5 on 2020-04-14 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=120)),
                ('number_topics', models.IntegerField(default=0)),
                ('number_posts', models.IntegerField(default=0)),
                ('dir_image', models.ImageField(null=True, upload_to='directories/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=5000)),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('number_of_views', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('admin_message', models.TextField(blank=True, max_length=600, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('directory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.Directory')),
            ],
        ),
    ]
