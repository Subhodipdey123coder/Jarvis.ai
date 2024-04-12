import subprocess

def get_mac_address(ip_address):
    try:
        # Execute the arp command to get MAC address associated with the IP address
        arp_output = subprocess.check_output(['arp', '-n', ip_address])
        arp_output = arp_output.decode('utf-8')
        
        # Extract MAC address from the output
        mac_address = arp_output.split()[3]
        
        return mac_address
    except subprocess.CalledProcessError:
        print("MAC address not found for the IP address:", ip_address)
        return None

# Example usage:
ip_address = "192.168.1.1"  # Replace this with the IP address you want to find the MAC address for
mac_address = get_mac_address(ip_address)

if mac_address:
    print(f"MAC address for IP address {ip_address}:", mac_address)
