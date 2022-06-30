
def asciiequate(string):
    string = string.split()
    ascii = 0
    ASC = []
    for i in range(len(string)):
        for j in range(len(string[i])):
            ascii += ord(string[i][j])
            j += 1
        ASC.append(ascii)
        ascii = 0
    
    if ASC[0] == ASC[1]:
       return True
    else:
        return False

if __name__ == "__main__":
    string = input()
    print(asciiequate(string))

