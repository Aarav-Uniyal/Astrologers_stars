n = int(input("Enter the number of rows you want in your pattern.\n"))
a = int(input("Enter 1 for erect pattern or 0 for reversed pattern.\n"))
b = bool(a)

if b == True:
    i = 0
    while (i < n):
        i = i + 1
        print ("*"*i)
elif b == False:
    while (True):
        n = n - 1
        print ("*"*(n+1))
        if n == 0:
            break 


