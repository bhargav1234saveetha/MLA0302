bins = {
    "Bin A": 40,
    "Bin B": 90,
    "Bin C": 65
}

for name, level in bins.items():
    print(name, "Fill Level:", level, "%")

full_bin = max(bins, key=bins.get)
print("Collect First:", full_bin)
