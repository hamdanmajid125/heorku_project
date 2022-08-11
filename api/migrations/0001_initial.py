# Generated by Django 4.0.3 on 2022-04-05 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectID', models.IntegerField(primary_key=True, serialize=False)),
                ('projectTitle', models.CharField(max_length=100)),
                ('projectDate', models.DateTimeField(auto_now=True)),
                ('projectCategory', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Screens',
            fields=[
                ('screenID', models.IntegerField(primary_key=True, serialize=False)),
                ('screenTitle', models.CharField(max_length=50)),
                ('projectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project')),
            ],
        ),
        migrations.CreateModel(
            name='Controls',
            fields=[
                ('controlID', models.IntegerField(primary_key=True, serialize=False)),
                ('controlTitle', models.TextField()),
                ('controlsType', models.TextField()),
                ('screenID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.screens')),
            ],
        ),
    ]
