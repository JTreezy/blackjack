from art import logo
import random 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []

hit_me = random.choice(cards)

should_stop = False
bust = False

def add(n1,n2):
    return n1 + n2

def score_check():
    if score > 21: 
        print("You went over. You lose")
    elif final_computer_score > 21:
        print("You win")
    elif 21 > score > final_computer_score:
        print("You win")
    elif 21 > final_computer_score > score:
        print("You lose")
        
def bust_check():
    if score > 21:
        bust == True
        print(f"Your final hand: {your_cards}, final score: {score}\nComputer's final hand: {computer_cards}, final score: {final_computer_score}")
        print("You went over. You lose")
    if final_computer_score > 21:
        print(f"Your final hand: {your_cards}, final score: {score}\nComputer's final hand: {computer_cards}, final score: {final_computer_score}")
        print("Your opponent went over. You win")

your_cards.append(hit_me)
computer_cards.append(hit_me)

computer_hand = [computer_cards[0]]
print(logo)
while should_stop != True:
    score = add(sum(your_cards), your_cards[0])
    final_computer_score = add(sum(computer_cards),computer_cards[0])
    
        
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == "n":
        score_check()
        if score == final_computer_score:
           print(f"Your final hand: {your_cards}, final score: {score}\nComputer's final hand: {computer_cards}, final score: {final_computer_score}")
           print("Draw") 
    elif choice == 'n':
        print(f"Your final hand: {your_cards}, final score: {score}\nComputer's final hand: {computer_cards}, final score: {final_computer_score}")
        score_check()
        should_stop = True   
    elif choice == 'y':      
        your_cards.append(hit_me)
        computer_cards.append(hit_me)   
        
        score_check()
        bust_check()

        print(f"Your cards: {your_cards}, current score: {score}\nComputer's first hand: {computer_hand}")
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            
        score_check()
        bust_check()        
  