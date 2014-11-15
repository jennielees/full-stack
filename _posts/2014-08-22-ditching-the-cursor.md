---
layout: post
title: Ditching the Cursor
week: 8
---

This week we're going to focus on how to effectively communicate with a database in Python.

First, we'll use SQL directly within Python. Get started by cloning [this repository](https://github.com/jennielees/pirates):

```
$ git clone https://github.com/jennielees/pirates.git
$ cd pirates
```

We will start by looking at the **pirates** files. If you already completed the Hackbright students ["Part 2"](https://github.com/hackbrightacademy/sql_lesson/blob/master/PART2-HB_APP.md) exercise, you can skim read until 'In Practice'.

### Getting Connected

When dealing with a database in Python, we always have to do two things. We have to open a connection to the database and create a cursor, which is a way of interacting with the database through the connection.

This maps directly on to what you do in Terminal:

```
$ sqlite3 mydatabase.db     # open a connection
sqlite> SELECT * FROM data; # this is the cursor
```

To do this in Python, we first import the sqlite3 library, so we can use the relevant functions, and then connect. Try this in a new file or in the interpreter:

```
import sqlite3

conn = sqlite3.connect('pirates.db')
db = conn.cursor()

conn.close() # Always do this after you are done with everything else.
```

To run any SQL command, we use `db.execute()` on it.

```
db.execute("SELECT * FROM pirates;")
```
You may be surprised to hear that this function doesn't have a result we can use. After calling `execute`, we have to go ask the cursor to get us the rows which matched:

```
results = db.fetchall()
```
Now `results` has a list of all the rows which matched the last thing `execute`d. We can `print` them to see what they look like:

```
print results

[(1, u'Blackbeard', 3), (2, u'Roger Rumguzzler', 2), (3, u"Cap'n Cathy", 1), (4, u'Tara the Terrible', 2), (1, u'Blackbeard', 3)]
```

This is a list, and each row is a tuple (remember, a tuple is just a list whose values you can't change, and has round instead of square brackets to denote this). You can clean the display up with a `for` loop:

```
for row in results:
    print row[0], row[1]
```

And that's the essentials of using SQL in Python!

### Writing is fun

Writing to a database using Python is just like the previous example, only you have to use an `INSERT` or `UPDATE` statement. From last week's labs, you should know what these are -- here's a refresher.

To create a new row of data, we use `INSERT`:

```
INSERT INTO pirates VALUES (1, 'Blackbeard', 3);
```

To alter an existing row, we use `UPDATE` with `WHERE`:

```
UPDATE pirates SET name='Bluebeard' WHERE id=1;
```
Always use a unique column like `id` here, or you may update multiple rows by mistake.

Doing this in Python, we break the statement into two halves, putting `?` where we will later insert real values during the `execute`. This is similar to how we do string formatting:

```
query = """INSERT INTO pirates VALUES (?, ?, ?)"""
db.execute(query, (1, 'Blackbeard', 3))
```

Note: triple quotes (`"""`) are the same as `"`, except triple-quoted strings can span multiple lines.

## In practice

Open up the `pirates.py` file you cloned earlier.

Run it to see what it does.

Here is the stub for a new function:

```
def new_pirate(db, name):
    query = """INSERT INTO pirates VALUES (?, ?, ?)"""
    
```

Call this function in `main()` with `raw_input` to get the user's name.

<pre class="hint">
def main():
    (conn, db) = connect_to_db()
    new_name = raw_input("And what be yer name, me heartie? ")
    new_pirate(db, new_name)
    list_pirates(db)
    conn.close()
</pre>

Try finishing up this function. What issues do you spot?

### What about the ids?

To make this function complete, we need to figure out which values we'll put in for `id` and `ship_id`.

Firstly, for `id`, we can do one of three things:

* Guess a value that no other pirate has
* Get all the pirates and choose the next value for `id`
* Use the database to control an auto-increasing `id` and don't try to set it manually

In the [SQL Lesson](https://github.com/hackbrightacademy/sql_lesson), you encountered auto incrementing fields. This is the safest way to do this. We should always make the database do the work if we can, and our code doesn't care about what `id` is, only that it is a key.

To make it work we'll need to actually change things at the database level, which involves a few steps.

Move your database file somewhere else (always best to move rather than flat-out delete):

```
$ mv pirates.db old_pirates.db
```
Edit the SQL file (`pirates.sql`) you used to create the database. When you create the pirates and ships tables, change the lines

```
id integer primary key not null
```
to

```
id integer primary key autoincrement
```

SQL isn't case sensitive but you can use caps if you prefer. Your insert statements should still work.

Re-create the database:

```
$ sqlite3 pirates.db < pirates.sql
```

Now, with an auto-incrementing `id`, you can insert new values as much as you like, confident that the `id` field will behave.

### Finishing the insert function

Let's try again with a different insert:

```
def new_pirate(db, name):
    query = """INSERT INTO pirates (name) VALUES (?)"""
    db.execute(query, (name,))
```

This slightly odd syntax does two things. First, it is only inserting into the `name` column. Since `ship_id` is optional, we're not assigning this pirate to a ship immediately. Second, the `execute` statement needs a tuple as the second argument, so we are forcing `name` to be the first element in a list with the syntax `(name,)`. If you get weird errors, check this syntax first.

Something weird happens if you run `pirates.py` multiple times. Can you spot it?

### Commitment

If you run the "add pirate, list pirates" multiple times, you'll notice that your newly added pirate doesn't actually get saved. She appears in the list, but not in the database itself.

Most database systems use a kind of staging area where changes are put before they get saved to disk. To make sure the changes actually get saved, we need to `commit` the action.

```
conn.commit()
```

### Assigning a ship

Now we have these basics, let's try a little more complexity. Assign a ship to this pirate by choosing randomly and then using `update`.

First, let's get the ID of the pirate we just created. In `new_pirate`, add a `return` to get the last row ID:

```
return db.lastrowid
```

Let's make a function to choose a random ship ID:

```
def get_ships(db):
    query = """SELECT * FROM ships;"""
    db.execute(query)
    results = db.fetchall()
    return results
```

```
import random # don't forget this at the top!

def random_ship_id(ships):
    ship = random.choice(ships)
    return ship[0]
```

Can you put together the random ship ID and the ID of the new pirate with this `UPDATE` statement?

```
query = """UPDATE pirates SET ship_id=? WHERE id=?"""
db.execute(query, (ship_id, pirate_id))
```

How do you know if it worked? Head to `sqlite3` and run a `SELECT`. 

For bonus points, update your `list_pirates` function with a `JOIN` to list the pirates *and* their ships' names. Remember, if using a `JOIN` and multiple columns have the same name, use the table name too:

```
SELECT pirates.name, ships.name FROM…
```

## An easier way

As you can already see, writing out SQL statements by hand can get pretty complex and tedious. Fortunately, as with many things that developers do a lot, there are lots of Python libraries around to make life easier.

One such library is [Peewee](http://docs.peewee-orm.com/en/latest/), a Python ORM.

ORM stands for "Object Relational Model" which is a way of saying "working with relational databases natively in Python". There are several others around, for Python and other languages. We use Peewee since it is very light and easy to use, but if you have a workplace that uses something different, let us know and we can help you understand those too.

### Hello, Peewee

First off, let's get peewee on our systems.

```
$ pip install peewee
```

Create a new file called something like `pirates2.py` (don't call it `peewee` or your `import` won't work):

```
from peewee import *
db = SqliteDatabase('peewee.db')
```

First up we will create representations of the objects already in our database. The `id` field goes away, as peewee handles all that for us.

We use `ForeignKeyField` to denote a relationship.

```
class Ship(Model):
    name = TextField()

class Pirate(Model):
    name = TextField()
    ship = ForeignKeyField(Ship, related_name="crew", null=True)    
    
class Cargo(Model):
    amount = IntegerField()
    name = TextField()
    ship = ForeignKeyField(Ship, related_name="cargo")
```

Because we are using peewee to define our tables, we should use a new database here, rather than try and work with our existing tables. 

So we need to make sure we create these tables:

```
db.create_tables([Ship, Pirate, Cargo])
```
This is a one-time creation step and can be commented out when it has been run.

Now let's actually look at how we use those definitions. Since we started with a blank database, let's create some new pirates:

```
blackbeard = Pirate(name="Blackbeard")
blackbeard.save()
```
Since our definition in `Pirate` says that `ship` can be `null`, we are ok to save a pirate with just a name. Let's print out the pirates using `select()`, which mirrors the SQL `SELECT`:

```
pirates = Pirate.select()
for pirate in pirates:
    print pirate.name
```

Write a function to accept user input and create a new pirate with that name, just as you did before. Check [this version](https://gist.github.com/jennielees/e292cccaaf615e9ef1ac) against yours when you are done.

### On Ships We Sail

Save some ships into the database. When you are using something like peewee, it's wise to try and work through Python rather than using `INSERT` directly in SQL, so that everything remains consistent. So let's open up a Python shell and do it in there:

```
$ python
>>> from pirates2 import Ship
>>> shipone = Ship(name="Fair Louisa")
>>> shipone.save()
1 
```
You'll see peewee print out a `1` for "success". Repeat the last two lines a couple more times to get a range of ships saved to the database.

Now, let's revisit our random ship assignment from before.

First we want to get all the ships, then we want to choose one at random. This time round we want to get the actual ship, not the ID (remember, peewee will take care of the ID part).

```
def random_ship():
    ships = Ship.select()
    rand = random.choice(ships)
    return rand
```

Oh no! This doesn't work.

Why?

Well, `Ship.select()` is deceptive. It isn't a list (instead, it's a query that returns one item from the database at a time). It supports the `for` loop, but functions like `random.choice` - which require a list - fail because it doesn't support other list operations, in this specific case `len()`.

If we want to do random selection here, because we only have a few ships, we can copy them into a list:

```
def random_ship():
    ships = []
    for ship in Ship.select():
        ships.append(ship)
    rand = random.choice(ships)
    return rand
```

If you try to `print` this directly, you will get a weird looking `<__main__.Ship object at 0x…>` thing, which is actually the full `Ship` object. Python doesn't natively know how to print ships, so to print a ship called `ship`, you need to `print ship.name`.

```
def main():
    ship = random_ship()
    print ship.name
```

Check your code against [this gist](https://gist.github.com/jennielees/f8820aeb529e6a8c1254) to make sure you're on track.

### Crew Assignment

Now that we can randomly pick ships, let's assign them to the crew.

First, let's find all the pirates who don't yet have ships. The `where()` operator restricts the query, just like in SQL:

```
lazy = Pirate.select().where(Pirate.ship==None)
for pirate in lazy:
    print pirate.name
```

To assign a ship, this is where peewee shines over using the SQL directly:

```
lazy = Pirate.select().where(Pirate.ship==None)
for pirate in lazy:
    new_ship = random_ship()
    pirate.ship = new_ship
    pirate.save() # don't forget to save! :)
    print "Assigned {} to the good ship {}".format(pirate.name, pirate.ship.name)
```

Look how we can `print pirate.ship.name` to directly access the ship a pirate is assigned to. We don't need to do a join, since peewee handles all of that for us. Beautiful.

### From the Ship

Let's play around a little more with Things That Would Otherwise Be Joins: going from ships to pirates or cargo.

The `get()` on the end of a query will give you the first result straight up. Useful when you are trying to just get one thing.

```
louisa = Ship.get(Ship.name=='Fair Louisa')
```

Let's print out her crew:

```
for pirate in louisa.crew:
    print pirate.name
```

And create some cargo using `louisa` to refer back to this ship:

```
cargo = Cargo(amount=10, name="Pieces o' Eight", ship=louisa)
cargo.save()

for item in ship.cargo:
    print "{} {}".format(item.amount, item.name)
```
#### Extra Credit

Write an interactive cargo manager using `raw_input` to get the ship name, cargo name and amount, and save it. 

Note that to save a `Cargo` object you need to make sure the `ship` argument is a `Ship` not a string or integer:

<pre class="hint">
ship_name = raw_input("Ship name, lubber? ")
user_ship = Ship.get(Ship.name==ship_name) # user_ship is now a Ship
cargo = Cargo(amount=10, name="Pieces o' Eight", ship=user_ship)
cargo.save()
</pre>

How would you handle the case where the name doesn't match a ship? What does `Ship.get` give you in this case, and can you deal with it gracefully?

<pre class="hint">
try:
    my_ship = Ship.get(Ship.name=="bob")
    # if peewee can't find that ship, it will throw an Exception
    # of type ShipDoesNotExist (try it without the try/except!)
except:
    # must have gotten a ShipDoesNotExist error!
    print "Sorry, that ship doesn't exist."
</pre>

Could you extend this to also check if the amount is a valid integer?

What if the cargo is already assigned to that ship? Should you write a new row, or find the existing one and update it? To update in peewee, you just change an object and call `save()` again, like we did with the pirates being assigned to ships.

<pre class="hint">
cargo_name = "Pieces o' Eight"
cargo_amount = 10
cargo_ship = Ship.get(Ship.name=="Fair Louisa")
try:
    # Does this ship have any cargo by this name?
    
    existing_cargo = Cargo.get(Cargo.name==cargo_name, Cargo.ship==cargo_ship)
    
    # If this failed, throwing an Exception, the next 
    # two lines don't run.
    
    # If it succeeded, add more to that cargo.
    existing_cargo.amount += cargo_amount
    existing_cargo.save()
    
except:

    # It must not already exist, so create it
    
    cargo = Cargo(amount=cargo_amount, name=cargo_name, ship=cargo_ship)
    cargo.save()
</pre>