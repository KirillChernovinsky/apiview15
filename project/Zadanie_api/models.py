from django.db import models

# Create your models here.


class Tovar(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField() # '2011-10-10 00:00:00'
    maker = models.ForeignKey('Maker', on_delete=models.CASCADE)
    category = models.ManyToManyField('Category')
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name},{self.size},{self.maker},{self.category},{self.price}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'


class Maker(models.Model):
    firm_name = models.CharField(max_length=100)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.firm_name}'