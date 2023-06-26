# Generated by Django 4.2 on 2023-06-26 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gview', '0003_cat_owns_cat_score_dog_owner_dog_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='pets',
        ),
        migrations.AlterField(
            model_name='cat',
            name='owns',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gview.owner'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gview.owner'),
        ),
    ]
