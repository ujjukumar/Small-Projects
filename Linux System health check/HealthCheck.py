#!/usr/bin/env python3

import shutil
import psutil

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20    # return True if more than 20% is available
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75   # return True if usage is less than 75%

def main():
    # If there's not enough disk, or not enough CPU, print an error
    if check_disk_usage('/') and check_cpu_usage():
        print("Everything ok!")
    else:
        print("ERROR")


if __name__ == "__main__":
    main()