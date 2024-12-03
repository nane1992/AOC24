import re

with open("data.txt", "r") as data:
    corrupted_memory = data.read()

pattern = r"(do\(\)|don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, corrupted_memory)

mul_enabled = True
total = 0

for match in matches:
    if match[0]:
        mul_enabled = match[0] == 'do()'
    else:
        if mul_enabled:
            a, b = map(int, match[1:])
            total += a * b

print("Sum: ", total)


