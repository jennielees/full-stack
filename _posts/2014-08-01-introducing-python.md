---
layout: post
title: Introducing Python
week: 1
---

####Hello, Python

Open up a terminal window.

Type in `python`.

You'll get something that looks like this:

```
Python 2.7.6 (default, Feb 20 2014, 22:44:16)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.2.79)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

(If you don't, flag down a TA!)

You can type anything in here and Python will try to immediately run it. For example, try typing in:

```
>>> 3 + 4
```
(Note: Where you see `>>>` here, that represents the prompt from Python. Don't type the arrows in.)

What do you get? What if you change the spacing around? Can you do other math operations? ([Wikibooks](http://en.wikibooks.org/wiki/Python_Programming/Operators) might be helpful.)

Get Python to tell you:

* How many seconds are in a year
* Your lucky number (your zipcode plus your birth month squared)

#####Interlude: True Division Is Not A Band

Actually, you don't really need to know that it's called "true division", it's really just "division". But this is an annoying little thing that trips people up all the time. (By the way, [Joy Division](https://www.youtube.com/watch?v=zuuObGsB0No) are fab. Check them out sometime.)

Let's consider the following question:

**How many MUNI rides can I take before my Clipper card is empty?**

The MUNI fare just increased (or should have), so this seems pretty obvious.

Let's say my Clipper balance is $25:

```
>>> clipper = 25
```

And rides cost $2.25 each.

```
>>> fare = 2.25
```

To get the number of rides it's simple napkin math:

```
>>> clipper / fare
```
This should print out a number, but it's pretty ugly. And unrealistic: you can't take point zero whatever of a MUNI ride (try explaining that to the driver...)

Here's some Python fun: what if we go back to the old $2 fare?

```
>>> fare = 2
>>> clipper / fare
```
Hint: you can press the up arrow to find something you previously typed.

Do the math in your head. What's Python doing?

What if the clipper balance isn't a round number, like $20.14?

Round numbers are called 'integers' or `int` in code, and decimal numbers with something after the point are called 'floating-point' or `float`. The point is 'floating' because there can be any number of things to the right of it.

Try turning your integers into floats and running the exact same code:

```
>>> clipper = float(25)
>>> fare = float(2)
>>> clipper / fare
```

Anything different? What if you only do one at a time? What do you think is happening here?

####A variable by any other name

See how above we didn't have to type out the Clipper value multiple times? We've sneakily used a thing called a *variable*. Variables are really important in Python: they're how you store stuff so you can do stuff to it later. Think of them like named boxes where data lives. All you have to do is mention the name and you get access to everything in the box.

Variables are also an important form of communication. We can understand what's going on when we read `clipper divided by fare` much more easily than we can `number divided by number`. Giving your variables friendly names is a very Python-y thing to do.

Variable names can't have spaces in them, so you'll often see underscores used instead:

```
>>> variable_one = 1
>>> variable_two = 2
```

and so on. To see what's stored in a variable, in the Python interpreter, just type its name:

```
>>> clipper
```

Cool, it's still there. What happens if you type the name of a something that doesn't exist?

You can also explicitly tell Python to `print` something out. This works with a variable name or an expression (anything, like the addition and division examples, that works out to a value).

```
>>> print clipper
>>> print (clipper * 2)
```

Do brackets and spacing make a difference?

####Bad Things Can Happen

Like running out of Clipper cash before the last MUNI ride home.

Let's say that when my balance falls below $5.00 I have to go top it up. Can we write a program that might simulate taking some rides, and warn me when a top-up is imminent?

Yes we can!

Recap:

```
>>> clipper = 25
>>> fare = 2.25
```

Let's define a _function_ to take money off my card. The `def` (short for 'define') keyword is used for functions.

```
>>> def take_a_ride(start_balance):
>>>     new_balance = start_balance - fare
>>>     return new_balance
>>>
```
This doesn't do anything immediately but let's see what happens when we try using it:

```
>>> take_a_ride(clipper)
```
The value of `clipper` hasn't changed, so we need to do one more thing to actually put it back.

```
>>> clipper = take_a_ride(clipper)
```

**Discussion**: We'll stop and discuss this in class.

If you press your up-arrow key a few times you'll see the flaw in this system. I can go way past my balance warning point. Let's update `take_a_ride` to be more demanding.

```
>>> def take_a_ride(start_balance):
>>>     new_balance = start_balance - fare
>>>     if new_balance < 5:
>>>         print "Warning: Need to top up!"
>>>     return new_balance
>>>
```

Try running this on a balance just above 5:

```
>>> take_a_ride(6.00)
```
We'll come back to `if` later. Try writing another `if` to print a more menacing message if the balance goes below zero.

####Let's break things

Prize for the most interesting error message! We'll walk through the errors together and explain what Python is trying to do.

Hints:

* Experiment with punctuation and spelling
* Think of variable names Python might not like very much
* Find something Python doesn't want to print
