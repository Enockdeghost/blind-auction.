import subprocess
import platform
import os 

#auto clear
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        subprocess.call("clear")
bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is Your Name?: ")
    # hakuna kueka ujinga
    while True:
        try:
            price = float(input("What is Amount You want to Bid? Tsh "))
            if price <= 0:
                print("Please enter a positive amount!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")
    
    bids[name] = price
    finish_status = input("Are there other bidders? 'yes' or 'no': ").lower().strip()
    
    if finish_status == "no":
        bidding_finished = True
    elif finish_status == 'yes':
        clear_screen()
    else:
        print('please answer yes/ no')
        
def find_highest_bidder(bidding_record):
    if not bidding_record:  # Check kama dictionaryni tupu
        print("No bids were placed!")
        return
    
    highest_amount = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder
    
    print(f"Highest bidder is {winner} with bid of Tsh {highest_amount}")

find_highest_bidder(bids)

