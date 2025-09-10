import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

ANIMAL_DATA = load_data('animals_data.json')





for item in ANIMAL_DATA:
    item_index = ANIMAL_DATA.index(item)

    try:
        print("Name: ", ANIMAL_DATA[item_index]['name'])
        print("Diet: ", ANIMAL_DATA[item_index]['characteristics']['diet'])

        print("Location: ", end="")
        for location in ANIMAL_DATA[item_index]['locations']:
            if location != ANIMAL_DATA[item_index]['locations'][-1]:
                print(location, end=", ")
            else:
                print(location)

        print("Type: ", ANIMAL_DATA[item_index]['characteristics']['type'])
    except (KeyError, NameError, TypeError):
        print("")

    print("*" * 30)

