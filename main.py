import time as time_module
from setup_module import setup
from astronaut_module import astronaut_details
from coordinates_module import get_coordinates, getloc
from calculation_module import calspeed

def main(trail=True):
    iss = setup()
    astronaut_details()

    prevlon, prevlan, prevtime = get_coordinates()  # inicializar valores de referencia

    while True:
        lon, lat, time = get_coordinates()
        speed = calspeed(prevlon, prevlan, prevtime, lon, lat, time)

        # Actualizar la ubicación de la ISS en el mapa
        iss.goto(lon, lat)

        if trail:
            iss.dot(size=2)  # Ploteo de puntos de rastreo

        # Mostrar velocidad y país en la terminal
        print(f'Velocidad: {speed} km/h')
        print(f'Sobre {getloc(lon, lat)}')

        prevlon, prevlan, prevtime = lon, lat, time  # actualizar valores de referencia
        time_module.sleep(5)  # Refrescar cada 5 segundos

if __name__ == '__main__':
    main(trail=False)
