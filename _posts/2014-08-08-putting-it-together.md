---
layout: post
title: Putting it Together
week: 3
---

## DictReader, csv.reader's mortal enemy

Now we know all about dictionaries, we can make working with CSV files a lot more interesting. Well, a little more interesting. Move over `csv.reader`, we've got a new BFF.

```
import csv

with open('sweep.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if reader.line_num < 10: 
            print row
```

What `DictReader` does is take the first row of the CSV and turn it into keys for a dictionary. Then every row is mapped on to those keys, rather than a plain old list.

In miniature (remember the `cat` Terminal command prints the contents of a file to screen) -- you can make your own `mini.csv` file or get it [here](/public/data/mini.csv):

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
* Can you use the following to rewrite your days of the week script more effectively, without all the `if` statements? (Start [from here](https://gist.github.com/jennielees/72029eadf4a58221a980) if you have changed your script since then.)

```
days_counts = {
	'Mon': 0,
	'Tue': 0,
	...
	}
	
print days_counts['Mon']
```

Hints:

```
day = row['WEEKDAY']
print day

count = days_counts[day]
print "days_counts key is {} and value is {}".format(day, count)

days_counts[day] += 1
# adds 1 to whatever is in the days_counts dictionary
# after looking up the key in the day variable
# so if day is 'Mon', it adds 1 to days_counts['Mon'], etc.

# or you can put them together:
days_counts[row['WEEKDAY']]
# will get you days_counts['Mon'] if row['WEEKDAY'] is 'Mon', and so on.
```

Here's an [example version](https://gist.github.com/jennielees/b6efcdcdec4822b78d0c) of the street counts using a dictionary; feel free to check your work against it and ask the instructor about any differences you see. Uncomment the `print` statements for more insight into what's going on.

## It's date time!

Goal: Let's write a function that takes a street name and tells you if it is going to be swept tomorrow. To start with, we will ignore the weeks of the month and just look at the day.

*Note: when you make a million on the App Store from this, just remember who suggested it...*

### Knowing when we are right and wrong

Before we jump into this function, let's set up what we want to do. You should already have a function that takes a street name and prints out when it is swept. Start from there (or compare your code to [this dictionary version](https://gist.github.com/jennielees/74b73e0978f27ab211b0)).

What we are trying to get to is something like:

```
def swept_tomorrow(street_name, house_number):
   if this_part_of_street_will_be_swept_tomorrow:
       return True
   else:
       return False
```

We can expand what it does later, such as telling us which side is swept.

First of all, we need to make sure we have some idea of a **right answer**. That is, an input we can give this function where we know what the output should be.

Look in `sweep.csv` (you can go back to some of the code you already wrote and run it, or check the [Google Docs version](https://docs.google.com/a/hackbrightacademy.com/spreadsheets/d/1xmj93394Ce0ImkJtufKeU_IMT8tqG0l4Nm_R3Dha86U/edit?usp=drive_web)) and find a block of a street that is **definitely swept today** and another that is **definitely swept tomorrow**. (Continuing to ignore the weeks of the month for now.)

Now find something that **definitely isn't swept today**, and another that **definitely isn't swept tomorrow**. It doesn't matter if they are swept on other days of the week.

The easiest way to find these is to find streets that are only swept on one day, but blocks of larger streets are fine if you are sure they fulfil the criteria. Often a single block will have different sweeping days for each side.

<pre class="hint">
87 Coral Rd is swept on Mondays only.
60 Fanning Way is swept on Tuesdays only.
50 Delmar St is swept on Wednesdays and Fridays.
33 Vesta St is swept on Tuesdays and Thursdays.
77 Dukes Ct is swept on Fridays only.
</pre>

Now write out what you expect to happen so you can test your code works later. For example:

```
result = swept_tomorrow("Coral Rd", 87)
print "If tomorrow is Monday, this should be True: {}".format(result)
```

## Knowing whether it's today or tomorrow

Time to meet the delight that is `datetime` in Python.

There are a million ways we write dates and times out, they vary internationally, and not to mention we have the joy of timezones to deal with. Why write your own code to handle all this when there is a pre-built set of code you can use? The `datetime` library provides a lot of handy utilities to work with dates and times (yeah!) but is definitely something it can take a little time to figure out. 

`datetime` provides several submodules:

* `datetime.date` (just dates)
* `datetime.time` (just times)
* `datetime.datetime` (dates and times)
* `datetime.timedelta` (the difference between two times)

We care about dates and times, so let's use the `datetime.datetime` library. You need to write the full statement `from datetime import datetime` to use it.

Here is a `datetime` crash course: try it!

```
>>> from datetime import datetime

>>> now = datetime.now()
# now is a datetime object, set to the local system time. if you print now, you'll see its native form.

>>> day = now.weekday()
>>> print day
1
# Days of the week are numeric and start from 0.

human_day = now.strftime("%a")
print human_day
>>> 'Wed'
# strftime turns computer dates into strings.

```
[strftime](http://strftime.org/), short for _string-format-time_, is a handy way of turning a native `datetime` into something more human-friendly. Its syntax is a little kooky, but persevere and you'll be rewarded.

Conveniently, the `%a` formatter, for 'abbreviated day of week', is the same format our street sweeping data is in, _except Tuesday which is 'Tues' in the data and 'Tue' here_. Neat.

You can get more hands-on with `datetime` with [this Codecademy exercise](http://www.codecademy.com/courses/python-beginner-en-zFPOx/0/1).

### Sweeping Today

Before we move on to tomorrow, let's get our sweep on. Write a function that tells you if the block is swept today.

<pre class="hint">
from datetime import datetime

now = datetime.now()
now_day = now.strftime("%a")
if now_day == 'Tue':
    now_day = 'Tues'

def swept_today(street_name, house_number):
    ...
    # go through the rows looking for the right block
    ...
    # if the street name and numbers match, does the day?
    if row['WEEKDAY'] == now_day:
        return True
    # don't return False immediately, there may be multiple
    # rows for that block
    ...
    
    # finally at the end, return False if we never found it
    return False
    
    
# test using the blocks you identified earlier
# if today is Thursday
result = swept_today("Vesta St", 33)
print "If today is Thursday, this should be True: {}".format(result)

result = swept_today("Coral Rd", 87)
print "If today is Thursday, this should be False: {}".format(result)
</pre>

Check your work against [this](https://gist.github.com/jennielees/e71d772eb88be631b865) version.

## Tomorrow

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

Remember, the *return* keyword means that you can assign the function to a variable, and you'll get something back if all goes well:

```
day_to_check = tomorrow_day()
print day_to_check
```

### Sweeping Tomorrow

Build on what you just did with `sweep_today`. Given a street name, and house number, tell me whether it's going to be swept tomorrow. You can change your `sweep_today` function or rename it to something more general, like `sweep_day`.

**When done**: Add your code to GitHub. Ask the instructor/TA if you're not sure what this means.

**Next**: Head to Extra Credit and work on more extensions to street sweeping, or find a CSV file of your own and play around with that.


## A CSV of your own

Pick a CSV of your own to work with. Explore it the same way you did the street sweeping data, and work with the instructor/TA to identify a small script you could write to use the data.

One example is exporting and cleaning up your address book.
