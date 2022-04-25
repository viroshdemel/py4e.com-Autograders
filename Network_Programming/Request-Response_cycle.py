#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
"""Autograder: Request-Response Cycle."""
import socket

# Socket Initialization
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('data.pr4e.org', 80))
g = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
s.send(g)

# Receive Data
while True:
    d = s.recv(512)
    if len(d) < 1:
        break
    print(d.decode(),end='')
