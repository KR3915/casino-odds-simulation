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
def generate_card():
    values_list = extract_card()
    generated_val = values_list[random.randint(0,len(values_list) - 1)]
    return generated_val
#player turn
def player_turn():
    value = 0
    for i in range(2):
        card = generate_card()
        if card == "A":
            if value + 11 > 21:
                card = "1"
            else:
                card = "11"
        value += int(card)
    for x in range(20):
        if value < 17:
            card = generate_card()
            if card == "A":
                if value + 11 > 21:
                    card = "1"
                else:
                    card = "11"
            value += int(card)
        elif 17 < value <= 21:
            return value
        elif value > 21:
            return 0
    return value  # Fallback návrat
def dealer_turn():
    value = 0
    for x in range(20):
        i = 0
        if value<=17:
            card = generate_card()
            if card == "A":
               if value + 11>21:
                card = "1"
            else:
                card = "11"
            value += int(card)
        elif value > 17 and value <= 21:
            return value
            break
        elif value > 21:
            value = 0
            return value
            break
#game simulation
def game():
    settings = extract_game()
    win = False
    wins = 0
    loses = 0
    for i in range(settings[0]):
        print(dealer_turn())
        push = False
        value_player = player_turn()
        value_dealer = dealer_turn()
        if value_player == 0:
            win = False
        if int(value_player) > int(value_dealer):
            win = True
        elif value_player == value_dealer:
            push = True
        elif int(value_player) < int(value_dealer):
            win = False
        if push == False:
            if win == False:
                loses += 1
            else:
                wins += 1
    print(f"wins: {wins}\nloses:{loses}")

game()   
        

        
        

