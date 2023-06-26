# Generated by Django 4.2 on 2023-06-26 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gview', '0002_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='owns',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gview.owner'),
        ),
        migrations.AddField(
            model_name='cat',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='gview.owner'),
        ),
        migrations.AddField(
            model_name='dog',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
