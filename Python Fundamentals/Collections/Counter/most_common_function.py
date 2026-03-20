from collections import Counter

visits=["home","about","contract","home","about","home","profile","home","about","contact"]
visits_count=Counter(visits)

most_visited=visits_count.most_common(2)
print("Most visited pages: ", most_visited)

least_visited=visits_count.most_common()[:-3:-1]
print("Least visited pages: ",least_visited)

print("Total visits: ",visits_count.total())