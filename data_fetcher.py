import os
import requests as r
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
if API_KEY is None:
    raise RuntimeError("Missing API Key")


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    try:
        raw_data = r.get('https://api.api-ninjas.com/v1/animals', params={'name': animal_name},
                         timeout=10, headers={'X-Api-Key': API_KEY})
        raw_data.raise_for_status()

    except r.exceptions.HTTPError as errh:
        if 400 <= raw_data.status_code < 500:
            # 400 errors
            print(f"Client Error ({raw_data.status_code}): Invalid request or resource not found.")
        elif 500 <= raw_data.status_code < 600:
            # 500 errors
            print(f"Server Error ({raw_data.status_code}): The server encountered an issue.")
        else:
            # 300 redirects
            print(f"HTTP Error: {errh}")

    except r.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except r.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except r.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
    else:
        return raw_data.json()

