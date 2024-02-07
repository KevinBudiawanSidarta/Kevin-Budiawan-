n = int(input("Masukan tinggi segitiga pascal : "))
for i in range(n+1):
    for j in range(n-i):
        print(" ", end="")
        c = 1
        for k in range(i + 1):
            print(c, end=" ")
            c = c * (i-k) / (k+1)
            print()
            