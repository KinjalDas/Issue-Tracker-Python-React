# Generated by Django 2.2.6 on 2019-10-30 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='CRID',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='Component',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='Prog_or_Comm',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='Project',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='Title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]