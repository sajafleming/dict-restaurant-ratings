# your code goes here

def alph_restaurant_ratings(filename):
    """print
    """

    restaurants = {}
    scores_file = open(filename)

    #create dictionary from lines in text file that we opened above
    for line in scores_file:
        line = line.rstrip()
        names_and_scores = line.split(":")
        
        #setting the keys and values 
        restaurants[names_and_scores[0]] = names_and_scores[1]

    scores_file.close()
    #creates a new list of sorted key names
    sorted_restaurants = sorted(restaurants.keys())


    # using our sorted list of keys to search the 
    # dictionary "restaurants" for corresponding values 
    for restaurant in sorted_restaurants:
        rating = restaurants[restaurant]

        print restaurant + " is rated at " + rating

alph_restaurant_ratings("scores.txt")
