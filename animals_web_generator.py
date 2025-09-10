import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


ANIMAL_DATA = load_data('animals_data.json')


def serialise_animals():
    """Generates required string based off JSON file, returns string.
    If Data missing, inputs empty line"""
    output = ""
    for item in ANIMAL_DATA:
        output += "\n<li class='cards__item'>\n"
        item_index = ANIMAL_DATA.index(item)
        try:
            output += (f"\t<div class='card__title'>"
                       f"{ANIMAL_DATA[item_index]['name'].capitalize()} </div>\n")
            output += "\t\t<div class='card__text'>\n<ul>\n"
            output += (f"\t\t\t<li><strong>Diet: </strong>"
                       f"{ANIMAL_DATA[item_index]['characteristics']['diet'].capitalize()} </li>\n")
            output += (f"\t\t\t<li><strong>Lifespan: </strong>"
                       f"{ANIMAL_DATA[item_index]['characteristics']['lifespan'].capitalize()} </li>\n")
            output += "\t\t\t<li><strong>Location: </strong>"
            for location in ANIMAL_DATA[item_index]['locations']:
                if location != ANIMAL_DATA[item_index]['locations'][-1]:
                    output += location.capitalize() + ", "
                else:
                    output += location.capitalize() + " </li>\n"
            output += (f"\t\t\t<li><strong>Habitat: </strong>"
                       f"{ANIMAL_DATA[item_index]['characteristics']['habitat'].capitalize()} </li>\n")
            output += (f"\t\t\t<li><strong>Type: </strong>"
                       f"{ANIMAL_DATA[item_index]['characteristics']['type'].capitalize()} </li>")
        except (KeyError, NameError, TypeError):
            output += "\t\t\t<br/>\n"
        output += "\t\t\t</ul>\n\t\t</div>\n\t</li>\n"
    return output


def replace_text(filename, replacement_string):
    """replaces placeholder in file with desired string"""
    with open(filename, 'r') as file:
        file_data = file.read()
    file_data = file_data.replace("__REPLACE_ANIMALS_INFO__", replacement_string)
    with open(filename, 'w') as file:
        file.write(file_data)


replace_text('animals_template.html', serialise_animals())
