public_ip = requests.get('https://api.ipify.org').text
                        speak(f"Public IP Address: {public_ip}")