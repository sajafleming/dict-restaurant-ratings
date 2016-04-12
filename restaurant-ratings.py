# your code goes here

def alph_restaurant_ratings(filename):

    restaurants = {}
    scores = open(filename)

    #create dictionary from lines in text file that we opened above
    for line in scores:
        line = line.rstrip()
        words = line.split(":")
        
        #setting the keys and values 
        restaurants[words[0]] = words[1]

    #creates a new list of sorted key names
    sorted_restaurants = sorted(restaurants)

    counter = 0

    # using our sorted list of keys to search the 
    # dictionary "restaurants" for corresponding values 
    for restaurant in sorted_restaurants:
        key = sorted_restaurants[counter]
        value = restaurants[sorted_restaurants[counter]]

        counter += 1

        print key + " is rated at " + value

alph_restaurant_ratings("scores.txt")
