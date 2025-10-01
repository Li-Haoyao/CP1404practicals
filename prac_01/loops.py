for i in range(1, 21, 2):
    print(i, end=' ')
print("\na)")
for i in range(0, 101, 10):
    print(i, end=' ')
print("\nb)")
for i in range(20, 0, -1):
    print(i, end=' ')
print("\nc)")
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end='')
print("\nd)")
n = int(input("Number of lines: "))
for i in range(1, n + 1):
    print("*" * i)
