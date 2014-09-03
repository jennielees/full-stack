---
layout: post
title: Week 2 Extra Credit
---

#### Resources

* [Python CSV official documentation](https://docs.python.org/2/library/csv.html)
* [Python Module of the Week: CSV](http://pymotw.com/2/csv/)
* [Codecademy: Functions](http://www.codecademy.com/courses/python-beginner-c7VZg/0/1?curriculum_id=4f89dab3d788890003000096)
* [Learn Python the Hard Way: Functions](http://learnpythonthehardway.org/book/ex18.html)
* [Hackbright: Dictionaries](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise06)
* [Learn Python the Hard Way: Dictionaries](http://learnpythonthehardway.org/book/ex39.html) (last section is advanced)
* [Hackbright: files and dictionaries](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise07)
* [Codecademy: Datetime](http://www.codecademy.com/courses/python-beginner-en-zFPOx/0/1)
* (Advanced) [Khan Academy: Recursive Fibonacci](https://www.youtube.com/watch?v=urPVT1lymzU&index=18&list=PL36E7A2B75028A3D6)
* (Advanced) [Lambda Tutorial](http://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/)

#### Extra Credit

* What is loosely coupled code? Why might it be a good idea? When is it a bad idea?

* What does `if __name__=="__main__"` do? [Why](http://stackoverflow.com/a/20158605/3508332)?

Street Sweeping

* Extend your `sweep_times` function to take a street number and name, e.g. `sweep_times(683, "Sutter St")`.

* Create a new function, `sweep_day(day, number, street)` which prints out "Yes" if the street is swept on the day provided, and "No" if it is not. You can assume for now that the day will be in the same format as the data, e.g. "Mon" for Monday.

* Extend `sweep_day` to also take a week of the month argument.

* Create a list called `favorite_streets` and figure out how to run `sweep_times` on every street in the list.

* Update `sweep_day` to return a `True` or `False` value.

* Take a command line argument and break out the house number from the street name, calling `sweep_day` with these and tomorrow's day and week number. Take the result you get back from `sweep_day` and print an appropriate message.

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
 