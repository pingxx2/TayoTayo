# Generated by Django 4.1.1 on 2023-02-03 01:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0006_parking_parking_name_alter_parking_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parking",
            name="owner",
            field=models.ForeignKey(
                db_column="owner",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="parking",
            name="parking_name",
            field=models.CharField(max_length=20),
        ),
    ]
