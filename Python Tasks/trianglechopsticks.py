n = int(input())

def triangleChecker():
    abr = [int(x) for x in input().split()]
    a,b,r = abr[0],abr[1],abr[2]
    l = int(input())
    jar = [int(x) for x in input().split()]
    if len(jar)>l:
        for i in range(len(jar)-l):
            jar.pop()
    elif len(jar)<l:
        print("The length of the jar is too short")

    if l>r:
        counter = 0
        for i in range(l):
            if a + b > jar[i] and a + jar[i] > b and b + jar[i] > a:
                counter += 1
        else:
            pass
    else:
        print("The length of the jar cannot be lesser than the random number")

    win = ""
    if counter>r:
        win = "Nastu"
    else:
        win = "Grey"
    return counter, win

if __name__ == "__main__":
    for i in range(n):
        triangeNo, win = triangleChecker()
        print(triangeNo)
        print(win)
