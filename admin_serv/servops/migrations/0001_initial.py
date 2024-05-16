# Generated by Django 5.0.6 on 2024-05-16 13:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='logos/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('num_processors', models.IntegerField()),
                ('memory_capacity', models.IntegerField()),
                ('storage_capacity', models.IntegerField()),
                ('server_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servers', to='servops.servertype')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('launch_date', models.DateField()),
                ('memory_used', models.IntegerField()),
                ('required_memory', models.IntegerField()),
                ('launch_server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='servops.server')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource_usages', to='servops.application')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource_usages', to='servops.service')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='services',
            field=models.ManyToManyField(related_name='applications', to='servops.service'),
        ),
    ]