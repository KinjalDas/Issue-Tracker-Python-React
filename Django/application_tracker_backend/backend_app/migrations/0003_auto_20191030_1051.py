# Generated by Django 2.2.6 on 2019-10-30 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0002_auto_20191030_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='Open',
            field=models.BooleanField(default=True),
        ),
    ]
