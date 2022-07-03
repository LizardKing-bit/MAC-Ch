#!/usr/bin/env python

import subprocess

interface = input("interface > ") #change to the correct interface whose mac you're changing
new_mac = input("new MAC > ") #choose which MAC you want to change it to

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"]) #securely lest user input and run command
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
