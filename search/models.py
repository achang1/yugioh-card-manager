from django.db import models


# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    attribute = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    rarity = models.CharField(max_length=5)
    colour = models.CharField(max_length=30)



# class Monster(models.Model):
#     attack_points = models.IntegerField(default=0)
#     defence_points = models.IntegerField(default=0)
#
# class Magic(models.Model):
#
# class Trap(models.Model):