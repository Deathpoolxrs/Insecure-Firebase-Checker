import requests

def check_insecure_read(database_url, first_request=False):
    if first_request:
        response = requests.get(database_url + "/.json")
    else:
        response = requests.get(database_url)
    if response.status_code == 200:
        data = response.json()
        if data is None or isinstance(data, dict):
            return True
    return False

def check_insecure_write(database_url, data):
    response = requests.post(database_url + ".json", json=data)
    return response.status_code == 200

def check_vulnerable_endpoints(database_url):
    vulnerable_endpoints = []
    endpoints_to_check = ["Users", "Logs"]  # Add more endpoints if needed
    for endpoint in endpoints_to_check:
        read_url = database_url + f"/{endpoint}.json"
        write_url = database_url + f"/{endpoint}.json"
        
        if check_insecure_read(read_url):
            vulnerable_endpoints.append(f"Read access to {endpoint} endpoint")
        
        if check_insecure_write(write_url, {"test": "testing"}):
            vulnerable_endpoints.append(f"Write access to {endpoint} endpoint")
    
    return vulnerable_endpoints

def main():
    urls_file = input("Please enter the filename containing the list of Firebase URLs: ")
    with open(urls_file, "r") as file:
        urls = file.readlines()
    
    for url in urls:
        url = url.strip()  # Remove leading/trailing whitespace
        print("Checking:", url)
        
        # Check for insecure read access
        if check_insecure_read(url, first_request=True):
            print("Firebase allows anonymous read access or only read access.")
        else:
            print("Firebase read access is secure.")
        
        # Check for vulnerable endpoints (both read and write)
        vulnerable_endpoints = check_vulnerable_endpoints(url)
        if vulnerable_endpoints:
            print("Vulnerable endpoints detected:")
            for endpoint in vulnerable_endpoints:
                print("-", endpoint)
        else:
            print("No vulnerable endpoints detected.")
        
        print()  # Add a newline for readability between URLs

if __name__ == "__main__":
    main()
