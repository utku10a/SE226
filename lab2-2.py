while True:
 x = int(input("Give a number between 10 and 100:"))
 if x < 10 or x > 100:
    print('Invalid input. Please enter a number between 10 and 100')
    continue
 break

for n in range(1, x + 1, 1):
    if n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
         print(n)


