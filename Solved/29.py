# Distinct Powers

powers = {}

for a in range(2, 101):
    for b in range(2, 101):
        powers.update({a**b: a**b})

print(len(powers))
