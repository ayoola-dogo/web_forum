# Generated by Django 3.0.5 on 2020-04-21 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('Account Support', 'Account Support'), ('Vendor Support', 'Vendor Support'), ('General Support', 'General Support'), ('Market Place Support', 'Market Place Support')], max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VendorSupportMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(choices=[('Vendor Account', 'Vendor Account'), ('Products', 'Products'), ('Payment Processing', 'Payment Processing'), ('Report a Buyer', 'Report a Buyer')], max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField()),
                ('main_category', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='support.MainSupport')),
            ],
        ),
        migrations.CreateModel(
            name='MarketSupportMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(choices=[('Customer Support', 'Customer Support'), ('Report a Seller', 'Report a Seller'), ('Request a Refund', 'Request a Refund'), ('Cryptocurrency Issues', 'cryptocurrency Issues'), ('Miscellaneous', 'miscellaneous')], max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField()),
                ('main_category', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='support.MainSupport')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralSupportMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(choices=[('Vendor Account', 'Vendor Account'), ('Products', 'Products'), ('Payment Processing', 'Payment Processing'), ('Report a Buyer', 'Report a Buyer')], max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField()),
                ('main_category', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='support.MainSupport')),
            ],
        ),
        migrations.CreateModel(
            name='AccountSupportMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(choices=[('New Account', 'New Account'), ('Password Reset', 'Password Reset'), ('Close Account', 'Close Account'), ('Vendor Account', 'Vendor Account'), ('Profile Issues', 'Profile Issues')], max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField()),
                ('main_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='support.MainSupport')),
            ],
        ),
    ]
