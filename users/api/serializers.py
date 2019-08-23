from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import Person

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('id', 'email', 'username', 'name', 'ramal', 'is_administrator', 'is_participant')

class CustomRegisterSerializer(RegisterSerializer):

    name = serializers.CharField(max_length=40)
    ramal = serializers.CharField(max_length=6)
    is_administrator = serializers.BooleanField()
    is_participant = serializers.BooleanField()

    class Meta:
        model = Person
        fields = ('email', 'username', 'name', 'ramal', 'password', 'is_administrator', 'is_participant')

    def get_cleaned_data(self):

        return {
            'username': self.validated_data.get('username', ''),
            'name': self.validated_data.get('name',''),
            'ramal': self.validated_data.get('ramal', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'is_administrator': self.validated_data.get('is_administrator', ''),
            'is_participant': self.validated_data.get('is_participant', '')
        }

    def save(self, request):

        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_administrator = self.cleaned_data.get('is_administrator')
        user.is_participant = self.cleaned_data.get('is_participant')
        user.name = self.cleaned_data.get('name')
        user.ramal = self.cleaned_data.get('ramal')
        user.save()
        adapter.save_user(request, user, self)

        return user

class TokenSerializer(serializers.ModelSerializer):

    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user', 'user_type')

    def get_user_type(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        is_administrator = serializer_data.get('is_administrator')
        is_participant = serializer_data.get('is_participant')
        return {
            'is_administrator': is_administrator,
            'is_participant': is_participant
        }