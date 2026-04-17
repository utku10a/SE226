from data_package import *

user_input = input("Enter a comma separated list of numbers: ")

parts = user_input.split(",")

cleaned = strip_whitespaces(parts)

numbers = []
valid = True

for item in cleaned:
    if item.replace("-", "").replace(".", "").isdigit():
        numbers.append(int(item))
    else:
        valid = False

if valid == False:    print("Data Error: Please make sure you only enter numbers separated by commas.")
else:
    unique_numbers = remove_duplicates(numbers)
    mean_value = calculate_mean(list(map(lambda x: float(x), unique_numbers)))#mean ondalıklı gelebileceği için lambda ile float çeviriyoruz

    print("Cleaned and unique data:", unique_numbers)
    print("--------------------")
    print("Mean:", mean_value)
    print("Maximum:", find_maximum(unique_numbers))
    print("Minimum:", find_minimum(unique_numbers))