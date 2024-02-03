import smtplib
import psutil
from email.mime.text import MIMEText

sender_email = 'sotoj9268@gmail.com'
sender_password = 'rtyy zagf taco klxq'
receiver_email = 'sotoj9268@gmail.com'
subject = 'Alerta de rendimiento del CPU'

def enviar_correo(mensaje):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    msg = MIMEText(mensaje)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server.sendmail(sender_email, receiver_email, msg.as_string())

    server.quit()

def enviar_correo(mensaje):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    msg = MIMEText(mensaje)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server.sendmail(sender_email, receiver_email, msg.as_string())

    server.quit()

def monitorear_rendimiento():
    cpu_percent = psutil.cpu_percent(interval=1)

    if cpu_percent > 40:
        mensaje = f'Alerta: El rendimiento del CPU ha superado el 40%. Actual: {cpu_percent}%'
        enviar_correo(mensaje)

if __name__ == "__main__":
    while True:
        monitorear_rendimiento()