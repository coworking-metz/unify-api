import os
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_connected_clients(site="default"):
    # Fetching credentials from environment variables
    controller_ip = os.getenv("CONTROLLER_IP")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    
    if not controller_ip or not username or not password:
        raise Exception("Controller IP, Username, and Password must be set in .env")
    
    # Construct the controller URL with https prefix
    controller_url = f"https://{controller_ip}"
    
    # Set up URLs and headers
    login_url = f"{controller_url}/api/auth/login"
    clients_url = f"{controller_url}/proxy/network/api/s/{site}/stat/sta"
    headers = {'Content-Type': 'application/json'}
    
    # Start a session
    with requests.Session() as session:
        # Login and store cookies
        login_payload = {"username": username, "password": password}
        response = session.post(login_url, json=login_payload, headers=headers, verify=False)
        
        # Check if login was successful
        if response.status_code != 200:
            raise Exception("Login failed: " + response.json().get("meta", {}).get("msg", "Unknown error"))
        
        # Fetch clients data
        response = session.get(clients_url, headers=headers, verify=False)
        
        # Check for success and return client data
        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            raise Exception("Failed to retrieve clients: " + response.json().get("meta", {}).get("msg", "Unknown error"))



def get_unifi_devices(site="default"):
    # Fetching credentials from environment variables
    controller_ip = os.getenv("CONTROLLER_IP")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    
    if not controller_ip or not username or not password:
        raise Exception("Controller IP, Username, and Password must be set in .env")
    
    # Construct the controller URL with https prefix
    controller_url = f"https://{controller_ip}"
    
    # Set up URLs and headers
    login_url = f"{controller_url}/api/auth/login"
    devices_url = f"{controller_url}/proxy/network/api/s/{site}/stat/device"
    headers = {'Content-Type': 'application/json'}
    
    # Start a session
    with requests.Session() as session:
        # Login and store cookies
        login_payload = {"username": username, "password": password}
        response = session.post(login_url, json=login_payload, headers=headers, verify=False)
        # # Debug login response
        # print("Login Response Status Code:", response.status_code)
        # print("Login Response Headers:", response.headers)
        # print("Login Response Content:", response.text)        
        # Check if login was successful
        if response.status_code != 200:
            raise Exception("Login failed: " + response.json().get("meta", {}).get("msg", "Unknown error"))
        
        # Fetch devices data
        response = session.get(devices_url, headers=headers, verify=False)
        
        # Check for success and return device data
        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            raise Exception("Failed to retrieve devices: " + response.json().get("meta", {}).get("msg", "Unknown error"))
