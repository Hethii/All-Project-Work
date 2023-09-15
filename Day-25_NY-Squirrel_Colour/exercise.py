# with open("weather_data.csv") as data_line:
#     data = data_line.readlines()

#
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)


import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
temp_list = data["temp"].to_list()
print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print(f"Average: {average} ")

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.temp.max())


# to get the rows in a particular line:
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp = int(monday.temp)
# convert = (monday_temp * 1.8) + 32
# print(f"fahrenheit: {convert}")


# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_name")