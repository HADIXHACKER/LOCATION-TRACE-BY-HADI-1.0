import json
import requests
import time
import os
import sys
import uuid
import webbrowser
import fake_useragent
import pyfiglet
import platform
import subprocess

# Color Definitions
Wh = '\033[1;37m'  # White
Gr = '\033[1;32m'  # Green
Re = '\033[1;31m'  # Red
Bl = '\033[1;34m'  # Blue
Ye = '\033[1;33m'  # Yellow
Cy = '\033[1;36m'  # Cyan
Ma = '\033[1;35m'  # Magenta

# Clear Screen Function
def clear():
    if os.name == 'posix':
        os.system('clear')  # For Unix-like systems (Linux, macOS)
    elif os.name == 'nt':
        os.system('cls')  # For Windows systems

# Banner Creation
def banner():
    ab = pyfiglet.figlet_format("HADI_X_HACKER")
    print(f"{Ma}{ab}")

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)

def show_banner():
    to(f"{Re}Script Type>> {Gr}HADI_X_HACKER Location Tool 🔥")
    to(f"{Re}Telegram >> {Gr}@HADI_X_HACKER321")
    to(f"{Re}Creator >> {Gr}HADI_X_HACKER")
    to(f"{Re}Tool Status >> {Gr}Working")
    to(f"{Re}Tool Value >> {Gr}Paid Script")
    to(f"{Re}Time >> {Gr}6 months")
    print('\n')

# Example Functions
def IP_Track():
    ip = input(f"{Wh}\nEnter IP target: {Gr}")
    print()
    print(f"{Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============")
    try:
        req_api = requests.get(f"http://ipwho.is/{ip}")
        ip_data = json.loads(req_api.text)
        time.sleep(2)
        print(f"{Wh}\nIP target       :{Gr}", ip)
        print(f"{Wh}Type IP         :{Gr}", ip_data["type"])
        print(f"{Wh}Country         :{Gr}", ip_data["country"])
        print(f"{Wh}Country Code    :{Gr}", ip_data["country_code"])
        print(f"{Wh}City            :{Gr}", ip_data["city"])
        print(f"{Wh}Continent       :{Gr}", ip_data["continent"])
        print(f"{Wh}Continent Code  :{Gr}", ip_data["continent_code"])
        print(f"{Wh}Region          :{Gr}", ip_data["region"])
        print(f"{Wh}Region Code     :{Gr}", ip_data["region_code"])
        print(f"{Wh}Latitude        :{Gr}", ip_data["latitude"])
        print(f"{Wh}Longitude       :{Gr}", ip_data["longitude"])
        lat = int(ip_data['latitude'])
        lon = int(ip_data['longitude'])
        print(f"{Wh}Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
        print(f"{Wh}EU              :{Gr}", ip_data["is_eu"])
        print(f"{Wh}Postal          :{Gr}", ip_data["postal"])
        print(f"{Wh}Calling Code    :{Gr}", ip_data["calling_code"])
        print(f"{Wh}Capital         :{Gr}", ip_data["capital"])
        print(f"{Wh}Borders         :{Gr}", ip_data["borders"])
        print(f"{Wh}Country Flag    :{Gr}", ip_data["flag"]["emoji"])
        print(f"{Wh}ASN             :{Gr}", ip_data["connection"]["asn"])
        print(f"{Wh}ORG             :{Gr}", ip_data["connection"]["org"])
        print(f"{Wh}ISP             :{Gr}", ip_data["connection"]["isp"])
        print(f"{Wh}Domain          :{Gr}", ip_data["connection"]["domain"])
        print(f"{Wh}ID              :{Gr}", ip_data["timezone"]["id"])
        print(f"{Wh}ABBR            :{Gr}", ip_data["timezone"]["abbr"])
        print(f"{Wh}DST             :{Gr}", ip_data["timezone"]["is_dst"])
        print(f"{Wh}Offset          :{Gr}", ip_data["timezone"]["offset"])
        print(f"{Wh}UTC             :{Gr}", ip_data["timezone"]["utc"])
        print(f"{Wh}Current Time    :{Gr}", ip_data["timezone"]["current_time"])
    except Exception as e:
        print(f"{Re}Error: {e}")

def showIP():
    response = requests.get('https://api.ipify.org/')
    show_ip = response.text
    print(f"\n{Wh}========== {Gr}SHOW INFORMATION YOUR IP {Wh}==========")
    print(f"\n{Wh}[{Gr} + {Wh}] Your IP Address: {Gr}{show_ip}")
    print(f"\n{Wh}===============================================")

# Advanced Functions
def check_vpn_status():
    ip = input(f"{Wh}Enter IP to check VPN status: {Gr}")
    response = requests.get(f"https://vpnapi.io/api/{ip}")
    if response.status_code == 200:
        vpn_data = response.json()
        if vpn_data["security"]["is_vpn"]:
            print(f"{Wh}[{Re}-{Wh}] VPN Detected: {Gr}Yes")
        else:
            print(f"{Wh}[{Gr}+{Wh}] VPN Detected: {Re}No")
    else:
        print(f"{Re}Error fetching VPN status.")

def system_info():
    print(f"{Wh}System Info:")
    uname = platform.uname()
    print(f"{Wh}System: {Gr}{uname.system}")
    print(f"{Wh}Node Name: {Gr}{uname.node}")
    print(f"{Wh}Release: {Gr}{uname.release}")
    print(f"{Wh}Version: {Gr}{uname.version}")
    print(f"{Wh}Machine: {Gr}{uname.machine}")
    print(f"{Wh}Processor: {Gr}{uname.processor}")
    print(f"{Wh}Platform: {Gr}{platform.platform()}")

def shorten_url():
    url = input(f"{Wh}Enter the URL to shorten: {Gr}")
    response = requests.get(f"https://api.shrtco.de/v2/shorten?url={url}")
    if response.status_code == 201:
        short_url = response.json()["result"]["short_link"]
        print(f"{Wh}Shortened URL: {Gr}{short_url}")
    else:
        print(f"{Re}Error shortening the URL.")

# Main Menu with Banner
def option():
    clear()  # Clear the screen
    show_banner()
    options = [
        {'num': 1, 'text': 'IP Tracker', 'func': IP_Track},
        {'num': 2, 'text': 'Show Your IP', 'func': showIP},
        {'num': 3, 'text': 'Check VPN Status', 'func': check_vpn_status},
        {'num': 4, 'text': 'System Info', 'func': system_info},
        {'num': 5, 'text': 'Shorten URL', 'func': shorten_url},
    ]
    
    for option in options:
        print(f"{Ye}[{option['num']}] {option['text']}")
    
    try:
        choice = int(input(f"\n{Wh}Choose an option: "))
        if 1 <= choice <= len(options):
            options[choice - 1]['func']()
        else:
            print(f"{Re}[Error] Invalid choice.")
    except ValueError:
        print(f"{Re}[Error] Please enter a valid number.")

if __name__ == "__main__":
    banner()
    option()
    
