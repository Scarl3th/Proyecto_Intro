# Generated by Django 3.2.9 on 2021-12-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pag_calendario', '0006_alter_eliminar_event_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eliminar',
            name='event_id',
            field=models.CharField(max_length=120),
        ),
    ]
