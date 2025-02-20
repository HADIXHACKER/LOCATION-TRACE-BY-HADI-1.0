import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr
import pyfiglet
import sys
import uuid
import webbrowser
from fake_useragent import UserAgent
import socket
import whois
import dns.resolver
import re

# Color Definitions
WH = '\033[1;97m'  # White
GR = '\033[1;92m'  # Green
RE = '\033[1;91m'  # Red
CY = '\033[1;96m'  # Cyan
YE = '\033[1;93m'  # Yellow
PU = '\033[1;95m'  # Purple
BL = '\033[1;94m'  # Blue

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

ab = pyfiglet.figlet_format("HADI_X_HACKER")
print(GR + ab)

def type_effect(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def banner():
    type_effect(f"{WH}Script Type>> {CY}Advanced OSINT Tool")
    type_effect(f"{WH}Telegram >> {YE}@HADI_X_HACKER321")
    type_effect(f"{WH}Creator >> {YE}HADI_X_HACKER")
    print('\n' + WH + '='*50 + '\n')

# Existing Core Functions
def IP_Track():
    clear()
    try:
        ip = input(f"{WH}[+] Enter IP address: {GR}")
        print(f"{WH}\n[+] Tracking IP: {GR}{ip}")
        response = requests.get(f"http://ipwho.is/{ip}")
        data = response.json()
        
        print(f"\n{WH}===== IP Information =====")
        print(f"{WH}Country: {GR}{data.get('country', 'N/A')}")
        print(f"{WH}Region: {GR}{data.get('region', 'N/A')}")
        print(f"{WH}City: {GR}{data.get('city', 'N/A')}")
        print(f"{WH}ISP: {GR}{data.get('connection', {}).get('isp', 'N/A')}")
        print(f"{WH}Coordinates: {GR}{data.get('latitude', 'N/A')}, {data.get('longitude', 'N/A')}")
        print(f"{WH}Map: {GR}https://www.google.com/maps/@{data.get('latitude')},{data.get('longitude')},8z")
    except Exception as e:
        print(f"{RE}[!] Error: {str(e)}")
    input(f"\n{WH}Press Enter to continue...")

def showIP():
    clear()
    try:
        response = requests.get('https://api.ipify.org')
        print(f"{WH}\n[+] Your Public IP: {GR}{response.text}")
    except Exception as e:
        print(f"{RE}[!] Error: {str(e)}")
    input(f"\n{WH}Press Enter to continue...")

# New Advanced Functions
def phone_tracker():
    clear()
    try:
        phone = input(f"{WH}[+] Enter phone number with country code: {GR}")
        parsed = phonenumbers.parse(phone)
        
        print(f"\n{WH}===== Phone Information =====")
        print(f"{WH}Country: {GR}{geocoder.description_for_number(parsed, 'en')}")
        print(f"{WH}Carrier: {GR}{carrier.name_for_number(parsed, 'en')}")
        print(f"{WH}Timezone: {GR}{timezone.time_zones_for_number(parsed)[0]}")
        print(f"{WH}Valid: {GR}{phonenumbers.is_valid_number(parsed)}")
    except Exception as e:
        print(f"{RE}[!] Error: {str(e)}")
    input(f"\n{WH}Press Enter to continue...")

def mac_lookup():
    clear()
    try:
        mac = input(f"{WH}[+] Enter MAC address: {GR}").upper()
        print(f"\n{WH}===== MAC Information =====")
        print(f"{WH}Vendor: {GR}{resolve_mac_vendor(mac)}")
        print(f"{WH}Unicast/Multicast: {GR}{'Unicast' if int(mac[:2], 16) % 2 == 0 else 'Multicast'}")
        print(f"{WH}Universal/Local: {GR}{'Universal' if int(mac[:2], 16) & 0b00000010 == 0 else 'Local'}")
    except Exception as e:
        print(f"{RE}[!] Error: {str(e)}")
    input(f"\n{WH}Press Enter to continue...")

def resolve_mac_vendor(mac):
    try:
        with open('mac-vendors.txt', 'r') as f:
            for line in f:
                if mac[:8].replace(':', '').upper() in line.upper():
                    return line.split('\t')[1].strip()
        return "Unknown"
    except:
        return "Unknown"

def whois_lookup():
    clear()
    try:
        domain = input(f"{WH}[+] Enter domain: {GR}")
        print(f"\n{WH}===== WHOIS Information =====")
        w = whois.whois(domain)
        print(f"{WH}Registrar: {GR}{w.registrar}")
        print(f"{WH}Creation Date: {GR}{w.creation_date}")
        print(f"{WH}Expiration Date: {GR}{w.expiration_date}")
        print(f"{WH}Name Servers: {GR}{', '.join(w.name_servers)}")
    except Exception as e:
        print(f"{RE}[!] Error: {str(e)}")
    input(f"\n{WH}Press Enter to continue...")

def social_media_search():
    clear()
    username = input(f"{WH}[+] Enter username: {GR}")
    sites = {
        'Facebook': f'https://facebook.com/{username}',
        'Twitter': f'https://twitter.com/{username}',
        'Instagram': f'https://instagram.com/{username}',
        'GitHub': f'https://github.com/{username}'
    }
    
    print(f"\n{WH}===== Social Media Presence =====")
    for site, url in sites.items():
        try:
            response = requests.get(url)
            print(f"{WH}{site}: {GR}{'Found' if response.status_code == 200 else 'Not Found'}")
        except:
            print(f"{WH}{site}: {RE}Error")
    input(f"\n{WH}Press Enter to continue...")

def password_strength_check():
    clear()
    password = input(f"{WH}[+] Enter password to check: {GR}")
    strength = 0
    
    if len(password) >= 8: strength +=1
    if re.search(r"[A-Z]", password): strength +=1
    if re.search(r"[a-z]", password): strength +=1
    if re.search(r"[0-9]", password): strength +=1
    if re.search(r"[!@#$%^&*()]", password): strength +=1
    
    print(f"\n{WH}===== Password Strength =====")
    print(f"{WH}Strength: {GR}{strength}/5")
    input(f"\n{WH}Press Enter to continue...")

def fake_user_agent():
    clear()
    ua = UserAgent()
    print(f"\n{WH}===== Fake User Agents =====")
    print(f"{WH}Chrome: {GR}{ua.chrome}")
    print(f"{WH}Firefox: {GR}{ua.firefox}")
    print(f"{WH}Edge: {GR}{ua.edge}")
    input(f"\n{WH}Press Enter to continue...")

def website_scanner():
    clear()
    url = input(f"{WH}[+] Enter website URL: {GR}")
    try:
        print(f"\n{WH}===== Website Information =====")
        ip = socket.gethostbyname(url)
        print(f"{WH}IP Address: {GR}{ip}")
        
        # DNS Records
        print(f"\n{WH}DNS Records:")
        for qtype in ['A', 'AAAA', 'MX', 'NS', 'SOA', 'TXT']:
            try:
                answers = dns.resolver.resolve(url, qtype)
                print(f"{WH}{qtype}: {GR}{', '.join([str(r) for r in answers])}")
            except:
                pass
    except Exception as e:
        print(f"{RE}[!] Error: {str(e)}")
    input(f"\n{WH}Press Enter to continue...")

def main_menu():
    while True:
        clear()
        banner()
        options = [
            {'num': 1, 'text': 'IP Tracker', 'func': IP_Track},
            {'num': 2, 'text': 'Show Your IP', 'func': showIP},
            {'num': 3, 'text': 'Phone Number Tracker', 'func': phone_tracker},
            {'num': 4, 'text': 'MAC Address Lookup', 'func': mac_lookup},
            {'num': 5, 'text': 'WHOIS Lookup', 'func': whois_lookup},
            {'num': 6, 'text': 'Social Media Search', 'func': social_media_search},
            {'num': 7, 'text': 'Password Strength Check', 'func': password_strength_check},
            {'num': 8, 'text': 'Fake User Agent', 'func': fake_user_agent},
            {'num': 9, 'text': 'Website Scanner', 'func': website_scanner},
            {'num': 0, 'text': 'Exit', 'func': sys.exit}
        ]

        for opt in options:
            print(f"{WH}[{GR}{opt['num']}{WH}] {opt['text']}")

        try:
            choice = int(input(f"\n{WH}[+] Select option: {GR}"))
            for opt in options:
                if opt['num'] == choice:
                    opt['func']()
                    break
            else:
                print(f"{RE}[!] Invalid option")
                time.sleep(1)
        except ValueError:
            print(f"{RE}[!] Please enter a number")
            time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{RE}[!] Exiting...")
            sys.exit()

if __name__ == '__main__':
    try:
        main_menu()
    except Exception as e:
        print(f"{RE}[!] Critical error: {str(e)}")
        sys.exit(1)
