import RPi.GPIO as GPIO
from modulos.sala import sensorSala
from modulos.habitacion import sensorHabitacion
from modulos.puerta import sensorPuerta
from modulos.gas import sensorGas
from modulos.incendio import sensorIncendio
from modulos.Gmail import warning 
import time


# Configuración de pines
# sensores = [8, 12, 16, 22, 36]  # Pines GPIO para configurar los sensores: ventana sala, ventana habitación, puerta principal y salida, sensor de gas, incendio 
alarma = 3  # Pin GPIO para configurar alarma como salida
interruptor = 40  # Pin GPIO para el interruptor para encender y apagar el sistema
mess = ""
estado_previo = 0
estado_actual = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Configuración de la biblioteca RPi.GPIO
#GPIO.setup(sensores, GPIO.IN)
GPIO.setup(alarma, GPIO.OUT)
GPIO.setup(interruptor, GPIO.IN)

while True:
    # Leer el estado de la interrupción
    mess = ""
    estado_previo = estado_actual
    
    estado_interruptor = GPIO.input(interruptor)

    if estado_interruptor == GPIO.HIGH:
        estado_actual = 1
        
        #print("Sistema activado")

        s_sala = sensorSala()
        s_habitacion = sensorHabitacion()
        s_puerta = sensorPuerta()
        s_gas  = sensorGas()
        s_incendio = sensorIncendio()

        if s_sala == GPIO.HIGH:
            print ("Sensor sala activado")
            #GPIO.output(alarma, GPIO.HIGH)
            mess = f"{mess} sala,"
            #warning(mess)
            #time.sleep(3)
            #GPIO.output(alarma, GPIO.LOW)

        if s_habitacion == GPIO.HIGH:
            print ("Sensor habitación activado")
            #GPIO.output(alarma, GPIO.HIGH)
            mess = f"{mess} habitación,"
            #warning(mess)
            #time.sleep(3)
            #GPIO.output(alarma, GPIO.LOW)

        if s_puerta == GPIO.HIGH:
            print ("Sensor puerta activado")
            #GPIO.output(alarma, GPIO.HIGH)
            mess = f"{mess} puerta,"
            #warning(mess)
            #time.sleep(3)
            #GPIO.output(alarma, GPIO.LOW) 
        
        if s_gas == GPIO.HIGH:
            print ("Sensor gas activado")
            #GPIO.output(alarma, GPIO.HIGH)
            mess = f"{mess} gas,"
            #warning(mess)
            #time.sleep(3)
            #GPIO.output(alarma, GPIO.LOW) 

        if s_incendio == GPIO.HIGH:
            print ("Sensor incendio activado")
            #GPIO.output(alarma, GPIO.HIGH)
            mess = f"{mess} incendio,"
            #warning(mess)
            #time.sleep(3)
            #GPIO.output(alarma, GPIO.LOW)

        if mess: # Si mess tiene algún mensaje (hay algún sensor activo)
            GPIO.output(alarma, GPIO.HIGH)
            mess = f"Sensor(es) {mess} activado(s) - Alarma"
            warning(mess) 
            time.sleep(3)
            GPIO.output(alarma, GPIO.LOW)
           
            
        else:
            GPIO.output(alarma, GPIO.LOW)

    else:
        #print("Sistema desactivado")
        estado_actual = 0
        mess = ""
        
    if estado_actual != estado_previo:
        if estado_actual == 1:
            print("Sistema activado")
            mess = "Sistema de seguridad activado"
            warning(mess)
        else:
            print("Sistema desactivado")
            mess = "Sistema de seguridad desactivado"
            warning(mess)

    time.sleep(1)