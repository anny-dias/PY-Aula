#CONTINUE
#interrompe a iteração atual o look e passa para proxima

for n in range(1, 50):
    if n % 10 == 0:
        continue
    print(n, end = "-")
