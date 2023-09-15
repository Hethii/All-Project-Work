# my code.
with open("./Input/Names/invited_names.txt") as data:
    content = []
    for each_content in data.readlines():
        content.append(each_content.strip("\n"))

with open("./Input/Letters/starting_letter.txt") as letter:
    result = letter.read()
    for each_name in content:
        with open(f"./Output/ReadyToSend/Letter_for_{each_name}.txt", mode="w") as final_letter:
            completed_letter = result.replace("[name]", f"{each_name}")
            final_letter.write(completed_letter)


# Angela's code but tweaked by me.
with open("./Input/Names/invited_names.txt") as data:
    each_content = data.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    result = letter.read()
    for each_name in each_content:
        name = each_name.strip()
        completed_letter = result.replace("[name]", f"{name}")
        with open(f"./Output/ReadyToSend/Letter_for_{name}.txt", mode="w") as final_letter:
            final_letter.write(completed_letter)
