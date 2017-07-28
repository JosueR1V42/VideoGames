from django.db import models


# Create your models here.
class creator(model.Model):
	name = models.CharField(max_lenght=50,help_text='Escriba el nombre del autor')
	email = models.EmailField(help_text='Escriba el correo de contacto del autor')

class game(models.Model):
    """
    almacena los juegos mediante el equipo de
    administracion
    """
    opinion=models.CharField(max_lenght=50,help_text='Ingrese el Titulo del juego a ingresar: ')
    title=models.CharField(max_lenght=30, help_text='Titulo del videojuego ')
    creatores=models.ForeignKey(creator,help_text='Nombre del o los creadores ')
    synopsis=models.TextField(max_lenght=300, help_text='Historia del Videojuego ')
    pubdate=models.DateTimeField(help_text='Fecha y hora de la puclicacion del videojuego ')
    clasification=models.DecimalField(max_lenght=5, help_text='Clasificacion del videojuego ')
    genere=models.CharField(max_lenght=50, help_text='Genero del videojuego ')
    console=models.CharField(max_lenght=50, help_text='Plataforma de videojuego ')

class review(models.Model):
    review=models.IntegerField(max_lenght=1,help_text='Opiniones ')
	game=models.ForeignKey(game,help_text='Selecione el juego que desea hacer la sinopsis')
