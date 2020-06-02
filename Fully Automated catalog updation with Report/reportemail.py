#! /usr/bin/env python3

import emails
import os

def send_mail(subject, body, attachment=None):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)

if __name__ == '__main__':
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"
    send_mail(subject, body)