from django.db import models
from django.contrib.auth.models import User


# Create your models here. 
# year.strftime('%Y')
#{{ year|date: "Y" }}
# modelo temporada
class Season(models.Model):
    season = models.DateField(verbose_name='Temporada')

    class Meta:
        verbose_name = 'Temporada'
        verbose_name_plural = 'Temporadas'

    def __str__(self):
        return self.season.strftime('%Y')

class Contry(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    image = models.ImageField(verbose_name='Imagen', upload_to='contry', null=True, blank=True)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        
    def __str__(self):
        return self.name

class League(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Temporada')
    contry = models.ForeignKey(Contry, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Pais')
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = 'Liga'
        verbose_name_plural = 'Ligas'
        ordering = ['name']
        
    
    def __str__(self):
        return self.name

class Team(models.Model):
    team = models.CharField(max_length=50, verbose_name='Equipo')
    league = models.ForeignKey(League, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Liga')
    image = models.ImageField(verbose_name='Imagen', upload_to='team')
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['team']
        
    
    def __str__(self):
        return self.team


class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Liga')
    soccer_day = models.SmallIntegerField(verbose_name='Jornada', null=True, blank=True)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Equipo local',related_name='home_matches')
    visit_team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Equipo visitante',related_name='visit_matches')
    date = models.DateField(verbose_name='Fecha')
    gol_home_ht = models.IntegerField(verbose_name='Goles Equipo Local HT', blank=True, null=True)
    gol_visit_ht = models.IntegerField(verbose_name='Goles Equipo Visitante HT', blank=True, null=True)
    gol_home_ft = models.IntegerField(verbose_name='Goles Equipo Local FT', blank=True, null=True)
    gol_visit_ft = models.IntegerField(verbose_name='Goles Equipo Visitante FT', blank=True, null=True)
    goles_tramo_1_10 = models.IntegerField(verbose_name='Goles del 1 al 10', blank=True, null=True)
    goles_tramo_11_20 = models.IntegerField(verbose_name='Goles del 11 al 20', blank=True, null=True)
    goles_tramo_21_30 = models.IntegerField(verbose_name='Goles del 21 al 30', blank=True, null=True)
    goles_tramo_31_40 = models.IntegerField(verbose_name='Goles del 31 al 40', blank=True, null=True)
    goles_tramo_41_50 = models.IntegerField(verbose_name='Goles del 41 al 50', blank=True, null=True)
    goles_tramo_51_60 = models.IntegerField(verbose_name='Goles del 51 al 60', blank=True, null=True)
    goles_tramo_61_70 = models.IntegerField(verbose_name='Goles del 61 al 70', blank=True, null=True)
    goles_tramo_71_80 = models.IntegerField(verbose_name='Goles del 71 al 80', blank=True, null=True)
    goles_tramo_81_90 = models.IntegerField(verbose_name='Goles del 81 al 90', blank=True, null=True)
    goles_tramo_91_final = models.IntegerField(verbose_name='Goles del 91 al final', blank=True, null=True)
    

    class Meta:
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'
        ordering = ['date']
        
    
    def __str__(self):
        return '{} {}'.format(self.home_team, self.visit_team)


class Strategy(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    valor_ini_over_05_ht = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_over_05_ht = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_over_15_ht = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_over_15_ht = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_over_05_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_over_05_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_over_15_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_over_15_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_over_25_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_over_25_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_aem = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_aem = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_local_anota_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_local_anota_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_local_anota_mitad_1 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_local_anota_mitad_1 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_local_anota_mitad_2 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_local_anota_mitad_2 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_visitante_anota_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_visitante_anota_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_visitante_anota_mitad_1 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_visitante_anota_mitad_1 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_visitante_anota_mitad_2 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_visitante_anota_mitad_2 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_local_concede_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_local_concede_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_local_concede_mitad_1 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_local_concede_mitad_1 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_local_concede_mitad_2 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_local_concede_mitad_2 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_visitante_concede_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_visitante_concede_ft = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_visitante_concede_mitad_1 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_visitante_concede_mitad_1 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_visitante_concede_mitad_2 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_visitante_concede_mitad_2 = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_local_favorito = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_local_favorito = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_ini_visitante_favorito = models.PositiveSmallIntegerField(null=True, blank=True)
    valor_fin_visitante_favorito = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Estrategia'
        verbose_name_plural = 'Estrategias'
        
    def __str__(self):
        return self.name