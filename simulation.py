import json
import random
result = ""
settings = []
#extracts game settings from JSON file
def extract_game():
    bet = 0
    turns = 0
    balance = 0
    stand = 0
    with open("settings.json") as f:
        settings = json.load(f)
        for game in settings["games"]:
                turns = game["turns"]
                bet = game["bet"]
                balance = game["balance"]
                stand = game["stand at"]
    return (turns,bet,balance,stand)      

#extracts card data from the JSON file
def extract_card():
    values_all = []
    temp_var = ""
    stringval = ""
    with open("settings.json") as file:
        settings = json.load(file)
        card_names = [card for card in settings["cards"]]
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
def extract_card():
    values_list = extract_card+()
    generated_val = values_list[random.randint(0,len(values_list) - 1)]
    print (generated_val)
game = extract_game()
print(game)
        
        

