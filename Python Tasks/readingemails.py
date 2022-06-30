

def reademail(email):
    splitEmail = email.split("@", 1)
    temp = splitEmail[1].split(".", 1)
    splitEmail.pop()
    splitEmail.extend(temp)

    #local
    acceptableRange = []
    acceptableRangeL = [x for x in range(97, 127)]
    acceptableRangeU = [x for x in range(65, 91)]
    compensation = [94,95]
    acceptableRange.extend(acceptableRangeU)
    acceptableRange.extend(compensation)
    acceptableRange.extend(acceptableRangeL)

    aRangeD = acceptableRange.copy()
    aRangeD.pop()
    aRangeD.pop()
    aRangeD.pop()
    aRangeD.pop()

    #print(acceptableRange)
    _local = splitEmail[0]
    for i in range(len(_local)):
        if ord(_local[i]) not in acceptableRange:
            return False
        elif _local.startswith(".")==True or _local.endswith(".")==True:
            return False
        else:
            pass
            
    
    domain = splitEmail[1]
    for i in range(len(domain)):
        if ord(domain[i]) not in aRangeD:
            return False
        elif domain[0]=="-" or domain[-1]=="-":
            pass
        else:
            pass
    
    extension = splitEmail[2]
    if len(extension)>3:
        return False
    for i in range(len(extension)):
        if ord(extension[i]) not in aRangeD:
            return False
        else:
            pass
        
    return True
        


if __name__ == "__main__":
    exampleEmail = input()
    if len(exampleEmail)>64:
        print("The email is too long")
    else:
        print(reademail(exampleEmail))