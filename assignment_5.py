x= ((2017,"Samuel",("CSCE","Intro to Python")),(8940,"John",("Math","Physics","Biology")))

def function(x, name):
    for i in range(len(x)):
        if name == x[i][1]:
            #print(i)
            return x[i][2]
    return "Error with name"


print(function(x,"Samuel"))

# NEXT QUESTION 
def store(string):
    Dictionary={}
    new_words = string.split()
    Dictionary[new_words[0]] = 0
    for word in new_words:
        count = 1
        dictlist = list(Dictionary.items())
        #print(dictlist)
        for i in range(len(dictlist)):
            #print("loop")
            #print(dictlist[i][0],word,i)
            if word == dictlist[i][0]:
                count = dictlist[i][1] + 1
                Dictionary[word] = count
                count = 1
                #print("same")
                break
            else:
                Dictionary[word] = count
                #print("not same")
    return Dictionary

def printdict(Dictionary):
    print("Word                Count")
    print("=========================")
    dictlist = list(Dictionary.items())
    for i in range(len(dictlist)):
        print(dictlist[i][0],"                ",dictlist[i][1])

string = "new function consist new materials"

Dictionary = store(string)
#print(list(Dictionary.items()))
printdict(Dictionary)