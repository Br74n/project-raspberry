import RPi.GPIO as GPIO
import time

# Configuración de pines
incendio = 36  # Pin GPIO para configurar el sensor habitacion 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Configuración de la biblioteca RPi.GPIO
GPIO.setup(incendio, GPIO.IN)

def sensorIncendio():
    estado_sensor_incendio = GPIO.input(incendio)
    return estado_sensor_incendio