# Generated by Django 5.0 on 2024-04-04 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0003_alter_recipe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='id',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ID',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
    ]
