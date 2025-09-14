from data_fetcher import fetch_data

def get_valid_animal():
    while True:
        user_input = input("Please enter animal: ")
        if len(user_input) == 0:
            print("Error! Names cannot be blank.")
        else:
            break
    return user_input


def serialise_animals(animal):
    """Generates required string based off JSON file, returns string.
    If Data missing, inputs empty line"""
    data = fetch_data(animal)
    if len(data) == 0:
        return f"<li class='cards__item'><h2> No animal '{animal}' found! </h></li>"
    output = ""
    for item in data:
        output += "\n<li class='cards__item'>\n"
        item_index = data.index(item)
        try:
            output += (f"\t<div class='card__title'>"
                       f"{data[item_index]['name'].capitalize()} </div>\n")
            output += "\t\t<div class='card__text'>\n<ul>\n"
            output += (f"\t\t\t<li><strong>Diet: </strong>"
                       f"{data[item_index]['characteristics']['diet'].capitalize()} </li>\n")
            output += (f"\t\t\t<li><strong>Lifespan: </strong>"
                       f"{data[item_index]['characteristics']['lifespan'].capitalize()} </li>\n")
            output += "\t\t\t<li><strong>Location: </strong>"
            for location in data[item_index]['locations']:
                if location != data[item_index]['locations'][-1]:
                    output += location.capitalize() + ", "
                else:
                    output += location.capitalize() + " </li>\n"
            output += (f"\t\t\t<li><strong>Habitat: </strong>"
                       f"{data[item_index]['characteristics']['habitat'].capitalize()} </li>\n")
            output += (f"\t\t\t<li><strong>Type: </strong>"
                       f"{data[item_index]['characteristics']['type'].capitalize()} </li>")
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


