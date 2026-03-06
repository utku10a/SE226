while True:
 x = int(input("Give a number greater than 9:"))
 if x > 10:
    break


count = 0
while x >= 10:

 old = x
 sum = 0

 while old > 0:
     rakam = old % 10
     sum = sum + rakam
     old = old // 10

 print(x, "→", sum)
 count+=1
 x = sum

print(f'Last value: {x}')
print(f'Total steps: {count}')










