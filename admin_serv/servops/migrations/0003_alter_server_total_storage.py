# Generated by Django 5.0 on 2024-05-25 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servops', '0002_alter_server_total_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='total_storage',
            field=models.IntegerField(default=0),
        ),
    ]
