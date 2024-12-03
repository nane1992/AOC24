import re

with open("data.txt", "r") as data:
    corrupted_memory = data.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern,corrupted_memory)

total = 0
for match in matches:
    a, b = map(int, match)
    total += a * b

print("Sum: ", total)






