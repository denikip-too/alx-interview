#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys
import requests
import signal


def signal_handler(sig, frame):
    """for ctrl+c"""
    signal.signal(signal.SIGINT, original_sigint)
    sys.exit(1)

def log_stats():
    """print these statistics from the beginning
    After every 10 lines and/or a keyboard interruption (CTRL + C)"""
    for line in sys.stdin:
        print(line)
        line.rstrip()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigint_handler)
    log_stats()
