import csv

mydate = ['(月)4限','(火)2限','(火)5限','(木)5限','(金)5限']#ここに開催日程を入力する

with open("./educa.csv", "rt", newline="") as csvfile:
    reader = csv.reader(csvfile)
    profile = [row for row in reader]

x = profile.pop()

name = profile[0]

name_point = {}
name_point.update(zip(name,[0 for i in range(len(name))]))

mydate_point = {}
mydate_point.update(zip(mydate,[0 for i in range(len(mydate))]))

date_list = [profile[i][0] for i in range(len(profile))]

for i in range(len(date_list)):
    if date_list[i] in mydate:
        for j in range(len(profile[i])):
            if profile[i][j] == "○":
                mydate_point[profile[i][0]] += 1
                name_point[profile[0][j]] += 1

print(name_point)
print(mydate_point)