 obtener_clima(latitud, longitud):
 url = "https://api.open-meteo.com/v1/forecast"
 parametros = {
 "latitude": latitud,
 "longitude": longitud,
 "current": "temperature_2m,wind_speed_10m",
 }
 r = requests.get(url, params=parametros, timeout=10)
 r.raise_for_status()
 return r.json()["current"]

