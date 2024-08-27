# Exercise 1: List and Indexing


def manage_students():
    students = ['Ali' , 'Ahmed' , 'Qasim']
    first_student = students[1]
    last_student = students[2]
    print('First Student:', first_student)
    print('Last Student:', last_student)

    return first_student, last_student

print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation


def combine_foods():
    foods = 'Machbous' , 'Steak' , 'Shakshoka'
    meal = ''
    for food in foods:
        meal += food + ' '
    return meal

print('Exercise 2:', combine_foods())

# Exercise 3: Slicing Tuples

def slice_foods():
    foods = 'Machbous' , 'Steak' , 'Shakshoka'
    last_two_foods = foods[-2] , foods[-1]
    return last_two_foods

print('Exercise 3:', slice_foods())

# Exercise 4: Dictionaries and String Formatting

def hometown_info():
    # your code here

    home_town = {
        'city' : 'Manama',
        'state' : 'Capital',
        'population' : 100000
    }
    home_town_message= (f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")
    return home_town_message

print('Exercise 4:', hometown_info())

# Exercise 5: Iterating Over Dictionary Items


def list_home_town_items():
    home_town_items = []
    home_town = {
        'city' : 'Manama',
        'state' : 'Capital',
        'population' : 100000
    }
    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")
    return home_town_items

print('Exercise 5:', list_home_town_items())

