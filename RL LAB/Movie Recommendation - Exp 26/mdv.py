import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv(
    "q26_movie_feedback.csv"
)

users = df["User"].unique().tolist()
movies = df["Movie"].unique().tolist()

# Create rating matrix
rating_matrix = df.pivot(
    index="User",
    columns="Movie",
    values="Rating"
).fillna(0)

ratings = rating_matrix.values


# -----------------------------------------
# DDPG Parameters
# -----------------------------------------

np.random.seed(42)

# Actor preferences
actor = np.zeros(len(movies))

# Critic values
critic = np.ones(len(movies))

actor_learning_rate = 0.02
critic_learning_rate = 0.01

episodes = 300

reward_history = []


# -----------------------------------------
# Training
# -----------------------------------------

for episode in range(episodes):

    total_reward = 0

    for user in range(len(users)):

        # Actor produces continuous scores
        scores = (
            actor +
            np.random.normal(
                0,
                0.15,
                len(movies)
            )
        )

        # Select movie with highest score
        movie = np.argmax(scores)

        # User feedback
        reward = ratings[
            user,
            movie
        ]

        # Critic error
        error = (
            reward -
            critic[movie]
        )

        # Update critic
        critic[movie] += (
            critic_learning_rate *
            error
        )

        # Update actor
        actor[movie] += (
            actor_learning_rate *
            error
        )

        total_reward += reward

    reward_history.append(
        total_reward
    )


# -----------------------------------------
# Generate Recommendations
# -----------------------------------------

recommendations = []

for user in range(len(users)):

    scores = actor.copy()

    # Find movies not yet rated
    unrated = np.where(
        ratings[user] == 0
    )[0]

    if len(unrated) > 0:

        movie = unrated[
            np.argmax(
                scores[unrated]
            )
        ]

    else:

        movie = np.argmax(scores)

    recommendations.append([
        users[user],
        movies[movie],
        round(
            float(scores[movie]),
            3
        )
    ])


# -----------------------------------------
# Display Results
# -----------------------------------------

result = pd.DataFrame(
    recommendations,
    columns=[
        "User",
        "Recommended_Movie",
        "Actor_Score"
    ]
)

print("MOVIE RECOMMENDATION - DDPG")
print("---------------------------")

print(
    "Average Reward:",
    round(
        np.mean(
            reward_history[-20:]
        ),
        2
    )
)

print(
    "Best Episode Reward:",
    round(
        max(reward_history),
        2
    )
)

print("\nRecommendations:")

print(
    result.to_string(
        index=False
    )
)

print("\nLearned Actor Scores:")

for movie, score in zip(
    movies,
    actor
):

    print(
        movie,
        ":",
        round(
            float(score),
            3
        )
    )
