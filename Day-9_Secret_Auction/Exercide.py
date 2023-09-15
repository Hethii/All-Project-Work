# 1 Student grading using dictionary
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}



# for key in student_scores:
#     if student_scores[key] >= 91:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] >= 81:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] >= 71:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"

# print(student_grades)

# 2 adding new dictionary called add_new_dictionary to a list. the new dictionary has a str, int and a list inside.
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_name, total_visits, the_cities):
        new_country = {}
        new_country["country"] =country_name
        new_country["visits"] =total_visits
        new_country["cities"] =the_cities
        travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)