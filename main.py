# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine

import resources

application_path = (
    os.path.dirname(sys.executable)
    if getattr(sys, "frozen", False)
    else os.path.dirname(os.path.abspath(__file__))
)

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon(":/icons/app.ico"))

    engine = QQmlApplicationEngine()
    qml_path = os.fspath(Path(__file__).resolve().parent / "main.qml")
    engine.load(qml_path)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
