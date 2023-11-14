from random import randint
numbers = []
for i in range(20):
    numbers.append(randint(215, 218))
#print(numbers)
tapoc = []
for tipoc in numbers:
    if tipoc//2:
        tapoc.append(tipoc)
    elif tipoc == 217:
        print(tapoc)
        raise SystemExit()
        print(tapoc)
print(tapoc)
    
