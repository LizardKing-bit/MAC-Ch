#!/usr/bin/env python

import subprocess

interface = "eth0" #change to the correct interface whose mac you're changing
new_mac = "00:11:22:33:44:88" #choose which MAC you want to change it to

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig "+ interface +" down", shell=True) #"+ interface +" is how to add the int variable to the code
subprocess.call("ifconfig "+ interface +"  hw ether "+ new_mac , shell=True) #+ new_mac is how to add the mac var to code
subprocess.call("ifconfig "+ interface +"  up", shell=True)