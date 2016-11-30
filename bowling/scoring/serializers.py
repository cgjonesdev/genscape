from rest_framework import serializers
from models import Player


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'
        read_only_fields = (
            'strike_frame',
            'strike_reserve',
            'spare_frame',
            'spare_reserve')


    def create(self, validated_data):
        return Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name', instance.name)
        instance.current_frame = validated_data.get(
            'current_frame', instance.current_frame)
        instance.first_roll = validated_data.get(
            'first_roll', instance.first_roll)
        instance.second_roll = validated_data.get(
            'second_roll', instance.second_roll)
        instance.score = validated_data.get(
            'score', instance.score)
        instance.save()
        return instance
