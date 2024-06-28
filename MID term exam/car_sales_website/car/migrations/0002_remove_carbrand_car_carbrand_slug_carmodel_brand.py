# Generated by Django 5.0.6 on 2024-06-28 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbrand',
            name='car',
        ),
        migrations.AddField(
            model_name='carbrand',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='car.carbrand'),
            preserve_default=False,
        ),
    ]
