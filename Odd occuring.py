def Oddoccuring(arr):
    res = 0
    for element in arr:
        res = res^element
    return res

arr = []
n = int(input("Enter array size:"))
while(n):
    num = int(input("Enter the number:"))
    arr.append(num)
    n-=1

print("OddOccuring number is",Oddoccuring(arr))