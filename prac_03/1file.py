def display1():

    name = input("enter the file name: ")

    f = open(name,"r",encoding="utf-8")

    while True:

        line = f.readline()

        if not line:

            break

        if line[0] == '#':

            print(line)

def display2():

    name = input("enter the file name: ")

    with open(name,"w") as f:

        f.write(name)

    print("done")

def display3():
    name = {"mike", "bob", "joe"}
    for n in name:
        with open(f"{n}.txt", "w") as f:
            f.write(f"{n}\n")
        print("ok")
    print("done")

def display4():
    with open("1.txt", "r") as f:
        while True:
            word1 = f.readline()
            word2 = f.readline()
            if not word1 or not word2:
                break
            print(f"{word1.strip()} was born in {word2.strip()}")
    print("done")

def display5():
    while True:
        try:
            a = int(input("number: "))
        except :
            continue
        break
    print(a)

display5()