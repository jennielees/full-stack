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

### Extra Credit/Further Exercises

* Exercise to get more practice with files, loops, and lists: [Count the letters in a file](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise05).

* What does `if __name__=="__main__"` do? [Why](http://stackoverflow.com/a/20158605/3508332)?


####Street Sweeping Extensions

* Extend your `sweep_times` function to take a street number and name, e.g. `sweep_times("Sutter St", 683)`.

* Create a list called `favorite_streets` and figure out how to run `sweep_times` on every street in the list.

* Take a command line argument (remember `argv`?) and break out the house number from the street name, calling `sweep_day` with these and tomorrow's day and week number. Take the result you get back from `sweep_day` and print an appropriate message.

Here's a helper:

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