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

# Example Functions for New Tools

# 1. Phone Number Information Tool (using Numverify API)
def phone_number_info():
    phone = input(f"{Wh}Enter Phone Number (with country code, e.g. +14155552671): {Gr}")
    api_key = "YOUR_NUMVERIFY_API_KEY"  # Get your free API key from numverify.com
    url = f"https://apilayer.net/api/validate?access_key={api_key}&number={phone}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get('valid'):
            print(f"{Wh}\nPhone Number Info:")
            print(f"{Wh}Country         :{Gr}", data.get('country_name', 'N/A'))
            print(f"{Wh}Location        :{Gr}", data.get('location', 'N/A'))
            print(f"{Wh}Carrier         :{Gr}", data.get('carrier', 'N/A'))
            print(f"{Wh}Line Type       :{Gr}", data.get('line_type', 'N/A'))
            print(f"{Wh}Valid Number    :{Gr}", data.get('valid', 'No'))
        else:
            print(f"{Re}Error: Invalid phone number or could not fetch data.")
    except Exception as e:
        print(f"{Re}Error: {e}")

# 2. Username Information Tool (using GitHub API as example)
def username_info():
    username = input(f"{Wh}Enter Username (GitHub): {Gr}")
    url = f"https://api.github.com/users/{username}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'login' in data:
            print(f"{Wh}\nUsername Info:")
            print(f"{Wh}Username        :{Gr}", data['login'])
            print(f"{Wh}Name            :{Gr}", data.get('name', 'N/A'))
            print(f"{Wh}Bio             :{Gr}", data.get('bio', 'N/A'))
            print(f"{Wh}Location        :{Gr}", data.get('location', 'N/A'))
            print(f"{Wh}Public Repos    :{Gr}", data.get('public_repos', 'N/A'))
            print(f"{Wh}Followers       :{Gr}", data.get('followers', 'N/A'))
            print(f"{Wh}Following       :{Gr}", data.get('following', 'N/A'))
        else:
            print(f"{Re}Error: Username not found.")
    except Exception as e:
        print(f"{Re}Error: {e}")

# 3. Domain Information (Whois Lookup)
def domain_info():
    domain = input(f"{Wh}Enter Domain (e.g. google.com): {Gr}")
    url = f"https://whoisapi.p.rapidapi.com/whois?identifier={domain}"
    
    headers = {
        "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",  # Replace with your own key
        "X-RapidAPI-Host": "whoisapi.p.rapidapi.com"
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        print(f"{Wh}\nDomain Info:")
        print(f"{Wh}Domain          :{Gr}", data.get('domainName', 'N/A'))
        print(f"{Wh}Registrar       :{Gr}", data.get('registrarName', 'N/A'))
        print(f"{Wh}Country         :{Gr}", data.get('country', 'N/A'))
        print(f"{Wh}Creation Date   :{Gr}", data.get('creationDate', 'N/A'))
        print(f"{Wh}Expiry Date     :{Gr}", data.get('expirationDate', 'N/A'))
    except Exception as e:
        print(f"{Re}Error: {e}")

# 4. Geolocation by Phone Number
def geolocation_by_phone():
    phone = input(f"{Wh}Enter Phone Number (with country code, e.g. +14155552671): {Gr}")
    api_key = "YOUR_NUMVERIFY_API_KEY"  # Your API key
    url = f"https://apilayer.net/api/validate?access_key={api_key}&number={phone}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        print(f"{Wh}\nGeolocation Info:")
        print(f"{Wh}Country         :{Gr}", data.get('country_name', 'N/A'))
        print(f"{Wh}Location        :{Gr}", data.get('location', 'N/A'))
    except Exception as e:
        print(f"{Re}Error: {e}")

# 5. QR Code Generator Tool
def qr_code_generator():
    import qrcode
    data = input(f"{Wh}Enter Data for QR Code: {Gr}")
    qr = qrcode.make(data)
    qr.show()  # Display the QR code
    qr.save("qr_code.png")  # Save the QR code image

# 6. Device Fingerprint Info Tool
def device_fingerprint_info():
    fingerprint = uuid.uuid4()
    print(f"{Wh}\nDevice Fingerprint Info:")
    print(f"{Wh}Device ID (UUID) :{Gr}", fingerprint)

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
        
