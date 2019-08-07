from django.db import models
from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((choice.name, choice.value) for choice in cls)

class Card(models.Model):
    class CardRarity(ChoiceEnum):
        COMMON = "Common"
        RARE = "Rare"
        SR = "Super Rare"
        UR = "Ultra Rare"
        ULT_RARE = "Ultimate Rare"
        GR = "Ghost Rare"
        GUR = "Gold Ultra Rare"

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)
    rarity = models.CharField(max_length=30, choices=CardRarity.choices())
    colour = models.CharField(max_length=30)

    class Meta:
        abstract = True
    
    def __str__(self):
        return str(self.name, type(self).__name__)

class Monster(Card):
    class CardAttribute(ChoiceEnum):
        DARK = "Dark"
        DIVINE = "Divine"
        EARTH = "Earth"
        FIRE = "Fire"
        LIGHT = "Light"
        WATER = "Water"
        WIND = "Wind"
    
    class CardType(ChoiceEnum):
        NORMAL = "Normal"
        EFFECT = "Effect"
        RITUAL = "Ritual"
        FUSION = "Fusion"
        SYNCHRO = "Synchro"
        XYZ = "XYZ"

    atk_pts = models.IntegerField(default=0)
    def_pts = models.IntegerField(default=0)
    attribute = models.CharField(max_length=30, choices=CardAttribute.choices())
    card_type = models.CharField(max_length=30, choices=CardType.choices())
    level = models.IntegerField(default=0)
    effect = models.BooleanField(default=False)

class Magic(Card):
    class CardType(ChoiceEnum):
        NORMAL = "Normal"
        CONTINUOUS = "Continuous"
        EQUIP = "Equip"
        QUICK_PLAY = "Quick-play"
        FIELD = "Field"
        RITUAL = "Ritual"

    card_type = models.CharField(max_length=30, choices=CardType.choices())

class Trap(Card):
    class CardType(ChoiceEnum):
        NORMAL = "Normal"
        CONTINUOUS = "Continuous"
        COUNTER = "Counter"

    card_type = models.CharField(max_length=30, choices=CardType.choices())