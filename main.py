import RPi.GPIO as GPIO
from Modulos.sala import sensorSala
from Modulos.habitacion import sensorHabitacion
from Modulos.puerta import sensorPuerta
from Modulos.gas import sensorGas
from Modulos.Incendio import sensorIncendio
import time


# Configuración de pines
# sensores = [8, 12, 16, 22, 36]  # Pines GPIO para configurar los sensores: ventana sala, ventana habitación, puerta principal y salida, sensor de gas, incendio 
alarma = 3  # Pin GPIO para configurar alarma como salida
interruptor = 40  # Pin GPIO para el interruptor para encender y apagar el sistema

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Configuración de la biblioteca RPi.GPIO
#GPIO.setup(sensores, GPIO.IN)
GPIO.setup(alarma, GPIO.OUT)
GPIO.setup(interruptor, GPIO.IN)

while True:
    # Leer el estado de la interrupción
    estado_interruptor = GPIO.INPUT(interruptor)

    if estado_interruptor == GPIO.HIGH:
        print("Sistema activado")

        s_sala = sensorSala()
        s_habitacion = sensorHabitacion()
        s_puerta = sensorPuerta()
        s_gas  = sensorGas()
        s_incendio = sensorIncendio()

        if s_sala == GPIO.HIGH:
            GPIO.output(alarma, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(alarma, GPIO.HIGH)

        if s_habitacion == GPIO.HIGH:
            GPIO.output(alarma, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(alarma, GPIO.HIGH)

        if s_puerta == GPIO.HIGH:
            GPIO.output(alarma, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(alarma, GPIO.HIGH) 
        
        if s_gas == GPIO.HIGH:
            GPIO.output(alarma, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(alarma, GPIO.HIGH) 

        if s_incendio == GPIO.HIGH:
            GPIO.output(alarma, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(alarma, GPIO.HIGH) 
            
        else:
            GPIO.output(alarma, GPIO.LOW)

    else:
        print("Sistema desactivado")

    time.sleep(1)