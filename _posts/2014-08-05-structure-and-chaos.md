---
layout: post
title: Structure and Chaos
---


#### Dictionary Corner

**Discussion:** What's a dictionary? When is it used? What parallels does it have to other things (e.g. Javascript/JSON)?

Keys and values crop up all over the world of programming, so you've probably seen something similar before, even if you didn't realise it.

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

#### DictReader, csv.reader's mortal enemy

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

#### It's date time!

Write a function that takes a street name and tells you if it is going to be swept tomorrow. 

*Note: when you make a million on the App Store from this, just remember who suggested it...*

##### Today

Time to meet the delight that is `datetime` in Python.

`datetime` is both a module and a class within a module, which is a fancy way of saying you need to incant `from datetime import datetime` to use it. 

It's a very powerful module that gives you a lot of access to date and time functionality, but for now we care about a few small things.

**Discussion:** Modules and imports

Here is a `datetime` crash course:

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

##### Tomorrow

The `datetime` module has a class called `timedelta` which is, as it sounds, the delta between times.

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

**Discussion**: Problem solving and pseudocode.

#### A CSV of your own

Pick a CSV of your own to work with. Explore it the same way you did the street sweeping data, and work with the instructor/TA to identify a small script you could write to use the data.

One example is exporting and cleaning up your address book.