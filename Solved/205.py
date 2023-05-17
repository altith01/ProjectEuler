# Dice Game

def generate_occurances(num_sides, num_dice):
    if num_dice == 1:
        return [1 for _ in range(num_sides)]
    else:
        previous_occurances = generate_occurances(num_sides, num_dice-1)
        occurances = []
        for i in range(num_sides-1):
            occurances.append(sum(previous_occurances[:i+1]))
        for i in range(1+(num_dice-2)*(num_sides-1)):
            occurances.append(sum(previous_occurances[i:i+num_sides]))
        for i in range(num_sides-1,0,-1):
            occurances.append(sum(previous_occurances[-i:]))
        return occurances

peter_occurances = generate_occurances(4, 9)
peter_total = sum(peter_occurances)
colin_occurances = generate_occurances(6, 6)
colin_total = sum(colin_occurances)

matrix = []

for p in peter_occurances:
    matrix.append([])
    for c in colin_occurances:
        matrix[-1].append((p/peter_total)*(c/colin_total))

prob = 0
for i in range(len(matrix)):
    prob += sum(matrix[i][:i+3])

print(prob)
