import RPi.GPIO as GPIO
import time

# Configuración de pines
gas = 22  # Pin GPIO para configurar el sensor habitacion 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Configuración de la biblioteca RPi.GPIO
GPIO.setup(gas, GPIO.IN)

def sensorGas():
    estado_sensor_gas = GPIO.input(gas)
    return estado_sensor_gas