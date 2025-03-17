import requests

def escanear_url(url_objetivo, palabra):
    url_completa = f"{url_objetivo.rstrip('/')}/{palabra}"
    try:
        respuesta = requests.get(url_completa, timeout=5)
        if respuesta.status_code == 200:
            print(f"Encontrado: {url_completa} (Código {respuesta.status_code})")
        elif respuesta.status_code == 403:
            print(f"Acceso denegado: {url_completa} (Código {respuesta.status_code})")
        elif respuesta.status_code == 404:
            print(f"No encontrado: {url_completa} (Código {respuesta.status_code})")
        else:
            print(f"Estado desconocido: {url_completa} (Código {respuesta.status_code})")
    except requests.exceptions.RequestException as error:
        print(f"Error al conectar con {url_completa}: {error}")

def leer_palabras(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return [linea.strip() for linea in f]
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return []

url_objetivo = "http://127.0.0.1:8000"
archivo_palabras = "wordlist.txt"

palabras = leer_palabras(archivo_palabras)

for palabra in palabras:
    escanear_url(url_objetivo, palabra)

