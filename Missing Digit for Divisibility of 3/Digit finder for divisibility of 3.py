def printnum():
    num = int(input("Enter the number"))
    total = 0
    n = num
    while n != 0:
        total = total + (n % 10)
        n = n // 10
    for i in range(0, 10):
        div = total + i
        if div % 3 == 0:
            print(f"The digit can be {i}")


while True:
    printnum()
    rep = input("Repeat again?(y/n)")
    if rep.lower() == "y":
        continue
    else:
        exit()