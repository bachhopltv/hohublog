# Generated by Django 3.2.8 on 2021-10-06 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_auto_20211006_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=255),
        ),
    ]
