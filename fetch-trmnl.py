import os
import requests

def fetch_display_data():
    url = "https://usetrmnl.com/api/display"
    access_token = os.getenv("ACCESS_TOKEN")
    
    if not access_token:
        print("Error: ACCESS_TOKEN environment variable is not set.")
        return
    
    headers = {"access-token": f"{access_token}"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        print(f"Response Data: {data}")
        
        # Fetch and save the image
        image_response = requests.get(data['image_url'])
        image_response.raise_for_status()

        filename = "terminal-image.bmp"
        
        with open(filename, 'wb') as file:
            file.write(image_response.content)
        
        print(f"Image saved as {filename}")
    
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error occurred: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    fetch_display_data()
