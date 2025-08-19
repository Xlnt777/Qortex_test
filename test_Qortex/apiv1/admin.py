from django.contrib import admin
from .models import Artist, Album, Song, AlbumSong

class AlbumSongInline(admin.StackedInline):
    model = AlbumSong
    extra = 0

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [AlbumSongInline]
    list_display = ("title", "artist", "year")


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(AlbumSong)
class AlbumSongAdmin(admin.ModelAdmin):
    list_display = ("album", "song", "track_number")