import subprocess
import os

if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Elite', '__init__.py')
    if os.path.isfile(path): subprocess.run(['python', path])
    else: exit('File Not Found!')