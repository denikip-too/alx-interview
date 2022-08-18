#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys
import requests


def log_stats():
    """print these statistics from the beginning
    After every 10 lines and/or a keyboard interruption (CTRL + C)""" 
