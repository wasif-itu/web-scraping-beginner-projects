def test():
    for i in range(51):
        if i% 2==0:
            print(i)

test()


foods= ['apple', 'banana', 'cherry', 'date']

tuple_foods = tuple(foods)

students = { 'wasif': 21, 'ali': 22, 'sara': 20 }

print(students.keys())

print(students.values())

print(f"top_scorer: {max(students, key=students.get)}")


beverages = ['coffee', 'tea', 'juice']

with open('beverages.txt', 'w') as file:
    for i in beverages:
        file.write(i+ "\n")

with open('beverages.txt', 'r') as file:
    contents=file.readlines()

for line in contents:
    line.strip()
    print(line)


import csv

with open('fruits.csv', 'w', newline='') as csvfile:
    fruit_writer = csv.writer(csvfile)
    fruit_writer.writerow(['Name', 'Color', 'Taste'])
    fruit_writer.writerow(['Apple', 'Red', 'Sweet'])
    fruit_writer.writerow(['Banana', 'Yellow', 'Sweet'])
    fruit_writer.writerow(['Cherry', 'Red', 'Sweet-tart'])
with open('fruits.csv', 'r') as csvfile:
    fruit_reader = csv.reader(csvfile)
    for row in fruit_reader:
        print(row)





import datetime
today= datetime.date.today()
print(f"Today's date is: {today}")
