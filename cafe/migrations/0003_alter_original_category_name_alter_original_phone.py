# Generated by Django 4.1.1 on 2022-11-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cafe", "0002_alter_original_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="original",
            name="category_name",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="original",
            name="phone",
            field=models.CharField(max_length=20, null=True, verbose_name="전화번호"),
        ),
    ]