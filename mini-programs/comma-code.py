# function returns string of list variables seperated by commas,
# and with "and" before the last variable
def function(listArgument):
    retString = ""
    for i in range(len(listArgument)-1):
        retString += (str(listArgument[i]) + ', ')

    retString += str(' and ' + listArgument[-1] + '.')
    return retString

# main
spam = ['apples', 'bananas' , 'tofu', 'cats']
print(str(function(spam)))
