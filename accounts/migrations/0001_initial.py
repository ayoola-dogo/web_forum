# Generated by Django 3.0.5 on 2020-04-22 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership', models.CharField(choices=[('Free', 'Free'), ('Basic Plan', 'Basic Plan'), ('Standard Plan', 'Standard Plan'), ('Plus Plan', 'Plus Plan')], default='Free', max_length=100)),
                ('payments_method', models.CharField(max_length=100)),
                ('number_transactions', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]