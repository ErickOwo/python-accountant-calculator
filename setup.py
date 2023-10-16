from cx_Freeze import setup, Executable

base = None    

executables = [Executable("calculadora.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Calculadora",
    options = options,
    version = "1.0",
    description = '<any description>',
    executables = executables
)