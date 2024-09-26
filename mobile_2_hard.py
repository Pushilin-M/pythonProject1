import random

list_ = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n = random.choice(list_)
parol = []
for i in range(1,20):
    for j in range(1, 20):
        para = []
        if i == j:
            continue
        elif n % (i + j) != 0:
            continue
        else:
            n % (i + j) == 0
            npar = [j, i]
        para.append(i), para.append(j)
        if npar not in parol:
           parol.append(para)
print('число - ', n)
print('пароль - ', *parol)



