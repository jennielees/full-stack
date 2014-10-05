---
layout: post
title: Pocket Dictionaries
week: 3
---

### Dictionary Corner

What's a dictionary? When is it used? What parallels does it have to other things (e.g. Javascript/JSON)?

Check out [this piece on dictionaries](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise06) to find out this, and more. (Stop at the exercises part and come back here.)

Keys and values crop up all over the world of programming, so you've probably seen something similar already, even if you didn't realise it. Sometimes you will also see the word _hash_ used for the same thing.

A dictionary is Python's term for a key-value store, and it's just as it sounds: a way to map *keys* into *values*.

A simple dictionary (or 'dict' for short) looks like this: you can type this code directly into `python` to try it out.

```
# Defining a new dictionary

leet_skillz = {
    'halo': 10,
    'starcraft': 4,
    'hearthstone': 7,
    'solitaire': 11,
    'simcity': 9
    }
    
# Defining an empty dictionary

no_skillz = {}
```

The colon separates the key from the value. The key has to be a fixed piece of data, usually a string or a number. New keys can be added to a dictionary, so they can (but don't have to) start out empty.

The value in a dictionary can be any kind of Python data type, and we'll see more complex examples of this soon!

How do you use this? Finding an element is similar to a list, but with a string key, not an integer:

```
print leet_skillz['simcity']
```

You can also use the `get()` function which behaves itself much more nicely if the key isn't actually there.

```
awesome = leet_skillz.get('halo')
oops = leet_skillz.get('callofduty')
print awesome
print oops
```

Adding new items to a dictionary is nice and simple:

```
leet_skillz['bridge'] = 8
no_skillz['skateboarding'] = True

print leet_skillz
print no_skillz
```

Now there's a new entry. If something was already there, it got overwritten. You can also use a variable as the key:

```
best_game_ever = "dominion"
leet_skillz[best_game_ever] = 4

print leet_skillz
```

In a `for` loop, the `for something in dictionary` operator looks at the **keys** in the dictionary, making it possible to loop through the dictionary as well as only work with the keys.

```
for game in leet_skillz:
   print "Looking at {}".format(game)
   skill = leet_skillz[game]
   print "My skill level is {}".format(skill) 
```

#####Why do we use dictionaries?

For one, they make it much easier to lump data together and access it with a friendly name. Unlike lists, they don't commit you to defining (or knowing) the size or position of elements, which makes things much easier on-the-fly.

There are also a lot of places where you want to keep track of two (or more) things at once, like scores in different categories, and a dictionary saves you from trying to keep track of where you are in a bunch of different lists. Thanks, dictionaries!

More dictionary practice: [Learn Python the Hard Way](http://learnpythonthehardway.org/book/ex39.html) and [Codecademy](http://www.codecademy.com/courses/python-beginner-en-pwmb1/2/1). 
_The Codecademy exercise starts with lists, so you may have already done all or some of it._

### Piratical Diction

####Pirate BARRRRRtender

**Practices: dictionaries, functions, raw_input**

To get really down and dirty with functions and dictionaries, let's create a new app which specializes in bartending. Pirate barrrrrtending. 

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

* The function should ask each of the questions in the `questions` dictionary, and gather the responses in a new dictionary. 
* The new dictionary should contain the type of ingredient (for example `"salty"`, or `"sweet"`), mapped to a Boolean (True or False) value. 
* If the customer answers y or yes to the question then the value should be `True`, otherwise the value should be `False`. 
* The function should return the new dictionary.

You can use the `raw_input` function to get an answer from the landlubber... er, customer. This [exercise](http://learnpythonthehardway.org/book/ex11.html) is a good introduction (or reminder).

#####Write a function to construct a drink

* The function should take the preferences dictionary created in the first function as a parameter. 
* Inside the function you should create an empty list to represent the drink. 
* For each type of ingredient which the customer said they liked you should append a corresponding ingredient from the ingredients dictionary to the drink. 
* Finally the function should return the drink.

To choose an ingredient from one of the ingredient lists you can use the `random.choice` function again (remember the superhero names?). This selects a random item from a list, for example:

```
import random

beatles = ["John", "Paul", "George", "Ringo"]
# Print the name of a random Beatle
print random.choice(beatles)
```

####Provide a main function

Use `if __name__ == '__main__':` to run this function from the command line. The `main()` function should call your two functions in order, passing your list of preferences to the drink creation function. It should then print out the contents of the drink.

This is a good skeleton you can start with:

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

####Extra challenges!
If you found completing the basic requirements fairly straightforward then you should try to extend your app to add the following features:

#####Push to version control
Use Git to save your bartender file and push it to GitHub. If you skipped the pre-work, now might be a good time to [spend 15 minutes on Try Git](https://try.github.io/levels/1/challenges/1). Ask the instructor/TA if you aren't sure what to do, or if you want them to check you pushed to GitHub correctly.

#####Give the cocktails a name
All good cocktails should have a memorable name. Try to write a function which will name your cocktails. The name should be a random combination of an adjective and a noun (for example your bartender could make a "Fluffy Chinchilla", a "Salty Sea-Dog", or a "Fluffy Sea-Dog"). Think back to the superheroes, though you can use lists or dictionaries in the code for the adjectives and nouns.

#####Keep 'em coming
At the moment you can only get one drink at a time from the bartender. A well trained pirate bartender should offer his customer another drink when they've finished their previous one. Try adding a loop in the main function which will ask the customer whether they want another drink, and keep creating new recipes as long as they agree.

#####Stock control

Even pirate bars don't have a limitless supply of ingredients. You could add a stock count for each ingredient which decreases whenever the bartender makes a drink. Print a message to tell the bartender to restock the ingredients when supplies are low.