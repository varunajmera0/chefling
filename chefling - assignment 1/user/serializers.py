from rest_framework import serializers
from rest_framework import exceptions
from django.contrib.auth import authenticate
from user.models import User

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'],
                                        validated_data['name'],
                                        validated_data['password'])
        return user


class UserSigninSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email", "")
        password = data.get("password", "")

        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                data["user"] = user
            else:
                msg = "User is deactivated."
                raise exceptions.ValidationError(msg)
        else:
            email_exist = User.objects.filter(email=email)
            if not email_exist:
                msg = {"err":"You don’t seem to have an account with us!"}
                raise exceptions.ValidationError(msg)
            else :
                msg = {"err":"The password you have provided does not match with our records"}
                raise exceptions.ValidationError(msg)

        return User.objects.get(email=email)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileUpdateSerializer(serializers.Serializer):
    name      = serializers.CharField()
    password = serializers.CharField(required=True)
