# Roman numerals

numerals = open('89.txt', 'r').readlines()

saved_total = 0
for numeral in numerals:
    saved = 0
    numeral = numeral.strip()
    length = len(numeral)
    if 'IIII' in numeral:
        saved += 2
        if 'VIIII' in numeral:
            saved += 1
    if 'XXXX' in numeral:
        saved += 2
        if 'LXXXX' in numeral:
            saved += 1
    if 'CCCC' in numeral:
        saved += 2
        if 'DCCCC' in numeral:
            saved += 1
    saved_total += saved

print(saved_total)
