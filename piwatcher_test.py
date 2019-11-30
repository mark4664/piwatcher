#!/usr/bin/python3

# Script name: piwatcher_test.py
# Test python code for omzlo piwatcher circuit
# Mark Bradley
# 2019-11-30

###################################################################
# Code to test omzlo watch dog circit.
# Needs watchdog circuit board fitted and piwatcher programme.
# When a Pi is equiped with the watchdog circuit it will restart 
# unless you keep pressing enter in less than 10 seconds or use
# <ctrl> C to break out of the loop, breaking out sets the watchdog 
# timer to zero - disabled. 
# The wake command is set to 20 seconds to restart the Pi after that
# delay.
# See omzlo.com for details of circuit and piwatcher code.
###################################################################

import subprocess


# Check piwatcher status with - piwatcher status
watcher = subprocess.run(['/usr/local/bin/piwatcher','status'], stdout=subprocess.PIPE)
status = watcher.stdout.decode('UTF-8')
print(status)

# Set piwatcher wake time to 20 seconds - piwatcher wake 20
watcher = subprocess.run(['/usr/local/bin/piwatcher','wake','20'], stdout=subprocess.PIPE)

# Set piwatcher watch dog time out to 10 seconds - piwatcher watch 10
watcher = subprocess.run(['/usr/local/bin/piwatcher','watch','10'], stdout=subprocess.PIPE)

# Read all piwatcher's registers
watcher = subprocess.run(['/usr/local/bin/piwatcher','dump'], stdout=subprocess.PIPE)
status = watcher.stdout.decode('UTF-8')
print(status)

#Test loop - keep pressing enter within 10 seconds to stop the pi restarting
try:
    while True:
        print('If there is no input in the next 10 seconds the Pi will shut down!')
        input('Input something!')
        # Checking the status resets the watch dog timer
        watcher = subprocess.run(['/usr/local/bin/piwatcher','status'], stdout=subprocess.PIPE)
        status = watcher.stdout.decode('UTF-8')
        print(status)
        
except (KeyboardInterrupt):   # Run util stopped by keyboard interrupt....Ctrl + C
    # Set piwatcher watch dog time out to 0 seconds - disabled
    watcher = subprocess.run(['/usr/local/bin/piwatcher','watch','0'], stdout=subprocess.PIPE)
   
# Read all piwatcher's registers
watcher = subprocess.run(['/usr/local/bin/piwatcher','dump'], stdout=subprocess.PIPE)
status = watcher.stdout.decode('UTF-8')
print(status)
    
print('All Done') 
    
