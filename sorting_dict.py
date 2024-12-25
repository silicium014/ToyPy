dictionary = {
    21: "Manchester",
    30: "Liverpool",
    18: "Cheslea",
    17: "Manchester City",
    20: "Arsenal",
    10: "Tottenham"
}
# sort by key
print(sorted(dictionary.items(),key=lambda v: v[0]))

# sort by value
print(sorted(dictionary.items(),key=lambda v: v[1]))



