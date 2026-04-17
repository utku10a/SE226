def calculate_mean(num_list):
    total = 0
    for num in num_list:
        total += num
    return total / len(num_list)

def find_maximum(num_list):
    max_val = num_list[0]
    for num in num_list:
        if num > max_val:
            max_val = num
    return max_val

def find_minimum(num_list):
    min_val = num_list[0]
    for num in num_list:
        if num < min_val:
            min_val = num
    return min_val