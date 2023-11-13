with open("data/cities.csv", "r") as f:
    lines = f.readlines()[1:] # Skips header row

total = 0
for line in lines:
    name, population = line.split(",")
    print(f"Adding {name} to population")
    total += int(population)

print(f"Total population: {total:,}")
print(f"Average population: {total / len(lines):,}")

#Try adding comment --> 1
#Try adding comment --> 2

