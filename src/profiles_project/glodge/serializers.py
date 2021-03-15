from rest_framework import serializers

from . import models

class LodgeDetailSerializer(serializers.ModelSerializer):
    """A serializer for the Lodge Detail"""

    class Meta:
        model = models.LodgeDetail
        fields = ('id', 'lodge_name', 'lodge_address', 'lodge_phone')

    def create(self, validated_data):
        """Create and return a new user."""

        lodge = models.LodgeDetail(
            lodge_name=validated_data['lodge_name'],
            lodge_address=validated_data['lodge_address'],
            lodge_phone=validated_data['lodge_phone']
        )

        lodge.save()

        return lodge


class RoomDetailSerializer(serializers.ModelSerializer):
    """A serializer for the Room of a Lodge"""

    class Meta:
        model = models.RoomDetail
        filelds = ('id', 'lodge_detail', 'room_no', 'room_type', 'created_on')