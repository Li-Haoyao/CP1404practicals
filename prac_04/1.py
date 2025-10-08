def display1():
    NAMES = {"Ada", "Alan", "bill", "John"}
    print(", ".join(NAMES))
    while len(NAMES):
        name = input("who do you want to remove: ")
        if name == " ":
            break
        try:
            NAMES.remove(name)
        except:
            print("not in list")
        print(", ".join(NAMES))
    print("done")

def display2():
    numbers = get_numbers()
    square_number(numbers)
    display_number(numbers)

def get_numbers():
    items = input("enter numbers separated by commas: ")
    numbers = sorted([float(num) for num in items.split(",") if num.strip() != ""])
    return numbers

def square_number(numbers):
    for i in range(len(numbers)):
        numbers[i] *= numbers[i]

def display_number(nums):
    print(*nums)

def display3():
    data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
    name_long = max((len(item[0]) for item in data))
    score_long = max((len(str(item[1])) for item in data))
    for item in data:
        print(f"{item[0]:{name_long}} = {item[1]:{score_long}}")

display2()
