
#!/usr/bin/env python

import subprocess


""" 
ssh based command dispatch system
"""

machines = ["shell.cjb.net"]

cmd = "uname"

for machine in machines:
	subprocess.call("ssh gh0st@%s %s"%(machine, cmd), shell=True)
