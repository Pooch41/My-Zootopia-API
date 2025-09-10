import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


ANIMAL_DATA = load_data('animals_data.json')


def generate_output():
    """Generates required string based off JSON file, returns string.
    If Data missing, inputs empty line"""
    output = ""
    for item in ANIMAL_DATA:
        item_index = ANIMAL_DATA.index(item)
        try:
            output += "Name: " + ANIMAL_DATA[item_index]['name'] + "\n"
            output += "Diet: " + ANIMAL_DATA[item_index]['characteristics']['diet'] + "\n"
            output += "Location: "
            for location in ANIMAL_DATA[item_index]['locations']:
                if location != ANIMAL_DATA[item_index]['locations'][-1]:
                    output += location + ", "
                else:
                    output += location + "\n"
            output += ("Type: ", ANIMAL_DATA[item_index]['characteristics']['type'], "\n")
        except (KeyError, NameError, TypeError):
            output += "\n"
    return output


def replace_text(filename, replacement_string):
    """replaces placeholder in file with desired string"""
    with open(filename, 'r') as file:
        file_data = file.read()
    file_data = file_data.replace("__REPLACE_ANIMALS_INFO__", replacement_string)
    with open(filename, 'w') as file:
        file.write(file_data)


replace_text('animals_template.html', generate_output())
