'''
Created on 16-Apr-2020

@author: ila roy
'''
#DSA-Tryout
import random
def generate_cards_per_type(card_type):
    #Remove pass and write your logic here
    card_list=[]
    if card_type=="C":
        for i in range(2,11):
            card_list.append("C"+str(i))
        for i in ("J","Q","K","A"):
            card_list.append("C"+i)
    if card_type=="D":
        for i in range(2,11):
            card_list.append("D"+str(i))
        for i in ("J","Q","K","A"):
            card_list.append("D"+i)
    if card_type=="H":
        for i in range(2,11):
            card_list.append("H"+str(i))
        for i in ("J","Q","K","A"):
            card_list.append("H"+i)
    if card_type=="S":
        for i in range(2,11):
            card_list.append("S"+str(i))
        for i in ("J","Q","K","A"):
            card_list.append("S"+i)
    return card_list

def generate_card_deck():
    #Remove pass and write your logic here
    card_deck=[]
    card_deck+=generate_cards_per_type("C")+generate_cards_per_type("D")+generate_cards_per_type("H")+generate_cards_per_type("S")
    return card_deck
    
def shuffle_card_deck(cards_list):
    #Remove pass and write your logic here
    n=len(cards_list)
    mid=n//2
    for j in range(0,n):
        index1=random.randrange(0,mid)
        index2=random.randrange(mid,n)
        num1=cards_list[index1]
        cards_list[index1]=cards_list[index2]
        cards_list[index2]=num1
    return cards_list

def sort_cards_of_each_player(card_list):
    #Remove pass and write your logic here
    x=sorted(card_list[0:])
    return x
    
def allocate_cards_to_players(cards_list):
    dict_players={"player1":[],"player2":[],"player3":[],"player4":[]}
    for i,j in enumerate(cards_list):
        dict_players["player"+str((i%4)+1)].append(j)
    return dict_players

def prepare_cards():
    #Remove pass and write your logic here
    cards_list=generate_card_deck()
    shuffle_card_deck(cards_list)
    dict_players=allocate_cards_to_players(cards_list)
    for i in range(1,5):
        dict_players["player"+str(i)]=sort_cards_of_each_player(dict_players["player"+str(i)])
    for i in range(1,5):
        if "CA" in dict_players["player"+str(i)]:
            return 'player'+str(i)

first_player=prepare_cards()
print("The first player is:",first_player)