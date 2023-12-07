import RPi.GPIO as GPIO
import time

# Configuración de pines
puerta = 16  # Pin GPIO para configurar el sensor puerta sala 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Configuración de la biblioteca RPi.GPIO
GPIO.setup(puerta, GPIO.IN)

def sensorPuerta():
    estado_sensor = GPIO.input(puerta)
    return estado_sensor