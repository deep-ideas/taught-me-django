from rest_framework import serializers
from rest_framework.validators import UniqueValidator,UniqueTogetherValidator
from rest_framework_recursive.fields import RecursiveField
from django.contrib.auth.models import User


from .models import Country , Profile




class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        validator=[UniqueTogetherValidator(
            queryset=User.objects.all(),
            fields=("email","username","password")
        )]
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username', 
            'email',
            'password',
        )

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

class UserSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email')

    def __str__(self):
        return self.username

class UserSerializerName(UserSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name',)

class ProfileSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Profile.objects.all())]
    )
    user = RecursiveField('user.serializers.UserSerializer',read_only=True)
    country_id = serializers.IntegerField(write_only=True)

    user_by = serializers.IntegerField(write_only=True)

    class Meta:
        model = Profile
        fields=(
            'phone_number',
            'country',
            'user',
            'date_of_birth',
            'gender',
            'address_line',
            'city',
            'region',
            'postal_code',

            'user_by',
            'country_id',
        ) 
        depth = 1
    def create(self, validated_data):
        profile = Profile(**validated_data)

        country_id = validated_data.get('country_id')
        validated_data.pop('country_id',None)

        countryId = Country.objects.get(id=country_id)
        profile.country = countryId
        profile.save()
        return profile
        

    


