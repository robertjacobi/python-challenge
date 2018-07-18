import os
import csv

election_csv = os.path.join("election_data.csv")

total_votes = 0
name_list = []
name_list2 = []
candidates = []
w = 0
x = 0
y = 0
z = 0

with open(election_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvfile)

    for row in csvreader:
        total_votes = total_votes + 1

        name_list.append(row[2])
        name_list2.append(row[2])

    for line in name_list:
        con = line.split()
        for names in con:
            if names not in candidates:
                candidates.append(names)

w = name_list2.count(str(candidates[0]))
x = name_list2.count(str(candidates[1]))
y = name_list2.count(str(candidates[2]))
z = name_list2.count(str(candidates[3]))

wPer = round(int((w / total_votes) * 100),3)
xPer = round(int((x / total_votes) * 100),3)
yPer = round(int((y / total_votes) * 100),3)
zPer = round(int((z / total_votes) * 100),3)

if w > x and w > y and w > z:
    winner = str(candidates[0])
if x > w and x > y and x > z:
    winner = str(candidates[1])
if y > x and y > z and y > z:
    winner = str(candidates[2])
if z > x and z > y and z > x:
    winner = str(candidates[3])

print("                                         ")
print("Election Results")
print("------------------------")
print("Total Votes: " + str(total_votes))
print("------------------------")
print(str(candidates[0]) + ": " + str(wPer) + "%" + " (" + str(w) + ")")
print(str(candidates[1]) + ": " + str(xPer) + "%" + " (" + str(x) + ")")
print(str(candidates[2]) + ": " + str(yPer) + "%" + " (" + str(y) + ")")
print(str(candidates[3]) + ": " + str(zPer) + "%" + " (" + str(z) + ")")
print("------------------------")
print("Winner: " + str(winner))
print("------------------------")

output_path = os.path.join("PyPoll.txt")

with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['--------------------------'])
    csvwriter.writerow(['Total Votes: ' + str(total_votes)])
    csvwriter.writerow(['--------------------------'])
    csvwriter.writerow([str(candidates[0]) + ': ' + str(wPer) + '%' + ' (' + str(w) + ')'])
    csvwriter.writerow([str(candidates[1]) + ': ' + str(xPer) + '%' + ' (' + str(x) + ')'])
    csvwriter.writerow([str(candidates[2]) + ': ' + str(yPer) + '%' + ' (' + str(y) + ')'])
    csvwriter.writerow([str(candidates[3]) + ': ' + str(zPer) + '%' + ' (' + str(z) + ')'])
    csvwriter.writerow(['--------------------------'])                
    csvwriter.writerow(['Winner: ' + str(winner)])
    csvwriter.writerow(['--------------------------'])                                       