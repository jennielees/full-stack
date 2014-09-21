---
layout: post
title: Putting it Together
week: 3
---

#### Snippets: stage one of the robot brain

We're going to build an app to keep track of useful code snippets. Hopefully this will even turn out to be something you actively use!

Create a new `snippets` directory, and `git init` a new git repository.

##### Logging: it's like spying but legal

The `logging` module makes it easier to see what's going on in our script.

Inside the `snippets` directory create a file `snippets.py` and kick it off:

```
import logging
import csv

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)
```

This means that any DEBUG level (or higher) messages will get written to 'output.log'.

Why bother with this? It's possible to develop without `logging`, but you'll find yourself with a bunch of `print` statements that you're constantly commenting out. Best to use `logging` and handle it properly.

##### Constructing the snippets app

**Discussion**: App design and brief.

* Function to put a snippet to a csv
* Command line arguments: Design interface with class
* input()
* Input parser
* Main function
* 'Test' function that prints out the csv contents
* Catching bad input with exceptions - 'good exceptions'
* Designing the csv

* Write snippets into csv
* Loading up snippets back from the csv

* Errors and exceptions
  * Using them for good

* Possibly start hinting about databases and basic sql?
