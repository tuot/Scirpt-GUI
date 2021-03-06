import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {
    "packages": ["os"],
    "excludes": ["tkinter",],
    "include_files": ["main.qml", "app.ico"],
}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
    script="main.py",
    base=base,
    target_name="script-gui",
    icon="app.ico",
)

setup(name="script-gui",
      version="0.1",
      description="My Script GUI App",
      options={"build_exe": build_exe_options},
      executables=[target],
      )
