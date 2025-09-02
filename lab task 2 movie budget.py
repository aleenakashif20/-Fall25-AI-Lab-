movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

# Calculate average budget 
average_budget = sum(budget for _, budget in movies) / len(movies)

print(f"The average budget for all movies is: ${average_budget:,.2f}\n")
print("Movies with budgets higher than the average:")

# Use a list comprehension to filter for movies over the average
high_budget_movies = [movie for movie in movies if movie[1] >average_budget]

# Loop and print the results
for name, budget in high_budget_movies:
    print(f"- {name} with a budget of ${budget:,}")