# Generated by Django 5.0.6 on 2024-06-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=120)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
    ]
