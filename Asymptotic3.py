def test(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*")
            iteration+=1
        print("")
    print("\nwhen n is",n,"iteration =",iteration)
test(5)
test(4)
test(3)
