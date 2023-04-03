# Passcode derivation
# Works I guess

data = open('79.txt').read().splitlines()

codes = []
for datum in data:
    if datum not in codes:
        codes.append(datum)

not_nums=["0","1","2","3","4","5","6","7","8","9"]

for code in codes:
    remove = []
    for i in range(len(not_nums)):
        if not_nums[i] in code:
            remove = [i] + remove
    for i in remove:
        not_nums.pop(i)

DONE = False
while not DONE:
    begin_nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    end_nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for num in not_nums:
        begin_nums.remove(num)
        end_nums.remove(num)

    for code in codes:
        remove = []
        for i in range(len(begin_nums)):
            if begin_nums[i] in code[1:]:
                remove = [i] + remove
        for i in remove:
            begin_nums.pop(i)
        remove = []
        for i in range(len(end_nums)):
            if end_nums[i] in code[:-1]:
                remove = [i] + remove
        for i in remove:
            end_nums.pop(i)

    print("Begin:", begin_nums)
    print("End:", end_nums)
    print()
    not_nums.append(begin_nums[0])
    not_nums.append(end_nums[0])

    for i in range(len(codes)):
        codes[i] = codes[i].replace(begin_nums[0], "")
        codes[i] = codes[i].replace(end_nums[0], "")

    #print(codes)
    DONE = True
    for code in codes:
        if code != "":
            DONE = False
            break
