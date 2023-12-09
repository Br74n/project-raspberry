from email.message import EmailMessage
import smtplib
from datetime import datetime

lcFecha = datetime.now().strftime('%Y-%m-%d') 
lcNombreArchivo = "/var/www/html/Fecha"+lcFecha+".csv"
lcNombreSolo = "Fecha"+lcFecha+".csv"

remitente = "saw79989@gmail.com"
destinatarios = ["milton.millan@correounivalle.edu.co", "hernandez.bryan@correounivalle.edu.co", "emmanuel.caipe@correounivalle.edu.co"]

mensaje = "Sensor activado"

def warning(mess):
    for destinatario in destinatarios:
        mensaje = mess
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = "Alarma Raspberry:"
        email.set_content(mensaje)
        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.login(remitente, "pexb kpdq wnbu rayr")

        smtp.sendmail(remitente, destinatario, email.as_string())

        smtp.quit()
