import requests as r
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

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
    raw_data = r.get('https://api.api-ninjas.com/v1/animals', params = {'name': animal_name},
                     headers = {'X-Api-Key': API_KEY})

    output = raw_data.json()
    return output
