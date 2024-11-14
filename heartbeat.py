import os
import requests

def send_heartbeat(mac_addresses, location):
    """
    Send a heartbeat signal with the provided MAC addresses to the specified backend URL.
    
    :param mac_addresses: List of MAC addresses to include in the heartbeat signal.
    :param location: Location information to be included in the heartbeat signal.
    """
    # Fetch environment variables
    ticket_backend_url = os.getenv("TICKET_BACKEND_URL")
    ticket_backend_token = os.getenv("TICKET_BACKEND_TOKEN")
    
    # Ensure required environment variables are set
    if not all([ticket_backend_url, ticket_backend_token]):
        raise ValueError("TICKET_BACKEND_URL or TICKET_BACKEND_TOKEN environment variable is missing.")
    
    # Normalize all MAC addresses
    normalized_macs = [normalize_mac(mac) for mac in mac_addresses]
    mac_addresses_str = ",".join(normalized_macs)
    
    # Prepare data payload
    data = {
        "key": ticket_backend_token,
        "macAddresses": mac_addresses_str,
        "location": location
    }
    
    # Send the POST request
    response = requests.post(f"{ticket_backend_url}/api/heartbeat", data=data)
    # Print a message to indicate the request status
    if response.ok:
        print("Heartbeat sent successfully.")
    else:
        print("Failed to send heartbeat.", response.status_code)


def normalize_mac(mac):
    """
    Normalize a MAC address to uppercase with ':' as the separator.
    
    :param mac: The MAC address as a string.
    :return: The normalized MAC address as a string.
    """
    # Remove any existing separators (e.g., ":" or "-") and convert to uppercase
    clean_mac = mac.replace(":", "").replace("-", "").upper()
    
    # Re-insert ':' every two characters
    normalized_mac = ":".join(clean_mac[i:i+2] for i in range(0, len(clean_mac), 2))
    
    return normalized_mac
