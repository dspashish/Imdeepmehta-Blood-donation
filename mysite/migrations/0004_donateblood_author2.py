# Generated by Django 2.1 on 2020-03-23 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_donateblood_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='donateblood',
            name='author2',
            field=models.CharField(default='ashish', max_length=200),
            preserve_default=False,
        ),
    ]
