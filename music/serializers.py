from turtle import title
from  rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist', 'album','genre' ]
        # Add release_date when fixed