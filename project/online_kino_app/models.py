from django.db import models


class Films(models.Model):
    name = models.CharField(max_length=30)
    release = models.IntegerField()
    country = models.CharField(max_length=40)
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name},{self.release},{self.country},{self.director},{self.genre}'


class Director(models.Model):
    name = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name},{self.birthday}'


class Genre(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name}'


class Afisha(models.Model):
    date = models.DateField()
    films = models.ManyToManyField('Films')


    def __str__(self):
        return f'{self.date},{self.films}'