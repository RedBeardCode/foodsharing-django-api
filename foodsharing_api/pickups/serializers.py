"""Serializer for pickup app"""
from rest_framework import serializers
from rest_framework.fields import BooleanField

from foodsharing_api.stores.serializers import StoreSerializer
from foodsharing_api.users.serializers import UserSerializer

from foodsharing_api.pickups.models import TakenPickup as TakenPickupModel
from foodsharing_api.users.models import User as UserModel


class TakenPickupSerializer(serializers.ModelSerializer):
    """Taken pickup serializer"""
    user = UserSerializer()
    store = StoreSerializer()

    class Meta:
        model = TakenPickupModel
        fields = ['user', 'store', 'at', 'confirmed']

class PickupMemberSerializer(serializers.ModelSerializer):
    """Pickup member serializer"""
    confirmed = BooleanField()

    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'confirmed', 'phone', 'mobile', 'photo']


class PickupSerializer(serializers.ModelSerializer):
    """Pickup serializer"""
    members = PickupMemberSerializer(many=True)
    store = StoreSerializer()

    class Meta:
        model = TakenPickupModel
        fields = ['members', 'store', 'at']
