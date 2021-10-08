""" Quiz questions and answers """
import random

# Return / enter not included: 3 spaces
questions = {
    '1. What is the result of f"{2 + 2} + {10 % 3}": ': '4 + 1',

    '2. Assuming name = "Jane Doe", what does name[1] return: ': 'a',

    '3. What will name.find("Doe") return from "Jane Doe": ': '5',

    '4. What is the result of "bag" > "apple": ': 'True',

    '5. console.log() is to JavaScript as " blank " is to Python: ': 'print()',

    '6. print "Hello Pythonic!": ':
    'print("Hello Pythonic!")',

    '7. Coding Challenge: while True print "keep learning and enjoying life": "':
    'while True:   print("keep learning and enjoying life")',

    '8. Coding Challenge: interate over a dict named user_data via the items() method.\
        \n   Use the variable username to represent your "keys", and the variable password\
        \n   to represent your "values". Finally print out username, and password.':
    'for username, password in user_data.items():   print(username, password)',

    '9. create a function named ice_cream with two parameters, flavor="vanilla" and topping=None.\
        \n   Return your flavor and topping in a undeclared tuple: ':
    'def ice_cream(flavor="vanilla", topping=None):   return (flavor, topping)',

    '10. Coding Challenge: if food is "salad" print healthy else if food is "fast food" print unhealthy: ':
    'if food == "salad":   print("healthy")elif food == "fast food":   print("unhealthy")',

    '11. Coding Challenge: if 5 is greater than 1 print True, else print False ':
    'if 5 > 1:   print(True)else:   print(False)',

    '12. Using double quotes and the insert method please insert "New York"\
        \n   to cities = ["a", "b", "c"] at index 0: ':
    'cities.insert(0, "New York")',

    '13. How would you append "python" to a list called langs: ':
    'langs.append("python")',

    '14. create a list named cities with "LA", "NY" and "SEA": ':
    'cities = ["LA", "NY", "SEA"]',

    '15. Re-write the multiline comment below in a single line using single quotes:\n\n"""\nPython\nis\nawesome!\n"""':
    '\'Python is awesome!\'',

    '16. Coding Challenge: if clothing is red and beard is white, person equals Santa: ':
    'if clothing == "red" and beard == "white":   person = "Santa"',

    '17. what data type is user_variable = {2, 4, 5}. A "dict" or "set": ':
    'set',

    '18. Coding Challenge: if first_name equal "Sherlock", last_name is "Holmes" ':
    'if first_name == "Sherlock":   last_name = "Holmes"',

    '19. Coding Challenge: if species equal to "cat" print "Yep, it\'s a cat." ':
    'if species == "cat":   print("Yep, it\'s a cat.")',

    '20. print "Hello World!" : ':
    'print("Hello World!")'
}

# Randomize dict: because you can't shuffle a dict
list_questions = list(questions.items())  # place dict into a list
random.shuffle(list_questions)  # shuffle list
questions = dict(list_questions)  # turn list back into a dict
