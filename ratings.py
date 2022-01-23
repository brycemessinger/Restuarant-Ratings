"""Restaurant rating lister."""

from logging.handlers import RotatingFileHandler

# find alt name this func, its used later
# try not to keep 'dictionary' as the name of the dictionary
def read_scores():
    ratings_file = open('scores.txt', 'r')
    dictionary = {}

    for line in ratings_file:
        line = line.rstrip()
        restaurant, score = line.split(":")
        dictionary[restaurant] = int(score)
    return dictionary
        
def read_restaurants(scores):
    print("What is the name of the restaurant and what is it's rating?")
    restaurant_name = input("Restarant name ")
    restaurant_rating = input("Restarant rating ")
    scores[restaurant_name] = restaurant_rating






def print_scores(scores):
    for restaurant, rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}.")

# post_scores = read_scores()
scores = read_scores()
read_restaurants(scores)
print_scores(scores)
