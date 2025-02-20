import json
import requests
import time
import os
import sys
import uuid
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

# Define the IP Tracker Function
def IP_Track():
    ip_target = input(f"{Wh}Enter IP target: {Gr}")
    # Example: Fetching information about the IP using a public API like ipinfo.io
    url = f"https://ipinfo.io/{ip_target}/json"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        print(f"{Wh}IP Information for {Gr}{ip_target}:")
        print(f"{Wh}IP: {Gr}{data.get('ip', 'N/A')}")
        print(f"{Wh}City: {Gr}{data.get('city', 'N/A')}")
        print(f"{Wh}Region: {Gr}{data.get('region', 'N/A')}")
        print(f"{Wh}Country: {Gr}{data.get('country', 'N/A')}")
        print(f"{Wh}Location: {Gr}{data.get('loc', 'N/A')}")
    except Exception as e:
        print(f"{Re}Error: {e}")

# Main Menu with Banner
def option():
    clear()  # Clear the screen
    show_banner()
    options = [
        {'num': 1, 'text': 'IP Tracker', 'func': IP_Track},  # Now IP_Track is defined
        {'num': 2, 'text': 'Show Your IP', 'func': showIP},  # Define other functions similarly
        {'num': 3, 'text': 'Check VPN Status', 'func': check_vpn_status},
        {'num': 4, 'text': 'System Info', 'func': system_info},
        {'num': 5, 'text': 'Shorten URL', 'func': shorten_url},
        {'num': 6, 'text': 'Phone Number Info', 'func': phone_number_info},
        {'num': 7, 'text': 'Username Info', 'func': username_info},
        {'num': 8, 'text': 'Domain Info (Whois)', 'func': domain_info},
        {'num': 9, 'text': 'Geolocation by Phone', 'func': geolocation_by_phone},
        {'num': 10, 'text': 'QR Code Generator', 'func': qr_code_generator},
        {'num': 11, 'text': 'Device Fingerprint Info', 'func': device_fingerprint_info},
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
