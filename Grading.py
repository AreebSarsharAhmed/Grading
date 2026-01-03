scores = [100, 100, 90, 80, 80, 70]

# Get unique scores in descending order
unique_scores = sorted(set(scores), reverse=True)

# Create ranking
rank = {}
current_rank = 1

for score in unique_scores:
    rank[score] = current_rank
    current_rank += 1

# Print ranks
for s in scores:
    print(f"Score: {s}, Rank: {rank[s]}")