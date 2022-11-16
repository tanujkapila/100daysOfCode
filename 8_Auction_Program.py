from replit import clear
from art import logo
clear()
#HINT: You can call clear() to clear the output in the console.
print(logo)
auction_dict={99:'Tanuj',109: 'Tanya' , 1010:'Neena', 1100:'Sanjeev' }

still_want_to_bid = True

while still_want_to_bid:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: "))
  auction_dict[bid]=name

  continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.")
  if continue_bid == 'no':
    still_want_to_bid = False
    maximum_bid = max(auction_dict)
    maximum_bidder = auction_dict[maximum_bid]
    # print(auction_dict)
    # print(maximum_bid)
    # print(maximum_bidder)
    print(f"The winner is {maximum_bidder} with a bid of ${maximum_bid}")
  else:
    clear()
  
