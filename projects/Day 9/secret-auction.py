from art import logo

print(logo)
print("Welcome to the secret auction program.")

bid_dict = {}
def new_bid():
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    bid = float(bid)
    bid_dict[name] = bid
    end_check = input("Are there any other bidders? Type 'yes' or 'no'.")
    if end_check == "yes":
        new_bid()
    elif end_check == "no":
        highest_bid = bid
        highest_bidder = name
        for bidder in bid_dict:
            if bid_dict[bidder] > highest_bid:
                highest_bid = bid_dict[bidder]
                highest_bidder = bidder
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
        return

new_bid()