# Generated by Django 2.0.6 on 2019-02-28 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ValidationCWapp', '0004_auto_20190228_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(default=2019),
        ),
    ]
