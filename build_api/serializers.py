from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Cake,AddCaketoCart,Checkout

# this is registration serializers
class RegsiterSerializers(serializers.ModelSerializer):

    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(min_length=8)


    def create(self, validate_data):
        user = User.objects.create_user(validate_data['username'],validate_data['email'], validate_data['password'])
        return user


    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']


# this is add cake serializers
class AddcakeSerilaizer(serializers.ModelSerializer):

    class Meta:

        model=Cake
        fields="__all__"




# this is cart serializers
class CartSerializer(serializers.ModelSerializer):

    class Meta:

        model=AddCaketoCart
        fields="__all__"


class CheckoutSerializer(serializers.ModelSerializer):

    class Meta:
        model= Checkout
        fields="__all__"



class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)