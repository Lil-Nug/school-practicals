list_1 = list(input("Enter 3 numbers seperated by commas: ").split(','))
print(list_1)

list_2 = []

for i in list_1:
    list_2.append(int(i))

print(list_2)