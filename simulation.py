import json
import random
import math
result = ""
settings = []
f = open('log.txt', 'r+')
f.truncate(0)
#extracts game settings from JSON file
def config():
    char = input("press C for config menu, press any other key for simulation\n")
    
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
                values_all.append(str(card["value"]))
                values_all.append(str(card["name"]))
                temp_var = ""
        return values_all
#random vlaue
def generate_card():
    values_list = extract_card()
    values_list_val = values_list[::2]
    values_list_name = values_list[1::2]
    generated_val = values_list_val[random.randint(0,len(values_list_val) - 1)]
    generated_card = values_list[values_list.index(generated_val) + 1]
    return generated_val, generated_card
#player turn
def player_turn():
    cards_all = ""
    value = 0
    cards_all = ""
    for i in range(2):
        generated_card = generate_card()
        card_name = generated_card[1]
        card = int(generated_card[0])
        cards_all += card_name
        if card == "A":
            if value + 11 > 21:
                card = "1"
            else:
                card = "11"
        value += int(card)
    for x in range(20):
        if value < 17:
            generated_card = generate_card()
            card_name = generated_card[1]
            card = int(generated_card[0])
            cards_all += card_name
            if card == "A":
                if value + 11 > 21:
                    card = "1"
                else:
                    card = "11"
            value += int(card)
        elif 17 < value <= 21:
            return value, cards_all
        elif value > 21:
            return 0, cards_all
    return value,card  # Fallback návrat
def dealer_turn():
    cards_all = ""
    value = 0
    for x in range(20):
        if value < 17:
            generated_card = generate_card()
            card_name = generated_card[1]
            card = int(generated_card[0])
            cards_all += card_name + " "
            if card == "A":
                if value + 11 > 21:
                    card = "1"
                else:
                    card = "11"
            value += int(card)
        elif 17 <= value <= 21:
            return value, cards_all
        elif value > 21:
            return 0, cards_all
#game simulation
def game():
    settings = extract_game()
    cards_player = ""
    cards_dealer = ""
    win = False
    draws = 1
    wins = 0
    bet = settings[1]
    loses = 0
    i = 0
    balance = settings[2]
    game_number = 0
    while balance > 0 and i < settings[0]:
        game_number += 1
        i += 1
        push = False
        value_player = 0
        player = player_turn()
        dealer = dealer_turn()
        print()
        value_player = int(player[0])
        cards_player = player[1]
        value_dealer = dealer[0]
        cards_dealer = dealer[1]
        with open("log.txt", "a") as f:
            print(f"GAME:{game_number}\n    player cards:{cards_player}\n    player value:{value_player}\n   dealer cards: {cards_dealer}\ndealer vallue: {value_dealer}", file=f)
        print(f"\nGAME:{game_number}")
        print(f"player value:{value_player}\nplayers cards: {cards_player}\ndealer cards: {cards_dealer}\ndealer vallue: {value_dealer}")
        if value_player == 0:
            win = False
        if int(value_player) > int(value_dealer):
            win = True
        elif value_player == value_dealer:
            push = True
            draws += 1
            print("\nresult: DRAW\n...................................................................")
        elif int(value_player) < int(value_dealer):
            win = False
            balance = balance - bet
        if push == False:
            if win == False:
                loses += 1
                print("\nresult: LOSS\n...................................................................")
            else:
                balance += bet
                wins += 1
                print("\nresult: WIN\n...................................................................")
    #calculate winrate
    games = int(wins)+int(loses)+int(draws)
    winrate = wins/games
    winrate = math.floor(winrate * 100) / 100
    winrate = winrate * 100
    if balance > 0:
        print(f"---------------------------------------------------------------\nwinrate: {winrate}%\nwins: {wins}\nloses:{loses}\ndraws: {draws}\nbalance:{balance}\n---------------------------------------------------------------")
    else:
        print(f"---------------------------------------------------------------\nBalance ran out\nwinrate: {winrate}%\ngames played: {str(games)}\nnwins: {wins}\nloses:{loses}\ndraws: {draws}\n---------------------------------------------------------------")

game()   
        

        
        

   

        
        

