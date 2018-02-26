"""Serializer for the session app"""
from django.contrib.auth import authenticate, login
from rest_framework import serializers


class AuthLoginSerializer(serializers.Serializer):
    """Serializer to login and create a session"""
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """Validating the user credentials"""
        credentials = {
            'email': attrs.get('email'),
            'password': attrs.get('password')
        }
        user = authenticate(**credentials)
        if user:
            if not user.is_active:
                msg = 'User account is disabled'
                raise serializers.ValidationError(msg)
            login(self.context['request'], user)
        else:
            msg = 'Unable to login with provided credentials.'
            raise serializers.ValidationError(msg)

        return user
