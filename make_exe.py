from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == "win32":
    base = "Win32GUI"

bdist_msi_options = {
    "upgrade_code": "{48B079F4-B598-438D-A62A-8A233A3F8901}",
    "add_to_path": False,
    "initial_target_dir": r"[ProgramFilesFolder]\%s\%s" % ("Autoclicker - G@b", "Autoclicker")
}

executables = [Executable("main_GUI.py",
                          base=base,
                          target_name="AutoClicker",
                          icon="mouseclick.ico")]

packages = ["time", "threading", "tkinter", "pynput"]

options = {
    "build_exe": {
        "packages": packages,
        "include_files": ["mouseclick.ico"],
        "include_msvcr": True,
    }}

setup(
    name="Autoclicker",
    options=options,
    version="1.0",
    description="Autoclicker - G@b",
    author="G@b",
    executables=executables,
)
