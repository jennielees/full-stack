---
layout: post
title: Week 3 Extra Credit
week: 3
permalink: week-3-extra/
---

#### Resources

* [Learn Python the Hard Way - raw_input](http://learnpythonthehardway.org/book/ex11.html)
Dictionaries
* [Learn Python the Hard Way: Dictionaries](http://learnpythonthehardway.org/book/ex39.html) (last section is advanced)
* [Hackbright: files and dictionaries](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise07)

* [Codecademy: Datetime](http://www.codecademy.com/courses/python-beginner-en-zFPOx/0/1)
* [Python Module of the Week: Datetime](http://pymotw.com/2/datetime/)

* (Advanced) [Khan Academy: Recursive Fibonacci](https://www.youtube.com/watch?v=urPVT1lymzU&index=18&list=PL36E7A2B75028A3D6)
* (Advanced) [Lambda Tutorial](http://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/)

#### Extra Credit

* What does `if __name__=="__main__"` do? [Why](http://stackoverflow.com/a/20158605/3508332)?


* Update your `sweep_today` or `sweep_tomorrow` function to be more general. It should look like this:`sweep_day(number, street, day)` and return `True` if that block is swept on that day. Can you write out your test day of week function calls with this extra parameter?

* Extend `sweep_day` to also take a week of the month argument, e.g. 1 or 3.

* **Advanced** (datetime / math) Figure out how to check which week of the month it is right now, and pass that into `sweep_day`. You will need to think about when the first Monday in the month is, compared to today.

* **Advanced** (string manipulation) Update `sweep_day` to allow other ways of typing the day name. Helper:

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

* Use the `raw_input()` function to get input from a user instead of a command line argument. It helps if you've done the step before, as you can't expect users to always put 'Mon' for 'Monday'!

  Intros to `raw_input()`:

  * [Hackbright Guessing Game](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise01)
  * [Learn Python The Hard Way: raw_input](http://learnpythonthehardway.org/book/ex11.html)
  