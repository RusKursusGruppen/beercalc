# -*- coding: utf-8 -*-
import os

# Recursively return file paths in a directory
def get_files(directory):
    dir = os.listdir(directory)
    dir = [os.path.join(directory, entry) for entry in dir]
    files = filter(os.path.isfile, dir)
    directories = filter(os.path.isdir, dir)
    for dir in directories:
        files += get_files(dir)
    return files
