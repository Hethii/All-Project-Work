# # 1 for choosing Heads or Tails using random module and conditional statement
# import random
# #Write the rest of your code below this line 👇
# random_H_T = random.randint(0,1)

# if random_H_T == 0:
#     print("Tails")
# else:
#     print("Heads")


# #  2 to choose a payee amidst friends gatherings
# import random
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# random.number = random.randint(0, len(names) - 1)
# payee= names[random.number]
# print(f"{payee} is going to buy the meal today!")

# 3 for making X on a treasure map
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# x= (int(position[0])) - 1
# y= (int(position[1])) - 1
# map[y][x]='X'


# print(f"{row1}\n{row2}\n{row3}")