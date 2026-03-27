n = int(input("Enter number of users: "))

users = {}

for i in range(n):
    username = input("Enter username: ")
    count = int(input("How many items? "))

    items = []

    for j in range(count):
        item = input("Item " + str(j + 1) + ": ")
        items.append(item)

    users[username] = items

print("\nUSER DATA:")
for user in users:
    print(user + " -> " + str(users[user]))

item_count = {}

for user in users:
    unique_items = set(users[user]) # HER KULLANICIDA KOPYA ELE 

    for item in unique_items:
        if item in item_count:
            item_count[item] += 1 # ITEM COUNTTA VARSA 1 EKLE
        else:
            item_count[item] = 1 # ITEMLE İLK DEFA KARŞILAŞILIYOR 1 YAP

print("\nCOMMON ITEMS:")
for item in item_count:
    if item_count[item] > 1:
        print(item) 
      
print("\nUNIQUE ITEMS:")
for item in item_count:
    if item_count[item] == 1: # ITEM SADECE 1 KEZ GÖRÜLDÜ 1 E SABİTLENDİ ARTTIRILMADIYSA UNIQUEDIR
        print(item)

max_count = max(item_count.values())

print("\nMOST POPULAR ITEM:")
for item in item_count:
    if item_count[item] == max_count:
        print(item)
