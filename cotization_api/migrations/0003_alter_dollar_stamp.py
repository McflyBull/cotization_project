# Generated by Django 4.1.1 on 2022-10-02 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotization_api', '0002_alter_dollar_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dollar',
            name='stamp',
            field=models.DateTimeField(),
        ),
    ]
