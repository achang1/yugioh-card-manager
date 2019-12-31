from rest_framework import serializers
from .models import Monster, Magic, Trap


# ModelForm. Convert and validate to and from JSON
class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = ['pk', 'name', 'description', 'rarity', 'atk_pts', 'def_pts',
                  'attribute', 'card_type', 'monster_type', 'level', 'effect']
        read_only_fields = ['user']


class MagicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magic
        fields = ['pk', 'name', 'description', 'rarity', 'card_type']
        read_only_fields = ['user']


class TrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trap
        fields = ['pk', 'name', 'description', 'rarity', 'card_type']
        read_only_fields = ['user']