#!/bin/bash

nuitka.bat --standalone --onefile --follow-imports --plugin-enable=pyside6 \
    --windows-disable-console \
    --windows-icon-from-ico=app.ico \
    --include-qt-plugins=sensible,qml \
    --include-data-file=*.qml=. \
    -o Script-Gui.exe main.py