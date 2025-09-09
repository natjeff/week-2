import numpy as np

# update/add code below ...

#Function to calculate number of ways
def ways(n: int) -> int:
    return n // 5 + 1

#Test Cases Below
print(ways(12))
print(ways(20))
print(ways(3))
print(ways(0))

# Find lowest score
def lowest_score(names, scores):
    idx = np.argmin(scores)
    return names[idx]

# Sort names by score
def sort_names(names, scores):
    idx_sorted = np.argsort(scores)[::-1]
    sorted_names = names[idx_sorted]
    sorted_scores = scores[idx_sorted]
    return list(zip(sorted_names, sorted_scores))

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

#Test Cases Below
print(lowest_score(names, scores))
print(sort_names(names, scores))
