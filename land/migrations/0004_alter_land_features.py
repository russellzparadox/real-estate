# Generated by Django 5.0.6 on 2024-07-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0003_status_typeofpropertyuse_alter_land_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='lands', to='land.feature'),
        ),
    ]
