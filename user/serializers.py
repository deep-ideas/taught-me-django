from rest_framework import serializers
from rest_framework.validators import UniqueValidator,UniqueTogetherValidator
from django.contrib.auth.models import User


from .models import Country , Profile




class UserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    # username = serializers.CharField(
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    # password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        validator=[UniqueTogetherValidator(
            queryset=User.objects.all(),
            fields=("email","username","password")
        )]
        model = User
        fields = ('id','first_name','last_name','username', 'email',)

    def save(self):
        user = User.objects.create_user(
            self.validated_data['username'],
            self.validated_data['email'],
            self.validated_data['password']
        )
        return user


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name","flag")

class UserSerializerSimple(UserSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class UserSerializerName(UserSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name',)

class ProfileSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Profile.objects.all())]
    )
    class Meta:
        model = Profile
        fields=('phone_number','country') 

        

    


