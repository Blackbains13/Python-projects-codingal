def get_factors(number):
    factors = []
    for i in range(1, number +1):
        if number % i == 0: 
            factors.append(i)
    return factors


try:
    num = int(input("Enter a number: "))
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        print("The factors of",num,"are:",{get_factors},num,)
except ValueError:
    print("Invalid input! Please enter an integer")