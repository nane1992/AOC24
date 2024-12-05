with open("data.txt", "r") as data:
    rules_part, updates_part = data.read().split("\n\n")

with open("rules.txt", "w") as rules_file:
    rules_file.write(rules_part)
with open("updates.txt", "w") as updates_file:
    updates_file.write(updates_part)

with open ("rules.txt", "r") as rules:
    rules=rules.read().splitlines()
    rules=[rule.split("|") for rule in rules]
    rules = [[int(j) for j in i] for i in rules]

with open ("updates.txt", "r") as updates:
    updates=updates.read().splitlines()
    updates=[update.split(",") for update in updates]
    updates = [[int(j) for j in i] for i in updates]

for order in updates[:]:
    for rule in rules:
        a,b=rule
        if a in order and b in order:
            if order.index(a) > order.index(b):
                updates.remove(order)
                break

total=0
for order in updates:
    middle_index=int((len(order)-1)/2)
    total += order[middle_index]
    
print(total)

