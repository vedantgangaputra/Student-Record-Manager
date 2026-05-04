import matplotlib.pyplot as plt

file = "data.txt"


def add():
    name = input("name: ")
    marks = input("marks: ")

    f = open(file, "a")
    f.write(name + "," + marks + "\n")
    f.close()

    print("added\n")


def show():
    try:
        f = open(file, "r")
        data = f.readlines()
        f.close()

        if len(data) == 0:
            print("no data\n")
            return

        for i in data:
            x = i.strip().split(",")
            print(x[0], "-", x[1])
        print()

    except:
        print("file not found\n")


def graph():
    f = open(file, "r")
    names = []
    marks = []

    for i in f:
        x = i.strip().split(",")
        names.append(x[0])
        marks.append(int(x[1]))

    f.close()

    if len(names) == 0:
        print("no data to show graph\n")
        return

    plt.figure()
    plt.bar(names, marks)
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.title("Student Marks Graph")
    plt.show()


while True:
    print("1 add")
    print("2 show")
    print("3 graph")
    print("4 exit")

    ch = input("choice: ")

    if ch == "1":
        add()
    elif ch == "2":
        show()
    elif ch == "3":
        graph()
    elif ch == "4":
        break
    else:
        print("wrong input\n")