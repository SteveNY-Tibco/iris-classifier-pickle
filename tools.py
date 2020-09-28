import subprocess

def bash(command):
    return subprocess.check_call(command.split())
    
#    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
#    output, error = process.communicate()
#    return output, error
