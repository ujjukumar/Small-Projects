python_students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    temp_list = [name, score]
    python_students.append(temp_list)

Output = min(python_students, key = lambda x: x[1])

# To remove multiple lowest if exists
lowest_list = []
for x in python_students:
    if x[1] == Output[1]:
        lowest_list.append(x)

for x in lowest_list:
    python_students.remove(x)

seconds = min(python_students, key = lambda x: x[1])

names = [x[0] for x in python_students if x[1]==seconds[1]]

for name in names:
    print(name)