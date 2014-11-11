---
layout: post
title: Data, meet App
week: 8
---

## Peewee Streeswee

Let's use peewee to interact with the street sweeping data we encountered before!

Clone the repository at [https://github.com/jennielees/sweep_db](https://github.com/jennielees/sweep_db).

The `peewee.db` file has already been created for you, but if you want to see how it was done, you can peek inside `create.py`.

Inside `sweep.py` you will see two models defined for you.

The `Street` model has one attribute: its name. The `SweepTime` model has many attributes corresponding to the section of street and time it's swept -- you may well be familiar with these from earlier exercises.

In the past we looped through the whole CSV file whenever we wanted to look up a street. Now we can use Peewee and the database to do these lookups much more efficiently.

In `sweep.py`, try looking up the time for a specific street:

```
my_street = Street.get(Street.name == 'Sutter St')
for t in my_street.times:
    print t
```

Ugh! Lots of `<__main__.SweepTime object at 0x10fffff>` nonsense.

Let's add a method on to `SweepTime` that tells Python how to print it out. **Inside** the indentation, add a `__repr__` method:

```
class SweepTime(Model):
    day = CharField()
    ...
    ...
    is_odd = BooleanField()
    
    def __repr__(self):
        return "{}-{}: {} from {} to {}".format(self.start, self.end, self.day, self.from_hour, self.to_hour)
```

The `__repr__` method has to return a string representing the 'friendly' printable version of the `SweepTime` object. The double underlines mean it's an 'internal' Python method, and in this case, it gets automatically used when you try to `print`.

Add a similar `__repr__` inside `Street` that returns its name.

Re-run the times printing, and you should see something a lot nicer.

What happens if the street isn't found? Can you make it behave nicely?

#### Where? Where.

That little `for` loop probably had a lot of entries. To find the right block, we can ask the database directly with a "where".

For example, to find all the streets swept on a Tuesday:

```
for t in SweepTime.select().where(SweepTime.day == 'Tues'):
    print t
```

Let's apply this to our `my_street` query.

Since the street doesn't change, we want to leave that part unchanged -- and restrict the **times** we get back, applying the `where` to the `times`:

```
my_street = Street.get(Street.name == 'Sutter St')
for t in my_street.times.where(SweepTime.start < 683, SweepTime.end > 683):
    print t
```

This works because `my_street.times` is equivalent to `SweepTime.select().where(street==my_street)`, and we can have as many `where` clauses as we want!

Your file should look something like [this](https://gist.github.com/jennielees/f7b3b554e0e98b3f299a) now.

### A streetwise app

Using the code you wrote for the earlier street sweeping exercise -- or not, if you choose! -- can you expand this base into a database-backed app? Check [this gist](https://gist.github.com/jennielees/9b593cd8d20ecb91b440) out if you lost your code.

Your app should:

* Ask the user for a street name
* Ask the user for a house number
* Look up the times for that block
* Print out a message to the user with the times (making it clear which side is swept when)

You should also:

* Fail gracefully if the street isn't in the database
* Fail gracefully if the block isn't in the database
* Make sure you have a function that returns the times

Optional extensions:

* Instead of printing out the times, tell the user if any side of their street is swept tomorrow 
* Look at the blocks either side of the user's block too

Think about:

* Could you text the user with this information?
* Could you take a tweet input and tweet the answer back? 
* What might you have to change to make either of these work?



