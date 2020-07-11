n = input()
n = int(n)
if (n >= 80 and n <= 100):
    print('A')
elif (n >= 75 and n < 85):
    print('B+')
elif (n >= 70 and n < 75):
    print('B')
elif (n >= 65 and n < 70):
    print('C+')
elif (n >= 60 and n < 65):
    print('C')
elif (n >= 55 and n < 60):
    print('D+')
elif (n >= 50 and n < 55):
    print('D')
elif (n >= 0 and n < 50):
    print('F')
else:
    print('Invalid score')

