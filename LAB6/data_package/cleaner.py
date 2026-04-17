def remove_duplicates(data_list):
    unique = []
    for item in data_list:
        if item not in unique:#data listte olup unique in içinde yoksa ekle
            unique.append(item)
    return unique

def strip_whitespaces(string_list):
    cleaned = []
    for item in string_list:
        cleaned.append(item.strip())
    return cleaned
