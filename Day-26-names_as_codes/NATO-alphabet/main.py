import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

user_input = input("Enter a word: ").upper()
# user_name_list = list(user_input)

# print(phonetic_dict["A"])
coded_names = [phonetic_dict[letter] for letter in user_input]

# coded_names = []
# for letter in user_name_list:
#     for key, value in phonetic_dict.items():
#         if letter == key:
#             coded_names.append(value)
#

print(coded_names)
