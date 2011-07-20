#!/usr/bin/python2 -B
# -*- coding: utf-8 -*-
import sys
from os.path import dirname, join

# Correct path if pwd is not here, and prepend 3rd-party to path
sys.path[0] = join(dirname(__file__))
sys.path.insert(0, join(sys.path[0], "3rd-party"))


from app.controller import run

run()


