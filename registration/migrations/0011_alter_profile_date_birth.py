# Generated by Django 5.1.3 on 2025-01-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_profile_date_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_birth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
    ]
