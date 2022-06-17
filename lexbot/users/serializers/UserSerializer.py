# django
from django.contrib.auth import get_user_model, password_validation
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from lexbot.tasks.tasks import send_confirmation_email
from lexbot.users.models import Profile
from lexbot.users.serializers import ProfileModelSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class UserModelSerializer(serializers.ModelSerializer):

    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'profile',
        )


class UserRegisterSerializer(serializers.Serializer):
    """
    User register serializer
    """

    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    password = serializers.CharField(min_length=8, max_length=64)
    password2 = serializers.CharField(min_length=8, max_length=64)

    first_name = serializers.CharField(min_length=2, max_length=60)
    last_name = serializers.CharField(min_length=2, max_length=60)

    def validate(self, data):

        password = data['password']
        password2 = data['password2']

        if password != password2:
            raise serializers.ValidationError("Password don't match")

        password_validation.validate_password(password)
        return data

    def create(self, data):

        data.pop('password2')

        data = {
            **data,
            "username": data['email'],
        }

        user = User.objects.create_user(**data)
        Profile.objects.create(user=user)

        send_confirmation_email.delay(user_pk=user.pk)

        return user


class UserProfileUpdateSerializer(serializers.ModelSerializer):

    profile = ProfileModelSerializer()
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'profile'
        )

    def update(self, instance, validated_data):
        
        profile_data = validated_data.pop('profile')
        profile = instance.profile 
        
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        
        profile.rut = profile_data.get('rut', profile.rut)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.save()
        
        return instance
    
    
