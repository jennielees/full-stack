---
layout: post
title: Ready, Set, Code!
week: 1
---

### Coding Kata

We'll be coding up our own web server next week, so let's make sure our skills are sharp!

#### Exercise: Superhero Names (Lists and Files)

First, download the [hero and villain names](/full-stack/public/data/names.txt) file. This should be a file ending in '.txt'. Move it to your Python working directory.

##### Part 1

Write a Python script which loads the names from the file, and converts your own name to a superhero (or supervillain) name by picking the name corresponding to your first name's position in the alphabet. For example, if your name starts with A, you want superhero name #1. Mine (J) is name #10.

Here's a snippet of code to help with the letter part of this:

```
import string
uppers = string.uppercase
print uppers
j_position = uppers.find('J')
```

(By the way, I want to point out that [Princess Python](http://en.wikipedia.org/wiki/Princess_Python) is a real character.)

##### Part 2

Use the `random.choice` and `split()` functions to pick a randomly-selected first name and second name.

<pre class="hint">
import random

beatles = ["John", "Paul", "George", "Ringo"]
# Print the name of a random Beatle
print random.choice(beatles)
</pre>

##### Part 3

Expand the superhero generator to avoid names where the first and last name are the same, such as 'Poison Poison'.

#### Exercise: BARRRtender


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

To choose an ingredient from one of the ingredient lists you can use the `random.choice` function again.

#####Provide a main function

Use `if __name__ == '__main__':` to run this function from the command line. The `main()` function should call your two functions in order, passing your list of preferences to the drink creation function. It should then print out the contents of the drink.

<pre class="hint">
# code
# code
# code
def main():
    # first piece of code you want to run in this file
    print "main"
    

if __name__=="__main__":
    main() 
# this means "if this is run from the command line, run the main() function"
</pre>

If this is getting odd results make sure that *all* your other code is inside functions so you don't end up accidentally running it when you run the file.

To run the file, it's just `python bartender.py` (or whatever you called it).

#####Discussion
Once you've completed the basic requirements for the project, feel free to take a look at [this sample solution](https://gist.github.com/jennielees/af968ee8b13805a350b8). Compare and contrast your solution. What do you like better about the sample? What do you like better about yours?

### Improve your Jedi Skills

If you complete both these exercises, or just want more practice, try Code Kata at [Cyber Dojo](http://cyber-dojo.org/).

Hit "create", select the "Python" language and then pick a problem. Hit "enter" to start the kata. Your goal is to create a function inside the `test` file that tests for, and solves, the problem. [This blog post](http://technologyconversations.com/2013/12/29/learning-a-new-programming-language-through-katas-tdd-and-cyberdojo/) breaks down the process in more detail.

