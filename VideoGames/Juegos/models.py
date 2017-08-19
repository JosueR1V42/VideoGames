from django.db import models

__author__="Josue David Rivas"
__copyright__="Copyright 2017"
__credits__=["Josue David Rivas", "Cynthia Graciela Palma"]
__license__="MIT"
__version__="1.0.0"
__maintainer__="Josue David Rivas"
__email__="davixback@gmail.com"
__status__="Development"


# Create your models here.
class creator(models.Model):
	generes=(
		('F','Female'),
		('M','Male')
	)
	name=models.CharField(max_length=25,help_text='Nombre del creador ')
	birthday=models.DateField(help_text='Fecha de nacimiento')
	genere=models.CharField(max_length=1,help_text='Coloque el sexo del creador', choices=generes)

class games(models.Model):
	"""
	almacena los juegos mediante el equipo de
	administracion
	"""
	title=models.CharField(max_length=30, help_text='Titulo del videojuego ')
	creatores=models.ForeignKey(creator,help_text='Nombre del o los creadores ')
	synopsis=models.TextField(max_length=2000, help_text='Historia del Videojuego ')
	pubdate=models.DateTimeField(help_text='Fecha y hora de la puclicacion del videojuego ')
	genere=models.CharField(max_length=50, help_text='Genero del videojuego ')
	console=models.CharField(max_length=50, help_text='Plataforma de videojuego ')
	company=models.CharField(max_length=30,help_text='Compañia Desarrolladora')

class review(models.Model):
	review=models.CharField(max_length=100,help_text='Opiniones ')
	game=models.ForeignKey(games,help_text='Selecione el juego que desea hacer la sinopsis')

class score(models.Model):
	score=models.IntegerField(games,help_text='Puntuacion del videojuego (0-5)')
