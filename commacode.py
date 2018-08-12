spam = ['apples', 'bananas', 'tofu', 'cats']
i = 0
strAnswer = ""

while i < len(spam):
    
    if i == len(spam) - 1:
        strList = list(strAnswer)
        #strList.remove(strList[len(strList)-1])
        #strAnswer = strList
        strAnswer += ' and ' + spam[i] 
    elif i == len(spam) - 2:
        strAnswer += spam[i]
    else :    
        strAnswer += spam[i] + ', '
    i += 1
    #print(i)

print(strAnswer)

