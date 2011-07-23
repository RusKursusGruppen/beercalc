#!/usr/bin/python2 -B
# -*- coding: utf-8 -*-
import sys
from os.path import dirname, join

# Correct path if pwd is not here, and prepend 3rd-party to path
sys.path[0] = join(dirname(__file__))
sys.path.insert(0, join(sys.path[0], "3rd-party"))

from werkzeug import run_simple
from app.application import Application

app = Application(debug=True)
bind_address = "127.0.0.1"
port = 5000
run_simple(
    bind_address, port, app, use_debugger=True, use_reloader=True
)
