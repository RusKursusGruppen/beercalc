#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys
from os.path import dirname, join, realpath
import os

# Prepend 3rd-party to path
dname = realpath(dirname(__file__))
sys.path[0] = join(dname)
sys.path.insert(0, join(sys.path[0], "3rd-party"))

os.chdir(dname)

from werkzeug import run_simple
from app.application import Application

app = Application(debug=False)
bind_address = "127.0.0.1"
port = 5000

run_simple(
    bind_address, port, app, use_debugger=False, use_reloader=False
)

