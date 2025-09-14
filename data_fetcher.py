import requests as r

API_KEY = 'i3BxI1L4bQpTbXGGxbT+jQ==zeBl0kQPwglZqwTI'

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
