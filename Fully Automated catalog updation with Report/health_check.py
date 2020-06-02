#!/usr/bin/env python3

import shutil
import psutil
from report_email import send_mail
import socket

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20    # return True if more than 20% is available

def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 90   # return True if usage is less than 80%

def check_memory():
    """ Checks if system memory is notused more than 80%"""
    mem = psutil.virtual_memory()
    free = mem.free / 1024**2
    return free > 500

def check_localhost():
    ip = socket.gethostbyname("localhost")
    if ip != '127.0.0.1':
        return False
    else: True


def main():
    # If there's not enough disk, or not enough CPU, print an error
    if not check_cpu_usage():
        subject = "Error - CPU usage is over 80%"
        body = "CPU usage is over 80%"
        send_mail(subject, body)

    if not check_disk_usage('/'):
        subject = "Error - Available disk space is less than 20%"
        body = "Available disk space is lower than 20%"
        send_mail(subject, body)
    
    if not check_memory():
        subject = "Error - Available memory is less than 500MB"
        body = "Available memory is less than 500MB"
        send_mail(subject, body)

    if check_localhost():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        body = "hostname 'localhost' cannot be resolved to '127.0.0.1'"
        send_mail(subject, body)

if __name__ == "__main__":
    main()