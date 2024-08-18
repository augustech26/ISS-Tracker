from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calcular la distancia en kilómetros entre dos puntos 
    en la tierra (especificados en grados decimales)
    """
    # Convertir grados decimales a radianes
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Fórmula haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radio de la tierra en kilómetros
    return c * r

def calspeed(lon1, lat1, time1, lon2, lat2, time2):
    d = haversine(lon1, lat1, lon2, lat2)
    t = time2 - time1 or 1  # en caso de diferencia de tiempo 0, cambiar a 1 para manejar ZeroDivisionError
    return round((d / t) * 3600, 2)  # devuelve la velocidad en kilómetros por hora redondeada hasta el segundo decimal
