import json
import random
result = ""
with open("settings.json") as file:
    settings = json.load(file)
    card_names = [card for card in settings['cards']]
    print("Card Names:")
    for card in card_names:
        cardvar = "card" + card["name"]
        locals()[cardvar] = (card["name"], card["value"], card["quantity"])
        print (cardA)
        
        

