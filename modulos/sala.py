import RPi.GPIO as GPIO
import time

# Configuración de pines
sala = 8  # Pin GPIO para configurar el sensor ventana sala 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Configuración de la biblioteca RPi.GPIO
GPIO.setup(sala, GPIO.IN)

def sensorSala():
    estado_sensor = GPIO.input(sala)
    return estado_sensor