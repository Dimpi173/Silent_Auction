import os

'''In this program the other person dose not see the bid amount.'''
'''We can only see the final bidder amount.'''
print("******* Welcome to The Silent Auction Program ********")
bidder_info = {}
while True:
    bidder_info.update({
      input("What is your name? "): int(input("What is your bid? ")),
    })
    option = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if option == "yes":
        os.system('cls')
        continue
    elif option == "no":
        break
    else:
        print("Invalid Entry")
        break
max_bid = 0
max_bidder = ""
for bid in bidder_info:  
    if bidder_info[bid] > max_bid:
        max_bid = bidder_info[bid]
        max_bidder = bid
        
print(f"The winner is {max_bidder} with a bid of {max_bid}")
