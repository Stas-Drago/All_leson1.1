from collections import defaultdict
test_list = ['gfg is best for geeks','geeks love gfg','gfg is the bestoc']
print("Оригинальный лист: "+ str(test_list))
temp = defaultdict(int)

for sub in test_list:
    for wrd in sub.split():
        temp[wrd] += 1
        if 'gfg'> wrd:
            tor = wrd
res = max(temp, key=temp.get)
print('World with maximum frequency: '+ str(res),'\nСамое длинное слово, это: '+ str(tor))