---
layout: post
title: Week 8 Extra Credit
week: 8
permalink: week-8-extra/
---

* [Hackbright SQL Lesson](https://github.com/hackbrightacademy/sql_lesson/blob/master/PART2-HB_APP.md)
* [SQLite Autoincrement](https://www.sqlite.org/autoinc.html)
* [Peewee Docs](http://docs.peewee-orm.com/en/latest/)


## Using a specific SQLite database in peewee

In peewee, using a database file that you specify is a little more work than it looks.

We start by specifying a database name:

```
db = SqliteDatabase('pirates2.db')
```

However, even if we do this, peewee will still use `peewee.db` by default!

We also need to change **every** definition with a `Meta` entry assigning it to that database:

```
class Ship(Model):
    name = TextField()
    
    class Meta:
        database = db
```

The easiest way to make sure our `Model` classes all use this is to change things around a bit.

Create a new **base** class:

```
class BaseModel(Model):
    class Meta:
        database = db
```

This doesn't do anything other than specify the database. Now,  when we create a new class (like `Ship`), we use `BaseModel` instead of `Model`:

```
class Ship(BaseModel):
    name = TextField()
```

Because it **inherits** the database setting from `BaseModel`, we don't need to specify it separately inside Ship.
#### Exercise
Rewrite the first peewee exercise code to use this pattern and make sure it is writing to a file that isn't `peewee.db`.
