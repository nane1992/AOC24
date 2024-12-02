location_ID_G1 = []
location_ID_G2 = []
distances = []

with open ('data.txt', 'r') as input:
    for line in input:
        column1, column2 = map(int, line.split())
        location_ID_G1.append(column1)
        location_ID_G2.append(column2)

while len(location_ID_G1) > 0:
    distances.append(abs(min(location_ID_G1) - min(location_ID_G2)))
    location_ID_G1.remove(min(location_ID_G1))
    location_ID_G2.remove(min(location_ID_G2))

print(sum(distances))

