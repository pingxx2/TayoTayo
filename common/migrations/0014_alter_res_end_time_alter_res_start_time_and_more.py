# Generated by Django 4.1.1 on 2023-02-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0013_alter_res_end_time_alter_res_start_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="res", name="end_time", field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="res",
            name="start_time",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="res",
            name="time",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
