import json
import random
result = ""
settings = []
def extract_value():
    values_all = []
    temp_var = ""
    stringval = ""
    with open("settings.json") as file:
        settings = json.load(file)
        card_names = [card for card in settings['cards']]
        print("Card Names:")
        for card in card_names:
            cardvar = "card" + card["name"]
            locals()[cardvar] = (card["name"], card["value"], card["quantity"])
            for i in range(card["quantity"]):
                for char in str(card["value"]):
                    temp_var += char
                values_all.append(temp_var)
                temp_var = ""
        return values_all
#random vlaue
values_list = extract_value()
print(values_list)
def generate_value():
    values_list = extract_value

        
        

