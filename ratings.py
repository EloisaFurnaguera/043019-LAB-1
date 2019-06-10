


"""Restaurant rating lister."""
scores = {}

ratings_list = open("scores.txt")


for line in ratings_list:
    line = line.strip()
    rating = line.split(":")
    
    restaurant_name = rating[0]
    restaurant_score = rating[1]
    scores[restaurant_name] = restaurant_score

for name , rating in sorted(scores.items()):
    print (name, rating)



    


"""Ask the user for a new restaurant rating"""

print("Enter a new restaurant rating:")


new_restaurant = input("Name of the restaurant >") 
user_rating = input("Restaurant rating > ")

print(f'{new_restaurant} has been added')

scores[new_restaurant] = user_rating


for name , rating in sorted(scores.items()):
    print (name, rating)