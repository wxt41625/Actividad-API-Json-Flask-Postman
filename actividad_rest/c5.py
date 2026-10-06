import requests

# 1. Definimos la función que consulta el clima (la que ya tenías)
def obtener_clima(latitud, longitud):
    """
    Consulta la API de Open-Meteo y regresa un diccionario
    con la temperatura y la velocidad del viento actuales.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    
    # Usamos un diccionario para los parámetros de consulta.
    # requests se encarga de armar la URL correctamente.
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,wind_speed_10m",
    }
    
    # Hacemos la petición GET con un timeout de 10 segundos.
    r = requests.get(url, params=parametros, timeout=10)
    
    # Si la petición falla (por ejemplo, un error 404 o 500), esto lanza una excepción.
    r.raise_for_status()
    
    # Extraemos solo la parte "current" de la respuesta JSON.
    return r.json()["current"]


# 2. Definimos las ciudades con sus coordenadas.
#    (Usé latitud y longitud aproximadas).
ciudades = [
    {"nombre": "Querétaro", "lat": 20.59, "lon": -100.39},
    {"nombre": "CDMX", "lat": 19.43, "lon": -99.13},
    {"nombre": "Monterrey", "lat": 25.68, "lon": -100.31},
]

# 3. Preparamos la tabla para imprimir en consola.
#    Los "<" y ">" sirven para alinear el texto a la izquierda o derecha.
#    El número después de ":" es el ancho de columna.
print(f"{'Ciudad':<12} | {'Temp (°C)':>10} | {'Viento (km/h)':>14}")
print("-" * 42)  # Línea separadora

# 4. Recorremos la lista de ciudades.
for ciudad in ciudades:
    # Llamamos a nuestra función.
    datos_clima = obtener_clima(ciudad["lat"], ciudad["lon"])
    
    # Extraemos los valores que nos interesan.
    temperatura = datos_clima["temperature_2m"]
    viento = datos_clima["wind_speed_10m"]
    
    # Imprimimos la fila de la tabla con formato.
    # El ":>10.1f" significa: alinea a la derecha, 10 de ancho, con 1 decimal.
    print(f"{ciudad['nombre']:<12} | {temperatura:>10.1f} | {viento:>14.1f}")

print("-" * 42)


print("Irvin Misael")
