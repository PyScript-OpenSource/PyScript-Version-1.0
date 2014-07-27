import sys
from cx_Freeze import setup, Executable
class scrpy:
    def compileExe(name,version,description,file,appType):
        if appType == 'g':
            setup(
                name = name,
                version = version,
                description = description,
                executables = [Executable(file, base = "Win32GUI")])
        if appType == 'c':
            setup(
                name = name,
                version = version,
                description = description,
                executables = [Executable(file, base = "Console")])
