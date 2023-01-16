
"""
Paul Fanning rel 1.0 1/15/2023
The program below is the first step in using Python to automate nmap scripts
"""
import nmap3 # Import the nmap3 library

nmap = nmap3.Nmap() # Create an instance of the Nmap class

results = nmap.scan_top_ports("scanme.nmap.org") # Perform a scan on the host "scanme.nmap.org" using the scan_top_ports method
print(results) # Print the results of the scan to the console

os_results = nmap.nmap_os_detection("scanme.nmap.org") # Perform OS detection on the host "scanme.nmap.org" using the nmap_os_detection method
print(os_results) # Print the results of the OS detection to the console
