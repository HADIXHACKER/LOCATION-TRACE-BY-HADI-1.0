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
    ab = pyfiglet.figlet_format("HADI_X_HACKER", font="slant")
    print(f"{Gr}{ab}")
    print(f"{Wh}{Gr}===================================================")
    print(f"{Re}[{Wh}INFO{Re}] {Gr}Tool By: HADI_X_HACKER")
    print(f"{Re}[{Wh}INFO{Re}] {Gr}Telegram: @HADI_X_HACKER321")
    print(f"{Re}[{Wh}INFO{Re}] {Gr}Tool Status: {Wh}Working")
    print(f"{Re}[{Wh}INFO{Re}] {Gr}Tool Value: {Wh}Paid Script")
    print(f"{Re}[{Wh}INFO{Re}] {Gr}Valid Time: {Wh}6 months")
    print(f"{Wh}{Gr}===================================================")

# Smooth Text Function for Banner Animation
def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)

# Main Banner Info
def show_banner():
    to(f"{Re}Script Type >> {Gr}HADI_X_HACKER Location Tool 🔥")
    to(f"{Re}Telegram >> {Gr}@HADI_X_HACKER321")
    to(f"{Re}Creator >> {Gr}HADI_X_HACKER")
    to(f"{Re}Tool Status >> {Gr}Working")
    to(f"{Re}Tool Value >> {Gr}Paid Script")
    to(f"{Re}Time >> {Gr}6 months")
    print(f"\n{Gr}[{Re}Note{Gr}]: {Re}This is a fully functional tool for Termux!")

# Improved IP Tracker Function with Error Handling
def IP_Track():
    ip = input(f"{Wh}\nEnter IP target: {Gr}")
    print()
    print(f"{Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============")
    try:
        req_api = requests.get(f"http://ipwho.is/{ip}")
        ip_data = req_api.json()
        if req_api.status_code != 200:
            print(f"{Re}Error: Could not fetch data for IP: {ip}")
            return
        print(f"{Wh}\nIP target       :{Gr}", ip)
        print(f"{Wh}Type IP         :{Gr}", ip_data.get("type", "N/A"))
        print(f"{Wh}Country         :{Gr}", ip_data.get("country", "N/A"))
        print(f"{Wh}Country Code    :{Gr}", ip_data.get("country_code", "N/A"))
        print(f"{Wh}City            :{Gr}", ip_data.get("city", "N/A"))
        print(f"{Wh}Continent       :{Gr}", ip_data.get("continent", "N/A"))
        print(f"{Wh}Continent Code  :{Gr}", ip_data.get("continent_code", "N/A"))
        print(f"{Wh}Region          :{Gr}", ip_data.get("region", "N/A"))
        print(f"{Wh}Region Code     :{Gr}", ip_data.get("region_code", "N/A"))
        print(f"{Wh}Latitude        :{Gr}", ip_data.get("latitude", "N/A"))
        print(f"{Wh}Longitude       :{Gr}", ip_data.get("longitude", "N/A"))
        lat = ip_data.get('latitude', '0')
        lon = ip_data.get('longitude', '0')
        print(f"{Wh}Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
        print(f"{Wh}EU              :{Gr}", ip_data.get("is_eu", "N/A"))
        print(f"{Wh}Postal          :{Gr}", ip_data.get("postal", "N/A"))
        print(f"{Wh}Calling Code    :{Gr}", ip_data.get("calling_code", "N/A"))
        print(f"{Wh}Capital         :{Gr}", ip_data.get("capital", "N/A"))
        print(f"{Wh}Country Flag    :{Gr}", ip_data.get("flag", {}).get("emoji", "N/A"))
    except Exception as e:
        print(f"{Re}Error: {e}")

# Show Your Public IP Function
def showIP():
    response = requests.get('https://api.ipify.org/')
    show_ip = response.text
    print(f"\n{Wh}========== {Gr}SHOW INFORMATION YOUR IP {Wh}==========")
    print(f"\n{Wh}[{Gr} + {Wh}] Your IP Address: {Gr}{show_ip}")
    print(f"\n{Wh}===============================================")

# Check VPN Status Function
def check_vpn_status():
    ip = input(f"{Wh}Enter IP to check VPN status: {Gr}")
    response = requests.get(f"https://vpnapi.io/api/{ip}")
    if response.status_code == 200:
        vpn_data = response.json()
        if vpn_data.get("security", {}).get("is_vpn", False):
            print(f"{Wh}[{Re}-{Wh}] VPN Detected: {Gr}Yes")
        else:
            print(f"{Wh}[{Gr}+{Wh}] VPN Detected: {Re}No")
    else:
        print(f"{Re}Error fetching VPN status.")

# Show System Information
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

# Shorten URL
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
    
    # Option to return to main menu after an action
    input(f"\nPress Enter to return to the main menu...")

# Main function to run the script
if __name__ == "__main__":
    while True:
        banner()
        option()
        
