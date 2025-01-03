import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings
#from PronosticadorFutbol import settings


def send_email(email, subject, message):

    # credenciales
    user = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD
    
    sender_email = "estratebet@estratebet.com"  # email del remitente
    # configuracion del servidor
    msg = MIMEMultipart()

    smtp_server = settings.EMAIL_HOST
    smtp_port = settings.EMAIL_PORT
    
    
    # parametros del mensaje
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject

    
    msg.attach(MIMEText(message,'plain'))

    # Conexión al servidor
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)   # configuracion servidor
        server.starttls()   # inicializamos el servidor
        server.login(user,password) # nos logueamos
        try:
            server.sendmail(sender_email, email, msg.as_string())   # envio de correo
            server.quit()   # cerramos la conexion con el servidor
            return True
        except Exception as e:
            server.quit()   # cerramos la conexion con el servidor
            print(e)
            print("Error al enviar el correo")
            return False
    except smtplib.SMTPException as e:
        print("Error al conectar con el servidor")
        print(e)
        return False
    


