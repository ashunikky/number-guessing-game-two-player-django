from rest_framework import serializers
from . models import player, gamemaster


class playerSerializer(serializers.ModelSerializer):

    class Meta:
        model= player
        fields= '__all__'

class gamemasterSerializer(serializers.ModelSerializer):

    class Meta:
        model= gamemaster
        fields='__all__'