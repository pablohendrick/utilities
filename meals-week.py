import random as rd

meals = ['your meal', 'your meal', 'your meal']

days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

table_meals = {}
for day in days_of_the_week:
    aleatory_meals = random.choice(meals)
    table_meals[day] = aleatory_meal

for day, meal in table_meals.items():
    print(day + ': ' + meal)
