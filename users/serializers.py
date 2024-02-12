import random
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        new_code = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            code=new_code,
            password=validated_data['password'],
        )
        user.save()
        return user


class UserActivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'code',)

