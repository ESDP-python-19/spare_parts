# Generated by Django 5.0.6 on 2024-11-12 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0003_remove_contactrequest_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactrequest",
            name="is_new",
            field=models.BooleanField(default=True, verbose_name="Новый"),
        ),
    ]
