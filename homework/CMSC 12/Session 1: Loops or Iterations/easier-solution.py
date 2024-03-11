

n = int(input("Value of n: "))

# do the thing
for i in range(n):
    for j in range(i+1):
        print(f"{j+1} ", end='')
    print("")

