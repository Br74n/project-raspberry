from email.message import EmailMessage
import smtplib
from datetime import datetime

lcFecha = datetime.now().strftime('%Y-%m-%d') 
lcNombreArchivo = "/var/www/html/Fecha"+lcFecha+".csv"
lcNombreSolo = "Fecha"+lcFecha+".csv"

remitente = "saw79989@gmail.com"
destinatario = ["milton.millan@correounivalle.edu.co", "hernandez.bryan@correounivalle.edu.co", "emmanuel.caipe@correounivalle.edu.co"]

mensaje = "Sensor activado"

def warning():
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Alerta MEB: " + lcNombreSolo
    email.set_content(mensaje)
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(remitente, "vqdy orha usbs ckcy")
    smtp.quit()
    
"""
with open(lcNombreArchivo, "rb") as f:
 email.add_attachment(
  f.read(),
  filename=lcNombreSolo,
  maintype="application",
  subtype="csv"
 )



smtp.sendmail(remitente, destinatario, email.as_string())
"""
