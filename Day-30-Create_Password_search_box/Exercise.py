# try:
#     """to try a code that could generate error"""
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     """to catch the particular error and run this code instead"""
#     file = open("a_file.txt", "w")
#     file.write("Hello")
# except KeyError as error_message:
#     """to catch the particular error and run this code instead"""
#     print(f"The key {error_message} does not exist.")
# else:
#     """if 'try' actually goes through, then else follows it"""
#     content = file.read()
#     print(content)
# finally:
#     """to end it all as long as no error and raise is used for making up errors"""
#     file.close()
#     print("File was closed.")
#     raise TypeError("This is an error that I made up")

#
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)

# Exercise
# 1
# fruits = ["Apple", "Pear", "Orange"]
#
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)

# 2
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
#
#
# print(total_likes)


# Last
import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

# is_correct = True
# while is_correct:
#     try:
#         user_input = input("Enter a word: ").upper()
#         coded_names = [phonetic_dict[letter] for letter in user_input]
#         print(coded_names)
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")
#     else:
#         is_correct = False


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        coded_names = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(coded_names)


generate_phonetic()