from rest_framework import serializers
from notes.models import Note
from pins.models import Pin


# class NotesSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     is_owner = serializers.SerializerMethodField()
#     profile_id = serializers.ReadOnlyField(source='owner.profile.id')
#     profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    

#     def get_is_owner(self, obj):
#         request = self.context['request']
#         return request.user == obj.owner

#     class Meta:
#         model = Note
#         fields = [
#             'id', 'owner', 'is_owner', 'profile_id',
#             'profile_image', 'created_at', 'updated_at',
#             'title', 'content', 'code'
#         ]


class NotesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    pin_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    pins_count = serializers.ReadOnlyField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    def get_pin_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            pin = Pin.objects.filter(
                owner=user, note=obj
            ).first()
            return pin.id if pin else None
        return None

    class Meta:
        model = Note
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'code', 'pin_id', 'comments_count','pins_count',
        ]