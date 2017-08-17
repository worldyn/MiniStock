# A test that runs multiple clients that talks with the application
# Assumes you have an application.py running. Can be fun to run this script
# several times, in multiple terminal windows
import subprocess
from subprocess import PIPE

PROCESSES_COUNT = 2000

def main():
    process = subprocess.Popen('echo %USERNAME%', stdout=PIPE, shell=True)
    username = process.communicate()[0]
    print(username) #prints the username of the account you're logged in as

    i = 0
    while i < PROCESSES_COUNT:
        process = subprocess.Popen('python user_interface_test.py', shell=True)
        i += 1

if __name__ == '__main__':
    main()
