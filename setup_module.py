import turtle

def setup():
    turtle.title('ISS Tracker')

    # Configuración del mapa mundial
    screen = turtle.Screen()
    screen.setup(1189, 848)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic("assets/map.gif")

    # Configuración del objeto ISS
    screen.register_shape("assets/iss.gif")
    iss = turtle.Turtle()
    iss.shape("assets/iss.gif")
    iss.penup()

    return iss
