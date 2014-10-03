---
layout: post
title: Week 2 Extra Credit
week: 2
permalink: week-2-extra/
---

### Resources

_Feel free to go through these resources to get extra clarification or practice with a topic at any time._

Lists and Loops

* [Khan Academy video on lists](https://www.youtube.com/watch?v=zEyEC34MY1A)
* [Codecademy: lists](http://www.codecademy.com/courses/python-beginner-en-pwmb1/0/1?curriculum_id=4f89dab3d788890003000096)
* [Codecademy: Loops](http://www.codecademy.com/courses/python-beginner-en-cxMGf/0/1?curriculum_id=4f89dab3d788890003000096)

If

* [Control Flow: If and For](http://www.swaroopch.com/notes/python/#control_flow)
* [Codecademy: Control flow](http://www.codecademy.com/courses/python-beginner-BxUFN/0/1?curriculum_id=4f89dab3d788890003000096)

CSV

* [Python CSV official documentation](https://docs.python.org/2/library/csv.html)
* [Python Module of the Week: CSV](http://pymotw.com/2/csv/)
* [Codecademy: Functions](http://www.codecademy.com/courses/python-beginner-c7VZg/0/1?curriculum_id=4f89dab3d788890003000096)

Functions

* [Learn Python the Hard Way: Functions](http://learnpythonthehardway.org/book/ex18.html)

Dictionaries

* [Hackbright: Dictionaries](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise06)
* [Learn Python the Hard Way: Dictionaries](http://learnpythonthehardway.org/book/ex39.html) (last section is advanced)
* [Hackbright: files and dictionaries](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise07)

Extra

* [Codecademy: Datetime](http://www.codecademy.com/courses/python-beginner-en-zFPOx/0/1)
* (Advanced) [Khan Academy: Recursive Fibonacci](https://www.youtube.com/watch?v=urPVT1lymzU&index=18&list=PL36E7A2B75028A3D6)
* (Advanced) [Lambda Tutorial](http://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/)

### Extra Credit/Further Exercises

* Exercise to get more practice with files, loops, and lists: [Count the letters in a file](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise05).

* What does `if __name__=="__main__"` do? [Why](http://stackoverflow.com/a/20158605/3508332)?


####Street Sweeping Extensions

* Extend your `sweep_times` function to take a street number and name, e.g. `sweep_times(683, "Sutter St")`.

* Create a new function, `sweep_day(day, number, street)` which prints out "Yes" if the street is swept on the day provided, and "No" if it is not. You can assume for now that the day will be in the same format as the data, e.g. "Mon" for Monday.

* Extend `sweep_day` to also take a week of the month argument.

* Create a list called `favorite_streets` and figure out how to run `sweep_times` on every street in the list.

* Update `sweep_day` to return a `True` or `False` value.

* Take a command line argument (remember `argv`?) and break out the house number from the street name, calling `sweep_day` with these and tomorrow's day and week number. Take the result you get back from `sweep_day` and print an appropriate message.

Here's a helper if you need it:

```
def split_street(street_address):
    first_space = street_address.find(" ")
    print "The first space in this string is at {}".format(first_space)

    thing_before_space = street_address[:first_space]
    thing_after_space = street_address[first_space:]
    # these selectors cut the array up at the appointed index.

    return (thing_before_space, thing_after_space)
    # Using a tuple (a, b) means the function can
    # return more than one thing at once!

(left, right) = split_street("683 Sutter St")
# and this is how you access the two values.

print left
print right
```

* Update `sweep_day` to allow other ways of typing the day name. Helper:

```
>>> if 'mon' in 'monday':
...     print 'found'
...
>>> dayname = 'Mon'
>>> longname = 'monday'
>>> print dayname.lower()
>>> print longname.lower()
>>> if dayname in longname:
...    print 'found'
...
>>> if dayname.lower() in longname.lower():
...    print 'found when I checked lowercase'
...

```

* Use the `raw_input()` function to get input from a user instead of a command line argument. It helps if you've done the piece before, as you can't expect users to always put 'Mon' for 'Monday'!

  Intros to `raw_input()`:

  * [Hackbright Guessing Game](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise01)
  * [Learn Python The Hard Way: raw_input](http://learnpythonthehardway.org/book/ex11.html)
  

####Pirate BARRRRRtender

_This is a sneak preview of a Week 3 exercise that you can do now if you run out of things to do, or want a change from street sweeping!_

**Practices: dictionaries, functions, raw_input**

To get really down and dirty with functions, let's create a new app which specializes in bartending. Pirate barrrrrtending. 

The bartender will invent a new and delicious cocktail for you based upon your answers to some simple questions.

#####Create questions and ingredient dictionaries

The bartender should ask questions that determine your tastes and then identify ingredients to suit those tastes. If you like you can use the example bartender below, but feel free to customize!

```
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}
```

#####Write a function to ask what style of drink a customer likes.

The function should ask each of the questions in the `questions` dictionary, and gather the responses in a new dictionary. The new dictionary should contain the type of ingredient (for example `"salty"`, or `"sweet"`), mapped to a Boolean (True|False) value. If the customer answers y or yes to the question then the value should be `True`, otherwise the value should be `False`. 

The function should return the new dictionary.

Remember that you can use the `raw_input` function to get an answer from the landlubber... er, customer. 

#####Write a function to construct a drink

The function should take the preferences dictionary created in the first function as a parameter. Inside the function you should create an empty list to represent the drink. For each type of ingredient which the customer said they liked you should append a corresponding ingredient from the ingredients dictionary to the drink. Finally the function should return the drink.

To choose an ingredient from one of the ingredient lists you can use the `choice` function. This selects a random item from a list, for example:

```
import random

beatles = ["John", "Paul", "George", "Ringo"]
# Print the name of a random Beatle
print random.choice(beatles)
```

####Provide a main function

Use `if __name__ == '__main__':` to run this function from the command line. The main function should call your two functions in order, passing your list of preferences to the drink creation function. It should then print out the contents of the drink.

If you haven't encountered this in the other exercises yet, this is a good skeleton you can start with:

```
# code
# code
# code
def main():
    # first piece of code you want to run in this file
    print "main"
    

if __name__=="__main__":
    main() 
# this means "if this is run from the command line, run the main() function"
```

If this is getting odd results make sure that *all* your other code is inside functions so you don't end up accidentally running it when you run the file.

To run the file, it's just `python bartender.py` (or whatever you called it).

####Discussion
Once you've completed the basic requirements for the project, feel free to take a look at [this sample solution](https://gist.github.com/jennielees/af968ee8b13805a350b8). Compare and contrast your solution. What do you like better about the sample? What do you like better about yours?

####Extra challenges
If you found completing the basic requirements fairly straightforward then you should try to extend your app to add the following features:

#####Push to version control
Use Git to save your bartender file and push it to GitHub.

#####Give the cocktails a name
All good cocktails should have a memorable name. Try to write a function which will name your cocktails. The name should be a random combination of an adjective and a noun (for example your bartender could make a "Fluffy Chinchilla", a "Salty Sea-Dog", or a "Fluffy Sea-Dog"). Think back to the superheroes, though you don't have to use a file for the input words, a list or dictionary in the code is fine.

#####Keep 'em coming
At the moment you can only get one drink at a time from the bartender. A well trained pirate bartender should offer his customer another drink when they've finished their previous one. Try adding a loop in the main function which will ask the customer whether they want another drink, and keep creating new recipes as long as they agree.

#####Stock control

Even pirate bars don't have a limitless supply of ingredients. You could add a stock count for each ingredient which decreases whenever the bartender makes a drink. Print a message to tell the bartender to restock the ingredients when supplies are low.