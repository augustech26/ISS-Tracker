import json
import urllib.request

def astronaut_details():
    # Cargar el estado actual de los astronautas en la ISS en tiempo real
    response = urllib.request.urlopen("http://api.open-notify.org/astros.json")
    result = json.loads(response.read())

    # Extraer y mostrar los detalles de los astronautas
    
    print("""
 ______   ______   ______   ________ _______    ______    ______   __    __  ________  _______  
 /      | /      \\ /      \\ /        /       \\  /      \\  /      \\ /  |  /  |/        |/       \\ 
 $$$$$$/ /$$$$$$  /$$$$$$  |$$$$$$$$/$$$$$$$  |/$$$$$$  |/$$$$$$  |$$ | /$$/ $$$$$$$$/ $$$$$$$  |
 $$ |  $$ \\__$$/$$ \\__$$/    $$ |  $$ |__$$ |$$ |__$$ |$$ |  $$/ $$ |/$$/  $$ |__    $$ |__$$ |
 $$ |  $$      \\$$      \\    $$ |  $$    $$< $$    $$ |$$ |      $$  $$<   $$    |   $$    $$< 
 $$ |   $$$$$$  |$$$$$$  |   $$ |  $$$$$$$  |$$$$$$$$ |$$ |   __ $$$$$  \\  $$$$$/    $$$$$$$  |
_$$ |_ /  \\__$$ /  \\__$$ |   $$ |  $$ |  $$ |$$ |  $$ |$$ \\__/  |$$ |$$  \\ $$ |_____ $$ |  $$ |
/ $$   |$$    $$/$$    $$/    $$ |  $$ |  $$ |$$ |  $$ |$$    $$/ $$ | $$  |$$       |$$ |  $$ |
$$$$$$/  $$$$$$/  $$$$$$/     $$/   $$/   $$/ $$/   $$/  $$$$$$/  $$/   $$/ $$$$$$$$/ $$/   $$/ 
                                                                                                                                                                                                                                                                                                 
 """)

    print(f"Actualmente hay {result['number']} astronautas en la ISS: ")
    for p in result["people"]:
        print(p['name'])

    print(f"_______________________ Datos del rastreo _______________________" )
