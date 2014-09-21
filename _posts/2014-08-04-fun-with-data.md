---
layout: post
title: Fun with Data
week: 2
---


#### Comma Separated Victory

Let's look at some real data!

**Discussion:** Talking about sweep.csv and what's in it.

Get the `sweep.csv` file from [here](/python-codelabs/public/data/names.txt). CSV, short for comma-separated value, is a common format and many places can give you CSV data to work with, including your friendly local spreadsheet program.

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

##### csv.reader, your new best friend

Python has a whole bunch of built in libraries that do cool stuff. `csv` is one of these (remember `random` from last week?). When you `import csv` you get access to `csv.reader`, which creates a csv reader from your file. You can then loop through the `reader` object and get a nicely-formatted row back.

As with many Python built in libraries, the official documentation here is [pretty intense](https://docs.python.org/2/library/csv.html). However, heading to the [examples](https://docs.python.org/2/library/csv.html#examples) section is actually a useful way to learn more about this library.

```
import csv

with open('sweep.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
```

Note: The `reader` object is a special kind of [iterator](http://anandology.com/python-practice-book/iterators.html), and not the same as a list. If you want to access this data separately from a for loop, you'll need to load it into a new list first.

For example, if you wanted to get all the neighborhoods from the csv, using `csv.reader`:

```
import csv

neighborhoods = []

with open('sweep.csv') as f:

    reader = csv.reader(f)

    for row in reader:

        neighborhood = row[-2]
        # Negative means count from the right, which is easier here

        if neighborhood not in neighborhoods:
            # Append it to the list!
            neighborhoods.append(neighborhood)

print "Found {} neighborhoods".format(len(neighborhoods))
print sorted(neighborhoods)

```

_By the way, it's really hard typing 'neighborhood' as a Brit. Just saying'._

Experimenting:

* Is the `reader` object like a list? Can you access row 30 of the reader? (What happens if you try `reader[30]`?)
* Is the `row` object like a list? Can you access item 5 of a row? (What happens if you try `row[5]`?)


##### When is SF at its cleanest?

Using this data (either method), let's see if we can figure out the most popular day of the week for street sweeping. In the individual rows, this is the second item (`row[1]`).

Write this in a file called `sweep.py`, as you'll save yourself typing as we continue. When you get it working, check it into Git, as you may change it for the next bit.

Hint: One way to do this would be to use a variable for each day:

```
monday = 0
tuesday = 0
...

if row[1] == "Mon":
    monday += 1
```

`+=` is a shortcut for a variable adding 1 to itself.

Do you notice anything slow, or error-prone about this approach?

Let's move on to look for a specific piece of information.

#### Exploring the streets

Also known as "Fun with `if`".

Update `sweep.py` to print out answers to the following questions.

* Find your street name (or a street you like)
* Which day(s) of the week is your street swept?
* Which week(s) of the month?
* Can you identify which day your specific section of the  street is swept? (The columns LF_FADD and LF_TOADD specify left-side from and to numbers; RF_FADD and RF_TOADD similarly the right-side.)

Extra credit: Explore the file a little before trying to answer these questions. It always helps to be able to answer them without a program, or at least have some idea how!

As well as your usual file viewers, see if you can figure out what these commands do in Terminal:

* `head sweep.csv`
* `tail sweep.csv`
* `grep Sutter sweep.csv`
* `grep Sutter sweep.csv | less` (tip: hit space to continue, or q to exit)


#### Fun with functions

**Discussion:** Functions and parameters.

We'll talk about [functions](http://www.learnpython.org/en/Functions), but at the highest level, they are a really good way of wrapping up some code in a neat bundle to run again or re-use.

What does a function look like? With one, your code can move from

```
do this
do that
do this
do that
do this
```

to:

```
def do_this():
    do this
    do that

do_this()
do_this()
do_this()
```

You can imagine, the more you have to do something, the more attractive functions look. There are other reasons, too; putting your code in neat boxes makes it easier to understand, both for your future self and other people, and often saves a whole bunch of typing.

Take the code you wrote above to find when your street was being swept.

Turn it into a function -- without changing the logic, that's as easy as indenting it and adding a 'def'.

```
def sweep_times():
    #  your code here
```

Now to make sure this gets called, or executed, put the command `sweep_times()` in your code right after.

##### Parameters (not the kind of meters with maids)

That's great but your function only does one thing. Fortunately those brackets are just waiting to be filled with a *parameter*, or two...

Parameters let your function take a piece of input and use it locally. Think back to math and f(x): it's the same principle.

Here's a simple function, complete with parameter:

```
def print_hello(name):
    print "Hello, {name}".format(name=name)
```

To call the function, give it something to do:

```
print_hello("Jennie")
print_hello("Benedict Cumberbatch")
```

What happens if you put a number instead of a string? What if you don't put anything?

##### An argumentative interruption

    A: Your function takes a parameter?
       How strange, mine takes an argument!
    B: What, that? You call that an argument?
       That's not an argument.
    A: Oh yes it is!
    B: Oh no it isn't!
    A: *This* is an argument.
    B: Exactly.

A parameter's the thing in the function definition itself, so the word 'name' in `print_hello(name)` earlier.

An argument is the value you put in *when you call the function*, so the string (e.g. "Benedict Cumberbatch") itself.

Within the function, the argument you put in gets assigned to the variable you defined in the brackets. This works up to as many arguments as you can handle.

```
def many_things(one, two, three, four, five, six):
    print "I have one {one}, two {two}s, three {three}s, four {four}s, five {five}s and six {six}s.".format(one=one, two=two, three=three, four=four, five=five, six=six)

many_things("nose", "ear", "piercing", "limb", "sense", "cousin")
```

What kind of error do you get if you forget an argument? What if you put one extra in? (You'll see these kinds of errors more than you'd think, so get a feel for them!)

##### Parameter Street

Re-define your street sweeping function to take a parameter, `street_name`, and use this instead of the hardcoded street name you were using before.

You should be able to call this successfully:

```
sweep_times("Sutter St")
```

and see a print-out of the days this street is swept.

What happens if the street isn't in the sweep.csv list?

(Stuck? Check this [gist out](https://gist.github.com/jennielees/ca5d6a23836b107b31ce) for a skeleton.)


#### Command-line parameters

When you run your program itself, it has parameters! The system incantation `sys.argv` (for 'argument values') is a handy way of looking at the parameters supplied when you run the file.

```
python myfile.py one two three
       ^^^^^^^^^^^^^^^^^^^^^^^
       these are all arguments to the 'python' command!
```

Try creating a really simple file, `myfile.py` which just contains the following:

```
import sys

print sys.argv
```

What happens when you run it like above?

How would you get at the argument 'one' in the example?

Can you extend your `sweep_times` file to take a command line argument, e.g.

```
python sweep.py "Sutter St"
```

What happens if you forget the quotes?
