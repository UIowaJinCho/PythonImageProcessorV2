from Helpers.PromptColor import *
import re

"""
It allows user to choose 1 option from the prompt.

2022.12.22  Originally created  Hyunjin Cho
"""

def PromptInputMessage(question,list):
    
    #Prompt the user with the question
    print(StringInBlue(question))
    
    #List the options
    for i, option in enumerate(list, start=1):
        print(StringInBlue("%i:%s"%(i,option)))
    
    try:
        Input = int(input())
        #Return the proper output.
        if Input < 0:
            return list[Input]
        else:
            return list[Input-1]
    except Exception:
        raise Exception(StringInRed("Invalid selection"))


"""
It allows user to choose multiple options from the prompt.

2022.12.22  Originally created  Hyunjin Cho
"""
def PromptFilterInputMessage(question,list):
    
    #(user can insert commas or whitespace to select multiple filters)
    #such as 1 2 3 4 or 1,2,3,4 (however I dont think I implemented for mixed scenario 1,2 3 4 will not act properly)
    #((\d+,)+\d+)|((\d+ )+\d+)| 
    
    #(user can insert 1-4 and run for 1,2,3,4 filters)
    #\d+-\d+ range 

    #Prompt the user with the question
    print(StringInBlue(question))
    
    #List the options
    for i, option in enumerate(list, start=1):
        print(StringInBlue("%i:%s"%(i,option)))
    
    #Return the proper output.
    try:
        UserInput = input()
        if(re.match('\d+-\d+',UserInput)):
            tokens = UserInput.split('-')
            print(tokens)
            return list[int(tokens[0])-1:int(tokens[1])]
        elif(re.match('((\d+,)+\d+)',UserInput)):
            tokens = UserInput.split(',')
            print(tokens)
            filterList = []
            for token in tokens:
                filterList.append(list[int(token)-1])
            return filterList
        elif(re.match('((\d+ )+\d+)',UserInput)):
            tokens = UserInput.split(' ')
            print(tokens)
            filterList = []
            for token in tokens:
                filterList.append(list[int(token)-1])
            return filterList
        else:
            return [list[int(UserInput)-1]]
    except Exception:
        raise Exception(StringInRed("Invalid selection"))

