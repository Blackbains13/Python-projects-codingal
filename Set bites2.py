def setOrNot(number, n):
    if number & (1 << n):
        print("SET")
    else:
        print("NOT SET")


number = int(input("Enter the number:"))
n = int(input("Enter the bit position"))

setOrNot(number, n)