from .models import Member
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('email', 'password')
        extra_kwargs = {
            'email' : {'allow_null': False, 'required': True},
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user
