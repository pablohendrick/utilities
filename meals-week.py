import random

# Set your favorite meals
meals = ['your meal', 'your meal', 'your meal']

# Set days of the week
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create weekly table
table_meals = {}
for day in days_of_the_week:
    # Select random meal
    aleatory_meals = random.choice(meals)
    # Add meals in the table
    table_meals[day] = aleatory_meal

# Print table
for day, meal in table_meals.items():
    print(day + ': ' + meal)
