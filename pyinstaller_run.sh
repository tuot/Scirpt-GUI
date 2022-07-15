#!/bin/bash

pyinstaller main.py --windowed --clean --name Script-Gui --icon app.ico \
    --add-data "main.qml;."