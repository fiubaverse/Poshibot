#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
import ssl
import logging
import decouple

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

botname = "Poshibot"
bot_url = "https://t.me/fiuba_poshibot"

def send_token(receiver_email: str, token: str, sender_email: str = ''):
    try:
        smtp_user = decouple.config('SMTP_USER')
        smtp_password = decouple.config('SMTP_PASSWORD')
        smtp_server = decouple.config('SMTP_SERVER')
        smtp_port = decouple.config('SMTP_PORT')
    except decouple.UndefinedValueError:
        logging.error('SMTP config tokens are not well defined in .env!')
        raise

    # Use default sender email
    if sender_email == '':
        sender_email = smtp_user
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Ingreso a FIUBAVerse"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = f"""\
    Bienvenido a FIUBAVerse, señor cliente.
    Su token es: {token}
    
    Ingréselo en el chat con el bot {botname} para continuar su registración.
    Saludos!"""
    html = f"""\
    <html>
      <body>
        <p> Bienvenido a <b>FIUBAVerse</b>, señor cliente.</p>
        <h1 style='border-style: solid;background-color:DodgerBlue;color:white;'> Su token es: <b>{token}</h1>
        <p>Ingrese el token en el <a href="{bot_url}">chat con {botname}</a>\
           para continuar su registro.
        </p>
        <p>Saludos!</p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, smtp_password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


if __name__ == "__main__":
    import sys

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    logger = logging.getLogger(__name__)
    send(sys.argv[1], sys.argv[2])
