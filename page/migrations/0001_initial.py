# Generated by Django 3.0 on 2019-12-05 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_1', models.BigIntegerField()),
                ('number_2', models.BigIntegerField()),
            ],
        ),
    ]
