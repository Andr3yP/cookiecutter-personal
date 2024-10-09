import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")


# Iniciar ambiente virtual
subprocess.call(['python', '-m', 'venv', 'venv'])


# Path to a Python interpreter that runs any Python script
# under the virtualenv /path/to/virtualenv/
python_venv =   os.getcwd()+"\\venv\\Scripts\\python.exe"


# Verifica si existe environment.yml o requirements.txt
if os.path.exists('environment.yml'):
    print(f"{MESSAGE_COLOR}Creating Conda environment from environment.yml...{RESET_ALL}")
    subprocess.call(['conda', 'env', 'create', '--file', 'environment.yml'])
    
elif os.path.exists('requirements.txt'):
    print(f"{MESSAGE_COLOR}Installing requirements from requirements.txt...{RESET_ALL}")
    subprocess.call([python_venv, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.call([python_venv, '-m', 'pip', 'install', '-r', 'requirements.txt'])

else:
    print(f"{MESSAGE_COLOR}No environment.yml or requirements.txt found. Skipping dependency installation.{RESET_ALL}")



# Configurar el ambiente para recibir notebooks.
if '{{ cookiecutter.project_packages }}' == 'Notebook':
  subprocess.call([python_venv,'-m', 'ipykernel', 'install', '--user', '--name', 'venv'])


# Iniciar Git
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun Andrey!{RESET_ALL}")

