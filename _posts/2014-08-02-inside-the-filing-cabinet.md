---
layout: post
title: Inside the Filing Cabinet
---

Getting ready: Make a directory somewhere you can get back to easily, calling it something like `hackbright`, then make a `week1` subdirectory for this week's projects.

#### Reading a file

Let's do something more interesting than playing around with variables!

First, download the [hero and villain names](/python-codelabs/data/names.txt) file. This should be a file ending in '.txt'. Move it to your Python working directory. 

Here are two filesystem superpowers you can try:

* Open up Terminal and move it from there! 
 
  `mv ~/Downloads/names.txt .` is shorthand for "move the file called 'names.txt' in my Downloads folder, within my home directory (`~`) to the directory I am currently in (`.`)"
  
* Download it directly to the directory: open Terminal and navigate (change directory, `cd`) to your `week1` directory and then use the `curl` [command](http://en.wikipedia.org/wiki/CURL) to download it to a file:

  `curl -O http://jennielees.github.io/python-codelabs/data/names.txt`

  The `-O` means 'output to a file' so you should see a file called `names.txt` in your directory once you're done. Check by typing in `ls` to list files.

Once you have `names.txt` handy and you are in a terminal, open up Python again (just type `python`).

Let's look at the file!

##### Opening a file

Try opening the file up in Python by using this slightly-backwards syntax:

```
>>> with open('names.txt') as f:
>>>     data = f.readlines()
>>>
```

Notice how there is a colon at the end of the 'with' line, and the line below is indented four spaces? You have to type an empty line to finish this piece of code up, too.

Welcome to Python.

This structure is called a 'block' and is used everywhere in Python. Literally. Everywhere. 

**Discussion:** We'll talk more about blocks and indentation in class.

The above code didn't actually _do_ anything, it just read all the lines in the file and put them in a variable called 'data'. To get it out, we need to ask Python what's in 'data':

```
>>> print data
```

Ugh! Let's break down what that output was. You probably saw something like this:

```
['Black Widow\n', 'Wonder Woman\n', ...]
```

First things first, `\n`. This is a special character for the 'newline', marking that the next thing printed should be at the start  of the next line. When you read in a file, especially with `readlines`, you often get these pesky newlines sticking around. Don't worry though, Python has many ways to get rid of them!

Secondly, the square brackets. 

This is a Python **list**. Lists are super useful and crop up a lot. It's pretty much what it sounds like: a list of stuff.

**Discussion:** We'll talk about lists in class, and what you can and can't do with them.

One thing you can do with a list is **loop through it**:

```
>>> for name in data:
>>>    print name
>>>
```

Cool! But let's get rid of those newlines (since `print` itself adds a hidden newline, so you get double-spacing).

Try changing `name` to `name.strip()`:

```
>>> for name in data:
>>>    print name.strip()
>>>
```

(By the way, I want to point out that [Princess Python](http://en.wikipedia.org/wiki/Princess_Python) is a real character.)

The `strip()` function is a really handy one that gets rid of any spaces or hidden `\n` characters, but only on the outside.

```
>>> name = "  Space Monster  "
>>> name.strip()
>>> name = "Space     Monster"
>>> name.strip()
```

That's all well and good but our original `data` list hasn't changed.

Let's try:

```
>>> for name in data:
>>>     name = name.strip()
>>> 
>>> print data
```
 
Huh?

**Discussion:** We'll talk about _scopes_ and how the `for` keyword works.

Once you've cleaned up the list, let's do something with it. How about just putting it in alphabetical order?

```
>>> data = sorted(data)
```

(If you want to keep the original list around, you can assign the sorted version to another name.)

#### Writing to a file

Writing's very similar to reading. One big difference is that you have to tell Python you want to write the file; by default, `open` assumes you want to read it.


```
>>> with open('output.txt', 'w') as f:
>>>     f.writelines(data)
```

If you open up 'output.txt' you'll notice everything's on one line. Yup, those newlines were actually pretty useful after all. Can you figure out how to write the file with newlines in it?
 
Warning: if you run code again with the same filename, this will replace the contents of the file. That's usually what you want to do, but Python won't warn you about it in case it isn't.

#### Saving your code in a file

Since we're on files, let's try getting out of the Python interpreter and putting our code in a file as well!

Open up a text editor and put the file-reading code in it:

```
with open('names.txt') as f:
    data = f.readlines()
    
stripped = []
for name in data:
    stripped.append(name.strip())

data = sorted(stripped)

print "The names are:"
for name in data:
    print name
```

Save this file with a memorable name, like `superheroes.py`. Adding '.py' to the end means it's a Python file.

To run the file, switch back to your terminal and type:

```
python superheroes.py
```

If it didn't work, check the file is actually there (and your editor didn't add a second file extension like .txt on the end); that `python` by itself works; that you used consistent indentation in the file; look for typos or extra brackets.


#### Diversion: Inception!

What happens if you change the file you're reading to be `superheroes.py` instead of `names.txt`? Can the file read itself while it's running?

#### Superhero Generator

#####Version 1

Convert your name to a superhero (or supervillain) name by picking the name corresponding to your first name's position in the alphabet. For example, if your name starts with A, you want superhero name #1. Mine (J) is name #10.

Letter Helper:

```
import string
uppers = string.uppercase
print uppers
j_position = uppers.find('J')
```

What do you think `find` does? Why is `j_position` 9 and not 10?

**Discussion:** We'll discuss strings, and talk about what "import" means.

List Helper: To access an item in a list at a specific position, use square brackets:

```
list = ['a', 'b', 'c']
print list[0]
print list[2]
print list[3]
```

Lists start counting at zero.

How can you put this together with the `data` list you already have to find the right item?

##### Version 2

Let's get this party rolling. Instead of using boring pre-existing super* names, we'll randomize to create our own!

Split the existing names into two lists, corresponding to the first word and second word.

Hint: the `split()` function turns a string into a list, splitting it up by whatever's in the brackets.

```
name = "John Doe"
name_pieces = name.split(" ")
print name_pieces
first_name = name_pieces[0]
```

Once you have two lists, you need to pick randomly from each one.

Fortunately, Python has a handy utility for that.

```
import random
random.choice(list)
```

How might you combine the two names? Try just printing them both out. With two `print` statements you end up on two lines, but combining them on the same line is a feast of choice.

Some of the `print` options:

```
print first_name, last_name
print first_name + " " + last_name
print "{} {}".format(first_name, last_name)
print "{first} {last}".format(first=first_name, last=last_name)
```

**Discussion** We'll talk about printing strings out.


#### Comma Separated Victory

Let's look at some real data!

Get the `sweep.csv` file from [here](/python-codelabs/data/names.txt). CSV, short for comma-separated value, is a common format and many places can give you CSV data to work with, including your friendly local spreadsheet program.

* Read in the data from `sweep.csv` using `readlines()` and use `split(',')` to examine it.
* This is a nearly 40,000 line file, so let's use the `[:]` operator to access part of the list:

```
with open('sweep.csv') as f:
    data = f.readlines()

for line in data[:3]:
    print line.split(',')
```

`data[:3]` accesses the part of the list from items 0 to 3, which is a bit more manageable.

This method works for a 'clean' CSV, but .csv files are so common and varied that Python has a way of accessing them more easily, to deal with different standards. For example, the `split` call above fails if there is a comma inside one of the items.

```
import csv

with open('sweep.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
```

If you want to access a subset of this data, you'll need to load it into a new list first.

Using this data (either method), let's see if we can figure out the most popular day of the week for street sweeping. In the individual rows, this is the second item (`row[1]`).

One way to do this would be to use a variable for each day.

```
monday = 0
tuesday = 0
...

if row[2] == "Mon":
    monday += 1
```

`+=` is a shortcut for a variable adding 1 to itself.

We'll discuss more about this dataset next week: think of interesting things you might want to do with it!