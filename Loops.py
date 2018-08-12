import random
i = 10
while i <= 20:
    print(i)
    i = random.randint(1,30)
    if i == 18:
        break
    i += 1

for i in range(5,40,3):
    print(i*2)
    
