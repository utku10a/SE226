def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

term = lambda x2 , i: (x2 ** (2 * i) / factorial(2*i))


def exp_x(x, n):

    all = 0
    for i in range (n):

        all += term(x, i) * ((-1) ** i)


    print({all})


x_ipt = int(input("Enter the value of X: "))
n_ipt = int(input("Enter the value of N: "))

exp_x(x_ipt, n_ipt)


some = 0
def recursiveGeometric(n,r):

    global some
    if n<0 :
        return
    some += r**n
    recursiveGeometric(n-1, r)

#global "some" veriable changes(increases) inside the function . stops when n is lower than zero.
#if n is lower than zero at the beginning , the function stops and returns 0 instantly
# if r is lower than zero function doesn't stop and runs with given r value

#recursiveGeometric(3,2)
print(some)




