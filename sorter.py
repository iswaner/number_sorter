import random

length = int(input("Pick how many numbers to sort: "))
first = "x"
choice = input("Ascending, Descending, or Shuffled? ")
first = choice[0].lower()

while(first != "a" and first != "d" and first != 's'):
    choice = input(print("Ascending, Descending, or Shuffled?"))
    first = choice[0].lower()

list = []
for i in range(1,length + 1):
    list.append(i)

if first == ('a'):
    print(*list, sep = " ")
elif first == ('d'):
    list.sort(reverse = True)
    print(*list, sep = " ")
elif first == ('s'):
    random.shuffle(list)
    print(*list, sep = " ")
else:
    print("Somehow you got to the end with an invalid choice")
    sys.exit
