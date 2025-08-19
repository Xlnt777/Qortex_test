import pytest
from rest_framework.test import APIClient
from rest_framework import status
from .models import Artist, Album, Song, AlbumSong

#Fixtures
@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def artist():
    return Artist.objects.create(name="Test Artist")

@pytest.fixture
def song():
    return Song.objects.create(title="Test Song")

@pytest.fixture
def album(artist):
    return Album.objects.create(title="Test Album", year=2025, artist=artist)

# ===================== ARTIST =====================
@pytest.mark.django_db
def test_create_artist(api_client):
    data = {'name': 'New Artist'}
    response = api_client.post('/api/v1/artists/', data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Artist.objects.filter(name='New Artist').exists()

@pytest.mark.django_db
def test_get_artist_list(api_client, artist):
    response = api_client.get('/api/v1/artists/')
    assert response.status_code == status.HTTP_200_OK
    assert any(a['id'] == artist.id for a in response.data['results'])

# ===================== SONG =====================
@pytest.mark.django_db
def test_create_song(api_client):
    data = {'title': 'My Song'}
    response = api_client.post('/api/v1/songs/', data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Song.objects.filter(title='My Song').exists()

@pytest.mark.django_db
def test_update_song(api_client, song):
    response = api_client.patch(f'/api/v1/songs/{song.id}/', {'title': 'Updated Song'}, format='json')
    assert response.status_code == status.HTTP_200_OK
    song.refresh_from_db()
    assert song.title == 'Updated Song'

@pytest.mark.django_db
def test_delete_song(api_client, song):
    response = api_client.delete(f'/api/v1/songs/{song.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Song.objects.filter(id=song.id).exists()

# ===================== ALBUM =====================
@pytest.mark.django_db
def test_create_album(api_client, artist):
    data = {'title': 'New Album', 'year': 2023, 'artist': artist.id}
    response = api_client.post('/api/v1/albums/', data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Album.objects.filter(title='New Album').exists()

@pytest.mark.django_db
def test_update_album(api_client, album):
    response = api_client.patch(f'/api/v1/albums/{album.id}/', {'title': 'Updated Album'}, format='json')
    assert response.status_code == status.HTTP_200_OK
    album.refresh_from_db()
    assert album.title == 'Updated Album'

@pytest.mark.django_db
def test_delete_album(api_client, album):
    response = api_client.delete(f'/api/v1/albums/{album.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Album.objects.filter(id=album.id).exists()

# ===================== ADD SONG =====================
@pytest.mark.django_db
def test_add_song_to_album(api_client, album, song):
    url = f'/api/v1/albums/{album.id}/add_song/'
    data = {'song_id': song.id, 'track_number': 1}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert AlbumSong.objects.filter(album=album, song=song).exists()

# ===================== PAGINATION =====================
@pytest.mark.django_db
def test_song_list_pagination(api_client):
    for i in range(20):
        Song.objects.create(title=f'Song {i}')
    response = api_client.get('/api/v1/songs/')
    assert response.status_code == status.HTTP_200_OK
    assert 'results' in response.data
    assert len(response.data['results']) == 15  
    assert response.data['count'] == 20