import csv
classes = []
for i in range(10):
    classes.append([])
    for j in range(2):
        classes[i].append([])
with open('data.csv') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if row[0] == '0':
            if row[1] == '0':
                classes[0][0].append(row)
            else:
                classes[0][1].append(row)
        elif row[0] == '1':
            if row[1] == '1':
                classes[1][0].append(row)
            else:
                classes[1][1].append(row)
        elif row[0] == '2':
            if row[1] == '2':
                classes[2][0].append(row)
            else:
                classes[2][1].append(row)
        elif row[0] == '3':
            if row[1] == '3':
                classes[3][0].append(row)
            else:
                classes[3][1].append(row)
        elif row[0] == '4':
            if row[1] == '4':
                classes[4][0].append(row)
            else:
                classes[4][1].append(row)
        elif row[0] == '5':
            if row[1] == '5':
                classes[5][0].append(row)
            else:
                classes[5][1].append(row)
        elif row[0] == '6':
            if row[1] == '6':
                classes[6][0].append(row)
            else:
                classes[6][1].append(row)
        elif row[0] == '7':
            if row[1] == '7':
                classes[7][0].append(row)
            else:
                classes[7][1].append(row)
        elif row[0] == '8':
            if row[1] == '8':
                classes[8][0].append(row)
            else:
                classes[8][1].append(row)
        elif row[0] == '9':
            if row[1] == '9':
                classes[9][0].append(row)
            else:
                classes[9][1].append(row)

node_activation = []

for i in range(256):
    print(str(i+1)+"/256")
    node = i + 2

    node_activation.append([])

    for j in range(10):
        sum_1 = 0.0
        sum_2 = 0.0
        for cT in classes[j][0]:
            sum_1 += float(cT[node])
            for tmp_node in cT[2:]:
                sum_2 += float(tmp_node)

        node_activation[i].append([])
        node_activation[i][j].append(sum_1/sum_2)

        sum_1 = 0
        sum_2 = 0
        for cF in classes[j][1]:
            sum_1 += float(cF[node])
            for tmp_node in cF[2:]:
                sum_2 += float(tmp_node)

        node_activation[i][j].append(sum_1/sum_2)

for i in node_activation:
    print(i)
