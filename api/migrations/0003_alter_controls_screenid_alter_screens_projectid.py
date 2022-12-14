# Generated by Django 4.0.3 on 2022-07-31 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_controls_controlid_remove_project_projectid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controls',
            name='screenID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='controls', to='api.screens'),
        ),
        migrations.AlterField(
            model_name='screens',
            name='projectID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screens', to='api.project'),
        ),
    ]
