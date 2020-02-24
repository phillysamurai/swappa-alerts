#!/usr/bin/python3.7

import os, imaplib, email, subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mail_server(email, sms_gateway, text):
    email = os.environ["EMAIL"]
    pas = os.environ["PASS"]
    smtp = os.environ["SMTP"]
    port = int(os.environ['PORT'])
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, pas)
    server.sendmail(email, sms_gateway, text)
    server.quit()


def send_text(text):
    msg = MIMEMultipart()
    email = os.environ["EMAIL"]
    sms_gateway = os.environ["SMS_GATEWAY"]
    msg['From'] = email
    msg['To'] = sms_gateway
    msg['Subject'] = "SWAPPA PRICE ALERT\n"
    body = text
    msg.attach(MIMEText(body, 'plain'))
    sms = msg.as_string()
    mail_server(email, sms_gateway, sms)


def notify():
    imap_host = os.environ['IMAP_HOST']
    imap_user = os.environ["EMAIL"]
    imap_pass = os.environ["PASS"]
    imap = imaplib.IMAP4_SSL(imap_host)
    imap.login(imap_user, imap_pass)
    imap.select('Inbox')
    result, data = imap.uid('search', None, "ALL")
    inbox_item = data[0].split()
    most_recent = inbox_item[-1]
    result2, email_data = imap.uid('fetch', most_recent, '(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    b = email.message_from_string(raw_email)
    if b['From'] == os.environ["SMS_GATEWAY"]:
        subprocess.Popen(['notify-send', 'You Recieved a message from: ' + b['From']])
    else:
        subprocess.Popen(['notify-send', 'Sorry No Message'])
