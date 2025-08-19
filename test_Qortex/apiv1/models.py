from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    artist = models.ForeignKey(Artist, verbose_name='Артист', on_delete=models.CASCADE)
    songs = models.ManyToManyField("Song", through='AlbumSong')

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"

    def __str__(self):
        return self.title

class AlbumSong(models.Model):
    album = models.ForeignKey(Album,verbose_name='Альбом', on_delete=models.CASCADE)
    song = models.ForeignKey(Song, verbose_name='Песня', on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField(verbose_name="Порядковый номер")

    class Meta:
        unique_together = ('album', 'track_number')
        verbose_name = "Песня в альбоме"
        verbose_name_plural = "Песни в альбоме"

    def __str__(self):
        return f"{self.album.title} — {self.song.title} (трек {self.track_number})"