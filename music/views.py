from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Music
from .serializers import MusicSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, pk):
        music = get_object_or_404(Music, pk=pk) 
        if request.method == 'GET':
            music = get_object_or_404(Music, pk=pk)
            serializer = MusicSerializer(music)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = MusicSerializer(music, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'DELETE':
            music.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PATCH'])
def like_song(request, pk):
        song = get_object_or_404(Music, pk=pk)
        if request.method == 'PATCH':
            new_likes = song.likes + 1  
            serializer = MusicSerializer(song, {'likes':new_likes}, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)