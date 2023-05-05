repeats = [1,1,2,2,3,4,5,5,6,7,9,9,8]

uniques = []

for repeat in repeats:
    if repeat not in uniques:
        uniques.append(repeat)

print(uniques)