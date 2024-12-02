location_ID_G1 = []
location_ID_G2 = []
similarity=[]

with open ('data.txt', 'r') as input:
    for line in input:
        column1, column2 = map(int, line.split())
        location_ID_G1.append(column1)
        location_ID_G2.append(column2)

for ID_G1 in location_ID_G1:
    multiplier=0
    for ID_G2 in location_ID_G2:
        if ID_G1 == ID_G2:
            multiplier += 1
    similarity.append(ID_G1*multiplier)

print(sum(similarity))

