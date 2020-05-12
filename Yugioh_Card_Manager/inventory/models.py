from django.db import models
from enum import Enum
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    rarity = models.CharField(max_length=30, choices=CardRarity.choices())
    copies = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])

    class Meta:
        abstract = True
        unique_together = (('name', 'user'),)

    def __str__(self):
        return self.name

    @property
    def owner(self):
        return self.user


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
    
    class MonsterType(ChoiceEnum):
        AQUA = "Aqua"
        BEAST = "Beast"
        BEAST_WARRIOR = "Beast-Warrior"
        DINOSAUR = "Dinosaur"
        DRAGON = "Dragon"
        FAIRY = "Fairy"
        FIEND = "Fiend"
        FISH = "Fish"
        INSECT = "Insect"
        MACHINE = "Machine"
        PLANT = "Plant"
        PSYCHIC = "Psychic"
        PYRO = "Pyro"
        REPTILE = "Reptile"
        ROCK = "Rock"
        SEA_SERPENT = "Sea Serpent"
        SPELLCASTER = "Spellcaster"
        THUNDER = "Thunder"
        WARRIOR = "Warrior"
        WINGED_BEAST = "Winged Beast"
        WYRM = "Wyrm"
        ZOMBIE = "Zombie"

    atk_pts = models.IntegerField(default=0)
    def_pts = models.IntegerField(default=0)
    attribute = models.CharField(max_length=30, choices=CardAttribute.choices())
    card_type = models.CharField(max_length=30, choices=CardType.choices())
    monster_type = models.CharField(max_length=30, choices=MonsterType.choices())
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