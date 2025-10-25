n = 1
x = '0'
while int(x, 2) < int((bin(200)[2:]), 2):
    N = bin(n)[2:]
    if n % 3 == 0:
        x = str(N) + (str(N)[-3:])
        n =+ 1
    else:
        x = str(N) + (bin((n % 3) * 3)[2:])
        n += 1
    print(n)
