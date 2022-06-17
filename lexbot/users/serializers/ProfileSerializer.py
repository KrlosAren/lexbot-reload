"""Profile serializer"""


from rest_framework import serializers

from lexbot.users.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:

        model = Profile
        fields = (
            'rut',
            'phone',
        )
