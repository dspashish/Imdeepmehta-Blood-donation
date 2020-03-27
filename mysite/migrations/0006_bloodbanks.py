# Generated by Django 2.1 on 2020-03-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20200323_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBanks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_bank_name', models.CharField(max_length=200)),
                ('contact_person', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=200)),
            ],
        ),
    ]
