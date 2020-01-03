from rest_framework import serializers
from .models import Monster, Magic, Trap


# ModelForm. Convert and validate to and from JSON
class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = ['pk', 'user', 'name', 'description', 'rarity', 'atk_pts', 'def_pts',
                  'attribute', 'card_type', 'monster_type', 'level', 'effect']
        read_only_fields = ['user']


class MagicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magic
        fields = ['pk', 'user', 'name', 'description', 'rarity', 'card_type']
        read_only_fields = ['user']


class TrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trap
        fields = ['pk', 'user', 'name', 'description', 'rarity', 'card_type']
        read_only_fields = ['user']

def validate_name(self, value):
    class_name = self.__class__
    print(class_name)
    queryset = class_name.objects.filter(title_iexact=value)
    if self.instance:
        queryset = queryset.exclude(pk=self.instance.pk)
    if queryset.exists():
        raise serializers.ValidationError()
    return value