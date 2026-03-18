
def get_red_hood_dates(name , status , favorite_food):
    red_hood_dates = name + " ," + status + ", and my favorite food is " + favorite_foo
    return red_hood_dates
 
def test(name , status , favorite_food):
    red_hood_dates = get_red_hood_dates(name , status , favorite_food)
    print("Name: " + name)
    print("Status: " + status)
    print("Favorite Food: " + favorite_food)
    print("Title: " + red_hood_dates)
    print("  ~ xoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxo ~")

test("Barbara Gordon", "Hero", "Pizza")
test("Isabel Ardila", "Civilian", "Sushi")
test("Essence", "Neutral (Neither good or bad)", "Burgers -Medium rare")
test("Talia Al Ghul", "Villain", "Lobster")