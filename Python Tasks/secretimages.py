images = [x for x in input().split()]
print((images))

def extensionNo():
    #extension = []
    extpng = 0
    extbmp = 0
    extjpg = 0

    for i in range(len(images)):
        if images[i].endswith(".png"):
            extpng += 1
        elif images[i].endswith(".bmp"):
            extbmp += 1
        elif images[i].endswith(".jpeg"):
            extjpg += 1
    
    return extpng, extbmp, extjpg

if __name__ == "__main__":
    print(*extensionNo())
