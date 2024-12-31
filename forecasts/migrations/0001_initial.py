# Generated by Django 5.1.3 on 2024-12-31 10:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('image', models.ImageField(blank=True, null=True, upload_to='contry', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.DateField(verbose_name='Temporada')),
            ],
            options={
                'verbose_name': 'Temporada',
                'verbose_name_plural': 'Temporadas',
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('contry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecasts.contry', verbose_name='Pais')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecasts.season', verbose_name='Temporada')),
            ],
            options={
                'verbose_name': 'Liga',
                'verbose_name_plural': 'Ligas',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('valor_ini_over_05_ht', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_over_05_ht', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_over_15_ht', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_over_15_ht', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_over_05_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_over_05_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_over_15_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_over_15_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_over_25_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_over_25_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_aem', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_aem', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_local_anota_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_local_anota_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_local_anota_mitad_1', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_local_anota_mitad_1', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_local_anota_mitad_2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_local_anota_mitad_2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_visitante_anota_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_visitante_anota_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_visitante_anota_mitad_1', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_visitante_anota_mitad_1', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_visitante_anota_mitad_2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_visitante_anota_mitad_2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_local_concede_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_local_concede_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_local_concede_mitad_1', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_local_concede_mitad_1', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_local_concede_mitad_2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_local_concede_mitad_2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_visitante_concede_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_visitante_concede_ft', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_visitante_concede_mitad_1', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_visitante_concede_mitad_1', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_visitante_concede_mitad_2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_visitante_concede_mitad_2', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_local_favorito', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_local_favorito', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_ini_visitante_favorito', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_fin_visitante_favorito', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Estrategia',
                'verbose_name_plural': 'Estrategias',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50, verbose_name='Equipo')),
                ('image', models.ImageField(upload_to='team', verbose_name='Imagen')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecasts.league', verbose_name='Liga')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'ordering': ['team'],
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soccer_day', models.SmallIntegerField(blank=True, null=True, verbose_name='Jornada')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('gol_home_ht', models.IntegerField(blank=True, null=True, verbose_name='Goles Equipo Local HT')),
                ('gol_visit_ht', models.IntegerField(blank=True, null=True, verbose_name='Goles Equipo Visitante HT')),
                ('gol_home_ft', models.IntegerField(blank=True, null=True, verbose_name='Goles Equipo Local FT')),
                ('gol_visit_ft', models.IntegerField(blank=True, null=True, verbose_name='Goles Equipo Visitante FT')),
                ('goles_tramo_1_10', models.IntegerField(blank=True, null=True, verbose_name='Goles del 1 al 10')),
                ('goles_tramo_11_20', models.IntegerField(blank=True, null=True, verbose_name='Goles del 11 al 20')),
                ('goles_tramo_21_30', models.IntegerField(blank=True, null=True, verbose_name='Goles del 21 al 30')),
                ('goles_tramo_31_40', models.IntegerField(blank=True, null=True, verbose_name='Goles del 31 al 40')),
                ('goles_tramo_41_50', models.IntegerField(blank=True, null=True, verbose_name='Goles del 41 al 50')),
                ('goles_tramo_51_60', models.IntegerField(blank=True, null=True, verbose_name='Goles del 51 al 60')),
                ('goles_tramo_61_70', models.IntegerField(blank=True, null=True, verbose_name='Goles del 61 al 70')),
                ('goles_tramo_71_80', models.IntegerField(blank=True, null=True, verbose_name='Goles del 71 al 80')),
                ('goles_tramo_81_90', models.IntegerField(blank=True, null=True, verbose_name='Goles del 81 al 90')),
                ('goles_tramo_91_final', models.IntegerField(blank=True, null=True, verbose_name='Goles del 91 al final')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecasts.league', verbose_name='Liga')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='forecasts.team', verbose_name='Equipo local')),
                ('visit_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit_matches', to='forecasts.team', verbose_name='Equipo visitante')),
            ],
            options={
                'verbose_name': 'Partido',
                'verbose_name_plural': 'Partidos',
                'ordering': ['date'],
            },
        ),
    ]
