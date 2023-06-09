# Generated by Django 4.2.1 on 2023-05-04 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_alter_gamemaster_id_alter_player_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='firstname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='lastname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
