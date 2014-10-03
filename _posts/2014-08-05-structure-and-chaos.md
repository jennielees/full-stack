---
layout: post
title: Structure and Chaos
week: 2
---

### Fun with functions

_[Code from class walkthrough](https://gist.github.com/jennielees/d62581b38499ddc38266)_

We've already seen [functions](http://www.learnpython.org/en/Functions) around, but let's get more familiar with them.

What's a function? In short, they are a really good way of wrapping up some code in a neat bundle to run again or re-use.

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

You can imagine, the more you have to do something, the more attractive functions look. There are other reasons, too; putting your code in neat parcels makes it easier to understand, both for your future self and other people, and often saves a whole bunch of typing.

Take the code you wrote above to find when your street was being swept.

Turn it into a function -- without changing the logic, that's as easy as indenting it and adding a 'def'.

```
def sweep_times():
    #  your code here
```

Now to make sure this gets called, or executed, put the command `sweep_times()` in your code right after.

<pre class="hint">
def sweep_times():
    # your code here
    # by the way,
    # lines starting with a pound sign
    # (aka hash, if pound sign means £ to you)
    # are comments, which can contain anything
    
# to call the function, get out of the indent
# so python knows you are no longer telling it the
# function definition 
# then just invoke the function name

sweep_times()

# if you put this call before the 'def' part, python
# has no idea what you mean, as it steps through
# your file in order - try it!
</pre>

You can also check out the [Codecademy section on functions](http://www.codecademy.com/courses/python-beginner-c7VZg/0/1?curriculum_id=4f89dab3d788890003000096) and/orr [Learn Python the Hard Way 18 and 19](http://learnpythonthehardway.org/book/ex18.html) for more context and practice with functions.

### Parameters (not parking meters)

That's great but your function only does one thing. Fortunately those brackets are just waiting to be filled with a *parameter*, or two...

Parameters let your function take a piece of input and use it locally. Think back to math and f(x): it's the same principle.

Here's a simple function, complete with parameter:

```
def print_hello(name):
    print "Hello, {name}".format(name=name)
```

To call the function, give it something to do:

```
print_hello("Lady Gaga")
print_hello("Benedict Cumberbatch")
```

What happens if you put a number instead of a string inside the parentheses? What if you don't put anything?

### An argumentative interruption

    A: Your function takes a parameter?
       How strange, mine takes an argument!
    B: What, that? You call that an argument?
       That's not an argument.
    A: Oh yes it is!
    B: Oh no it isn't!
    A: *This* is an argument.
    B: Exactly.

In programming sometimes people get very caught up on specific definitions. Here's one of them.

A parameter's the thing in the function definition itself, so the word 'name' in `print_hello(name)` earlier.

An argument is the value you put in *when you call the function*, so the string (e.g. "Benedict Cumberbatch") itself.

Within the function, the argument you put in gets assigned to the variable you defined in the brackets. This works up to as many arguments as you can handle.

```
def many_things(one, two, three, four, five, six):
    print "I have one {one}, two {two}s, three {three}s, four {four}s, five {five}s and six {six}s.".format(one=one, two=two, three=three, four=four, five=five, six=six)

many_things("nose", "ear", "piercing", "limb", "sense", "cousin")
```

What kind of error do you get if you forget an argument? What if you put one extra in? (You'll see these kinds of errors more than you'd think, so get a feel for them!)

### Parameter Street

Re-define your street sweeping function to take a parameter, `street_name`, and use this instead of the hardcoded street name you were using before.

You should be able to call this successfully:

```
sweep_times("Sutter St")
```

and see a print-out of the days this street is swept.

What happens if the street isn't in the sweep.csv list?

(Stuck? Check this [gist out](https://gist.github.com/jennielees/ca5d6a23836b107b31ce) for a skeleton.)


### Command-line parameters

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

### Dictionary Corner

What's a dictionary? When is it used? What parallels does it have to other things (e.g. Javascript/JSON)?

Check out [this piece on dictionaries](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise06) to find out this, and more. We'll discuss in class, too.

Keys and values crop up all over the world of programming, so you've probably seen something similar already, even if you didn't realise it.

A dictionary is Python's term for a key-value store, and it's just as it sounds: a way to map *key* terms into *values*.

A simple dictionary (or 'dict' for short) looks like this:

```
leet_skillz = {
    'halo': 10,
    'starcraft': 4,
    'hearthstone': 7,
    'solitaire': 11,
    'simcity': 9
    }
```

The colon separates the key from the value.

Values can be any kind of Python data type, and we'll see more complex examples of this soon!

How do you use this? Finding an element is similar to a list, but with a string key, not an integer:

```
print leet_skills['simcity']
```

You can also use the `get()` function which behaves itself much more nicely if the key isn't actually there.

```
awesome = leet_skillz.get('halo')
oops = leet_skillz.get('callofduty')
print awesome
print oops
```

Adding items to a dictionary is nice and simple:

```
leet_skills['bridge'] = 8
```

Now there's a new entry. If something was already there, it got overwritten. You can also use a variable as the key:

```
best_game_ever = "dominion"
leet_skills[best_game_ever] = 4
```

Why do we use dictionaries?

For one, they make it much easier to lump data together and access it with a friendly name. There are also a lot of places where you want to keep track of two (or more) things at once, and a dictionary saves you from trying to keep track of where you are in a bunch of different lists. Thanks, dictionaries!

### DictReader, csv.reader's mortal enemy

Move over `csv.reader`, we've got a new BFF.

```
import csv

with open('sweep.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print row
```

What `DictReader` does is take the first row of the CSV and turn it into keys for a dictionary. Then every row is mapped on to those keys, rather than a plain old list.

In miniature:

```
$ cat mini.csv
WEEKDAY,STREET,ZIP
Mon,Sutter St,94102
Wed,Sutter St,94102

# each row becomes a list with csv.reader:
>>> print row
['Mon', 'Sutter St', '94102']
>>> print row[0]
'Mon'

# but a dict with csv.DictReader
>>> print row
{'WEEKDAY': 'Mon', 'STREET': 'Sutter St', 'ZIP': '94102'}
```

* Update your sweeper script to use `DictReader` instead of `csv.reader`.
* Can you use the following to rewrite your days of the week script more effectively?

```
days_counts = {
	'Mon': 0,
	'Tue': 0,
	...
	}
```

Hints:

```
days_counts[row['WEEKDAY']]
# will get you days_counts['Mon'] if row['WEEKDAY'] is 'Mon', and so on.

days_counts.get(key, 0)
# will give you the value if it's there, and 0 if it isn't.

```

### It's date time!

Goal: Let's write a function that takes a street name and tells you if it is going to be swept tomorrow.

*Note: when you make a million on the App Store from this, just remember who suggested it...*

#### Today

Time to meet the delight that is `datetime` in Python.

There are a million ways you can write dates and times out, they vary internationally, and not to mention we have the joy of timezones to deal with. Why write your own code to handle all this when there is a pre-built set of code you can use? The `datetime` library provides a lot of handy utilities to work with dates and times (yeah!) but is definitely something it can take a little time to figure out. 

`datetime` provides several submodules:

* `datetime.date` (just dates)
* `datetime.time` (just times)
* `datetime.datetime` (dates and times)
* `datetime.timedelta` (the difference between two times)

We care about dates and times, so let's use the `datetime.datetime` library. You need to write the full statement `from datetime import datetime` to use it.

Here is a `datetime` crash course: try it!

```
from datetime import datetime

now = datetime.now()
# now is a datetime object, set to the local system time. if you print now, you'll see its native form.

day = now.day
print day
>>> 3
# Days of the week are numeric and start from 0.

human_day = now.strftime("%a")
print human_day
>>> 'Wed'
# strftime turns computer dates into strings.

```
[strftime](http://strftime.org/), short for string-format-time, is a handy way of turning a native `datetime` into something more human-friendly. Its syntax is a little kooky but persevere and you'll be rewarded.

Conveniently, the `%a` formatter, for 'abbreviated day of week', is the same format our street sweeping data is in. Neat.

You can get more hands-on with `datetime` with [this Codecademy exercise](http://www.codecademy.com/courses/python-beginner-en-zFPOx/0/1).

### Tomorrow

The `datetime` module's `timedelta` is really handy if we want to add times to dates (or subtract).

```
from datetime import datetime, timedelta

one_week = timedelta(days=7)
today_next_week = datetime.now() + one_week
print today_next_week
print today_next_week.strftime("%a %d %b %Y")
```

Here's a wee helper:

```
from datetime import datetime, timedelta

def tomorrow_day():
    now = datetime.now()
    one_day = timedelta(days=1)
    return (now + one_day).strftime("%a")
```

The *return* keyword means that you can assign the function to a variable, and you'll get something back if all goes well:

```
day_to_check = tomorrow_day()
print day_to_check
```

You've actually been using return a lot already, just not explicitly. Functions like `datetime.now()` return a value!

Back to the original question: taking a street name, tell me whether it's going to be swept tomorrow, and if so, which house numbers should be wearing earplugs or moving their cars.

Expand this to not only check the 'WEEKDAY' column but also check the week of the month, if your street varies on different weeks (if not, find one that does).


#### A CSV of your own

Pick a CSV of your own to work with. Explore it the same way you did the street sweeping data, and work with the instructor/TA to identify a small script you could write to use the data.

One example is exporting and cleaning up your address book.
