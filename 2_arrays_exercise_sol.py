# exercise 1

expenses = [2200, 2350, 2600, 2130, 2190]
print(f"I spent extra {expenses[1]-expenses[0]} in feb comparing to jan")
print(f"Total expenses in first qarter: {expenses[0]+expenses[1]+expenses[2]}")
n = 0
for i in expenses:
    if int(i) == 2000:
        print("i have spent 2000 in {i} month")
        n += 1
if n == 0:
    print("I didnt spent 2000 in any month")
expenses.append(1980)
print(expenses)
expenses[3] = expenses[3]-200
print(expenses)

# exercise 2

heros=['spider man','thor','hulk','iron man','captain america']
print(len("heros"))
heros.append("black panther")
print(heros)
heros.remove("black panther")
heros.insert(3, "black panther")
print(heros)
heros[1:3]=["doctor strange"]
print(heros)
#print(dir(heros))
heros.sort()
print(heros)

#exercise 3

max = int(input("insert max number to which ill show you odd numbers:"))
for i in range(max):
    if i % 2 == 1:
        print(i)

