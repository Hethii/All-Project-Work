# # general code: new_list = [new_item for item in list if test]

# # adds 1 to each number in the list and produce a new list
# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
#
# # takes each alphabet to make a new list
# name = "Avia"
# new_list = [letter for letter in name]
#
# # multiplies each number in a range by 2
# new_number = [n * 2 for n in range(1, 5)]
#
# # returns the list of 4-letter word and capitalized 0ver 5-letter words
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_list_1 = [name for name in names if len(name) < 4]
# new_list_2 = [name.upper() for name in names if len(name) > 4]
#
# # Exercise 1 : square each item in the list
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number ** 2 for number in numbers]
# # print(squared_numbers)
#
# # Exercise 2: returns a list of only even numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [even_number for even_number in numbers if even_number % 2 == 0]
# # print(result)


# with open("file1.txt") as data:
#     content = data.readlines()
#
# with open("file2.txt") as data2:
#     content2 = data2.readlines()
# # this is not needed as "int" alone will convert all to integers and erase non-integers
# # new_list1 = [new_num.strip() for new_num in content]
# # new_list2 = [new_num1.strip() for new_num1 in content2]
#
#
# result1 = [int(final_list) for final_list in content2 if final_list in content]
# print(result1)

# using dictionary comprehension
# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# students_scores = {student: random.randint(1, 100) for student in names}
#
# passed_students = {student: score for (student, score) in students_scores.items() if score > 30}
# print(passed_students)

# Exercise 3: turning list to dictionary
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

# Exercise 4: turning temperature in a dict from C to F
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day: (value * 9/5 + 32) for (day, value) in weather_c.items()}
#
# print(weather_f)


# using panda to get value easily
import pandas
student_dict = {
    "student": ["Ezer", "Olamide", "Avia"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#loop through rows of a dataframe
for (index, row) in student_data_frame.iterrows():
    # print(row.score)
    if row.student == "Ezer":
        print(row.score)
