def power8(number):
    if number <=0:
        return False
    return(number & (number - 1)) ==0 and(number % 7 == 1)

n = int(input("Enter a number: "))
if power8(n):
    print("\nThe number is a power of 8")
else:
    print("\nThe number is not a power of 8")