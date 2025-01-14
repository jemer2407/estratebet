# Generated by Django 5.1.3 on 2025-01-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_remove_profile_date_birth_profile_adult'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_verified_update_email',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha verificación de actualización de correo electrónico'),
        ),
        migrations.AddField(
            model_name='profile',
            name='verification_update_email_token',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Token de verificación de actualización de correo electrónico'),
        ),
    ]
