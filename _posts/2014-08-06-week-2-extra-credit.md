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