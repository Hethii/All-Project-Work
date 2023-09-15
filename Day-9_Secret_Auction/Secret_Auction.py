# My Own Code:

# from replit import clear
# from art import logo
# print(logo)
print("Welcome to the secret auction program.")

every_bidders = []


def bidders_details(given_name, given_bid_value):
    """Used for return back every_bidders"""
    new_bidders = {}
    new_bidders["Name"] = given_name
    new_bidders["bid"] = given_bid_value
    every_bidders.append(new_bidders)


is_true = True
while is_true:
    name = input("What is your name?: \n")
    bid_value = int(input("What's your bid?:  $\n"))
    bidders_details(name, bid_value)
    other_bidders = input("Are there any other bidders? \n").lower()

    if other_bidders == 'yes':
        pass
        # this clear function will not work unless this code is used in replit
        # clear()
    else:
        is_true = False

bid_in_list = []
name_in_list = []
for value in every_bidders:
    name_in_list.append(value['Name'])
    bid_in_list.append(value['bid'])

highest_bid = 0
for each_bid in bid_in_list:
    if each_bid > highest_bid:
        highest_bid = each_bid
list_index = bid_in_list.index(highest_bid)
the_name_key = name_in_list[list_index]

print(f"The winner is {the_name_key} with a bid of ${highest_bid}")

# # Instructor [Angela Yu] code:
# from replit import clear
# from art import logo
# print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            # to understand how it works. this easily gets the highest bidder name.
            print(winner)
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    # this is my first mistake. this easily. this takes price as the value of for the name key and append it to the dictionary called bids
    bids[name] = price
    # print(bids)
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        pass
        # this clear function will not work unless this code is used in replit
        # clear()
