while True:
 x = int(input("Give a number between 3 and 9:"))
 if x < 3 or x > 9:
    print('Invalid input. Please enter a number between 3 and 9')
    continue
 break

old = 0

while old <= x:

    for y in range(1, old +1, 1):
        print(y)
    
    old += 1