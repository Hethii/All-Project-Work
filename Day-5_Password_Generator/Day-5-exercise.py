# # 1 calculate average height of students
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# total_number_of_student = 0
# sum_of_students = 0
# for student_average in student_heights:
#     total_number_of_student +=1
#     sum_of_students += student_average
#     average = sum_of_students / total_number_of_student
# print(round(average))

# # 2 to get highest score without usin max() or min

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for max_number in student_scores:
#     if max_number > highest_score:
#         highest_score = max_number
# print(f"The highest score in the class is: {highest_score}")

# # 3 Add up even numbers between 0, 100
# # 3a

# sum_even_numbers = 0
# for even_numbers in range(2, 101, 2):
#     sum_even_numbers += even_numbers
# print(sum_even_numbers) 

# # 3b 

# total1 = 0
# for numbers in range(1,101):
#     if numbers % 2 == 0:
#         total1 += numbers
# print(total1)

# 4 creat FizzBuzz


for numbers in range(1, 101):
    if numbers% 3 == 0 and numbers % 5 == 0:
        print('FizzBuzz')
    elif numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)