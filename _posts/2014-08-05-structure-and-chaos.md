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

<pre class="hint">
import sys

print sys.argv[1]

my_street = sys.argv[1]
</pre>

Can you extend your `sweep_times` file to take a command line argument, e.g.

```
python sweep.py "Sutter St"
```

<pre class="hint">
import sys

print sys.argv[1]

my_street = sys.argv[1]

...
...
...

check_street(my_street)
</pre>

What happens if you forget the street name? How could you use `except` to exit gracefully in this case?

<pre class="hint">
import sys

try:
    my_street = sys.argv[1]
except:
    print "!! I need a street name !!"
    exit()
    
# following code won't get run if you exit()
</pre>

What happens if you forget the quotes? (Not good things.)

<pre class="hint">
import sys

print sys.argv
# if you run (from Terminal)
# python sweep.py Sutter St
# you should see
# ['sweep.py', 'Sutter', 'St'] in the list
# argv looks for spaces and will split up things that aren't in quotes!
</pre>
