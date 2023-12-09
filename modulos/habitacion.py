import RPi.GPIO as GPIO
import time

# Configuración de pines
habitacion = 12  # Pin GPIO para configurar el sensor habitacion 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Configuración de la biblioteca RPi.GPIO
GPIO.setup(habitacion, GPIO.IN)

def sensorHabitacion():
    estado_sensor = GPIO.input(habitacion)
    return estado_sensor
