from rest_framework import serializers
from .models import Word,WordType
from django.contrib.auth.models import User

class WordSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    type = serializers.StringRelatedField(source='type.typename')
    class Meta:
        model = Word
        fields = ('id', 'owner','type', 'content', 'img_url', 'like_count','dislike_count','status')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    words = WordSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url','id', 'username','words')


class WordTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordType
        fields = ('id','typename')