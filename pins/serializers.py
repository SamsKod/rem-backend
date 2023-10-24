from rest_framework import serializers
from pins.models import Pin
from django.db import IntegrityError


class PinSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')



    class Meta:
        model = Pin
        fields = ['id', 'owner', 'note', 'created_at']


    def create(self, validated_data):
            try:
                return super().create(validated_data)
            except IntegrityError:
                raise serializers.ValidationError({
                    'detail': 'possible duplicate'
                })