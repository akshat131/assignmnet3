# Generated by Django 3.0.5 on 2020-04-21 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20200421_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='vailability',
        ),
        migrations.AddField(
            model_name='tool',
            name='availability',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
