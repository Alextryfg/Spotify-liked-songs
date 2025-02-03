import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time  # Para hacer pausas entre las solicitudes

# Configuración de la API de Spotify
SPOTIPY_CLIENT_ID = 'xxxxxxxxxxxxxxxxx'  # Tu Client ID
SPOTIPY_CLIENT_SECRET = 'xxxxxxxxxxxxxxxxx'  # Tu Client Secret
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'  # URI de redirección

# Autenticación con permisos necesarios
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="user-library-modify,playlist-read-private"
))

# ID de la playlist
playlist_id = 'xxxxxxxxxxxxxxxxx'

# Función para obtener todas las canciones de una playlist
def obtener_canciones_playlist(playlist_id):
    canciones = []
    offset = 0
    while True:
        # Obtener canciones en bloques de 100
        resultados = sp.playlist_items(
            playlist_id,
            offset=offset,
            fields="items(track(id)),next",
            additional_types=['track']
        )
        # Agregar los IDs de las canciones
        canciones.extend([item['track']['id'] for item in resultados['items'] if item['track']])
        if resultados['next'] is None:
            break
        offset += len(resultados['items'])
    return canciones

# Obtener las canciones de la playlist
tracks = obtener_canciones_playlist(playlist_id)

# Asegurarnos de que la lista de canciones esté en el orden correcto
# Se debe invertir el orden original para agregar la última canción de la playlist primero
tracks.reverse()

# Añadir canciones a "Me Gusta" en orden inverso
total_canciones = len(tracks)
for idx in range(total_canciones):  # Ahora itera desde la primera canción hacia la última (ya invertidas)
    track_id = tracks[idx]
    sp.current_user_saved_tracks_add([track_id])
    
    # Aviso cada 50 canciones añadidas
    if (idx + 1) % 50 == 0:
        print(f"Se han añadido {idx + 1} canciones de un total de {total_canciones}.")

    # Pausa cada 300 canciones añadidas para evitar sobrecarga
    if (idx + 1) % 300 == 0:
        print("Pausando por 1 segundo para evitar límites de tasa.")
        time.sleep(1)
    else:
        # Pausa de 0.1 segundos entre cada solicitud para evitar el límite de tasa
        time.sleep(0.1)

print(f"¡Todas las canciones han sido añadidas a 'Me Gusta' en el orden deseado! Total: {total_canciones} canciones.")
