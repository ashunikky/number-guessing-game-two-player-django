# Generated by Django 4.2.1 on 2023-05-04 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_gamemaster_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemaster',
            name='player',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player', to='game.player'),
        ),
    ]