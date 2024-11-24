# Generated by Django 5.0.6 on 2024-11-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("part", "0003_alter_part_amount_alter_part_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="part",
            name="description_en",
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="part",
            name="description_ko",
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="part",
            name="description_ru",
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="part",
            name="name_en",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="part",
            name="name_ko",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="part",
            name="name_ru",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
