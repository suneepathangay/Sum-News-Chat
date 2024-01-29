import subprocess

import os


path=os.getcwd()+"/auth.sh"
subprocess.run([path],shell=True)