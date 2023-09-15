import pandas

#my_code
data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_number = 0
cinnamon_number = 0
black_number = 0
nan = 0
colour_list = data["Primary_Fur_Color"].to_list()
# print(colour_list)
for colour in colour_list:
    if colour == "Gray":
        gray_number += 1
    elif colour == "Cinnamon":
        cinnamon_number += 1
    elif colour == "Black":
        black_number += 1

squirrel_colour_list = {
    "Fur Color": ["Gray", "Red", "Black"],
    # "Count": [gray_number, cinnamon_number, black_number]
}

#Angela's code
# grey_squirrels = len(data[data["Primary_Fur_Color"] == "Gray"])
# cinnamon_squirrels = len(data[data["Primary_Fur_Color"] == "Cinnamon"])
# black_squirrels = len(data[data["Primary_Fur_Color"] == "Black"])
# #
# squirrel_colour_list = {
#     "Fur Color": ["Gray", "Red", "Black"],
#     "Count": [grey_squirrels, cinnamon_squirrels, black_squirrels]
# }


new_data = pandas.DataFrame(squirrel_colour_list)
print(new_data)
# new_data.to_csv("squirrel_count")

