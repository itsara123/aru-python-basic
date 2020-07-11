def grade_cal(score):
    n = score
    n = int(n)
    if (n >= 80 and n <= 100):
        return 'A'
    elif (n >= 75 and n < 85):
        return 'B+'
    elif (n >= 70 and n < 75):
        return 'B'
    elif (n >= 65 and n < 70):
        return 'C+'
    elif (n >= 60 and n < 65):
        return 'C'
    elif (n >= 55 and n < 60):
        return 'D+'
    elif (n >= 50 and n < 55):
        return 'D'
    elif (n >= 0 and n < 50):
        return 'F'
    else:
        return 'invalid score'

for i in range(3):
    result = grade_cal(input())
    print(result)
