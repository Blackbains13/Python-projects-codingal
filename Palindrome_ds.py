
number = int (input("Enter your number: "))

original_number = number
reversed_number = 0

# Reverse the number
while number > 0:
    digit=number %10
    reversed_number = reversed_number * 10 + digit
    number//=10

if original_number == reversed_number:
    print("It is a Palindrome")
else:
    print("It is not a palindrome")