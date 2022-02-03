import random

def getRandomNumber():
    number = random.randint(1,45)
    return(number)

def getlotto():
    tmp = list()
    count = 0

    while True:
        if count ==6:
            break
        random_num = getRandomNumber()
        if random_num not in tmp:
            tmp.append(random_num)
            count +=1
        tmp.sort()

    for i in tmp:
        print(i, end=' ')


getlotto()