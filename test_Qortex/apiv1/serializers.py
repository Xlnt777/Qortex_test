from rest_framework import serializers
from .models import Artist, Album, Song, AlbumSong

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title"]

class AlbumSongSerializer(serializers.ModelSerializer):
    song = SongSerializer()

    class Meta:
        model = AlbumSong
        fields = ["song", "track_number"]



class AlbumSerializer(serializers.ModelSerializer):
    songs = AlbumSongSerializer(source="albumsong_set", many=True, read_only=True)
   
    class Meta:
        model = Album
        fields = ["id", "title", "year", "artist", "songs"]


class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(source="album_set", many=True, read_only=True)
    

    class Meta:
        model = Artist
        fields = ["id", "name", "albums"]


class AlbumAddSongSerializer(serializers.Serializer):
    song_id = serializers.IntegerField()
    track_number = serializers.IntegerField()