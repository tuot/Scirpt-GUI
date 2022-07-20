#!/bin/bash

pyinstaller main.py --onefile --windowed --clean --name Script-Gui --icon app.ico \
    --add-data "main.qml;."