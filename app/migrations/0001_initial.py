# Generated by Django 2.1.5 on 2019-01-20 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feira',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('long', models.CharField(max_length=255)),
                ('referecia', models.CharField(max_length=255)),
            ],
        ),
    ]
