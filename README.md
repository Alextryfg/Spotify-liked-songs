# Spotify-liked-songs

Este proyecto permite transferir las canciones de una playlist a tu lista de canciones que te gustan en Spotify. Esto puede ser útil si cambias de cuenta, ya que Spotify no ofrece una opción para trasladar las canciones guardadas en orden de una cuenta a otra.

## Requisitos

Para utilizar esta herramienta, es necesario crear una aplicación en Spotify y obtener las credenciales de acceso.

### Pasos para crear una aplicación en Spotify:
1. Accede a [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Inicia sesión con tu cuenta de Spotify.
3. Haz clic en "Create an App".
4. Proporciona un nombre y descripción para la aplicación.
5. Una vez creada, ve a la sección "Settings" y copia el `Client ID` y `Client Secret`.
6. Agrega `http://localhost:8888/callback` como Redirect URI en la configuración de la app.

Estas credenciales serán necesarias para autenticarte y gestionar las canciones desde la aplicación.

## Instalación

Clona el repositorio y asegúrate de tener instalado Python y las dependencias necesarias:

```sh
pip install spotipy
```

## Uso

Ejecuta el script proporcionando las credenciales obtenidas:

```sh
python main.py
```

## Notas
- Asegúrate de que tu cuenta de Spotify tiene acceso a la API de Spotify.
- Este script solo funciona con cuentas premium en algunos casos debido a restricciones de la API de Spotify.

## Licencia
Este proyecto está bajo la licencia MIT.

