import math

def log_puzzle(base, number):
    times = math.log(number) / math.log(base)
    print("How many times do we multiply",base,"with itself to get",number,"?")
    print("Answer : {base}^ {times:.2f} = {number}")


log_puzzle(2, 32)
log_puzzle(10, 1000)
log_puzzle(3, 81)
log_puzzle(2, 64)