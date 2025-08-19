from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Artist, Album, Song, AlbumSong
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, AlbumSongSerializer,AlbumAddSongSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('id')
    serializer_class = AlbumSerializer

    @action(detail=True, methods=['post'], serializer_class=AlbumAddSongSerializer)
    def add_song(self, request, pk=None):
        album = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        song_id = serializer.validated_data['song_id']
        track_number = serializer.validated_data['track_number']

        # Проверка существования песни
        try:
            song = Song.objects.get(pk=song_id)
        except Song.DoesNotExist:
            return Response({"error": "Песня с таким ID не найдена"}, status=404)

        # Проверка уникальности track_number
        if AlbumSong.objects.filter(album=album, track_number=track_number).exists():
            return Response(
                {"error": f"Трек {track_number} уже есть в альбоме"}, status=400
            )

        album_song = AlbumSong.objects.create(album=album, song=song, track_number=track_number)
        return Response({"id": album_song.id, "song": song.title, "track_number": track_number}, status=status.HTTP_201_CREATED)

