# Generated by Django 5.0 on 2023-12-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_alter_women_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=0),
        ),
    ]
