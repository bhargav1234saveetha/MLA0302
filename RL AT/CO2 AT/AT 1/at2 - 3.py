movies = {
    "Action": 8,
    "Comedy": 5,
    "Drama": 3
}

for movie, reward in movies.items():
    print(movie, "Reward:", reward)

best = max(movies, key=movies.get)
print("Recommended Category:", best)
