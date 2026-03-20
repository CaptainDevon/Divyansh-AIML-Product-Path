from collections import Counter

votes=["Python","Javascript","C++","Java","Java","C++","Javascript","Python","Python","C++","Javascript"]

vote_count=Counter(votes)
print(vote_count)
print(f"Python votes: {vote_count["Python"]}")
print(f"Java votes: {vote_count["Java"]}")
print(f"C++ votes: {vote_count["C++"]}")
print(f"Javascript votes: {vote_count["Javascript"]}")
print(f"GO votes (no in the list): {vote_count["GO"]}")
