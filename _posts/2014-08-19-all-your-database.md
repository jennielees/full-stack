---
layout: post
title: All Your Database (Are Belong To Us)
week: 7
permalink: all-your-database/
---

## Databasics

So far, we've done a lot of different things with data in Python. We've loaded in files, looped through to find interesting information, interacted with an end user and even connected to remote APIs.

However, we've not really been saving or updating information -- just importing it and printing it out, for the most part.

This is where a **database** comes in. Using a database is a really important part of back-end web development. It allows apps to save state, as well as show the data to the user in interesting ways. 

A standard type of database-driven app would be any e-commerce site. In order to show the shopper a list of items, the app needs to go look in the database and fetch them. When the user makes a purchase, it stores that in the database too, so that the shipping department can see what they have yet to ship -- and when the order is shipped, the purchase record is updated.

We will talk about databases in class, but if you miss it or want to read more, here are a few helpful links:

* [A Brief History of Databases](http://vvvnt.com/media/history-of-databases)
* [Good Database Design in Web Development](http://www.onextrapixel.com/2011/03/17/the-basics-of-good-database-design-in-web-development/)
* [Learn SQL the Hard Way: Introduction](http://sql.learncodethehardway.org/book/introduction.html)

## Enter SQL

SQL, short for Structured Query Language (but nobody really uses the full form), is the language used to communicate with many databases. It's often pronounced "sequel" but you won't look silly if you prefer "ess queue ell" -- it's like "gif" vs "jif", people use both.

SQL is totally unrelated to Python -- both are languages for interacting with computer systems, but Python is used to write code that the computer directly executes, whereas SQL gives the database specific instructions.

There are a class of databases known as "NoSQL", which (as you might have guessed) don't use SQL. However, many of the basic principles still apply, and SQL databases are still incredibly popular in back-end development, so we'll be learning about SQL in this class.

Let's get our hands dirty with databases!

### The Four Horsemen

First, let's look at the main **operations** you might want to do with a database.

You start out with an empty database, so you want to **create** a database table and create (**insert**) data inside those tables.

Then, you probably want to be able to get that data back out. That's called a **select** in SQL.

What if you want to change an existing piece of data? **Update**.

Finally, let's clear out something entirely with a **delete**.

You'll sometimes see these four operations referred to as "CRUD". Not because they are cruddy (I hope not!) but because they can be collectively called **Create, Read, Update, Delete**.

### Accessing a Database

You'll need a database to practice these commands on. Luckily there is a nice easy database program called **SQLite**. As the "lite" implies, it is a lightweight database that doesn't really require any installation or configuration. 

There are many other database systems out there, with different levels of complexity and power -- we'll be learning about the wider ecosystem a little later.

Let's get SQLite up and running:

#### Mac

Nothing to do here. SQLite should be preinstalled on your computer. To check, go to a terminal:

```
$ sqlite3
```

If it isn't installed, you can go to the [downloads page](http://www.sqlite.org/download.html) and get it.

#### Windows

Download the command-line SQLite program ([zip](http://www.sqlite.org/2014/sqlite-shell-win32-x86-3080701.zip)) and move the `sqlite3.exe` file to `C:\Python27\Scripts` (or equivalent depending where your Python is installed).

This should make it available in Git Bash if you set up your environment previously. If you have issues, ask the instructor/TA.

### Learning to speak SQL

In your terminal type `sqlite3` to open SQLite. If you type it with a file name, SQLite opens that exact file:

```
$ sqlite3 mydatabase.db
```

Filenames don't have to end with `.db` but it's a convention that they do (so you know it's a database file).

#### Bootstrapping

We'll start by using a file to get our database going. You could type everything from the file in, but it's quicker to load it up directly from the file.

Download [bar_ingredients.sql](/public/data/bar_ingredients.sql) -- remember `-O` is capital O, not zero :)

```
$ curl -O http://labs.bewd.co/public/data/bar_ingredients.sql
```

Now load it up into `bar.db`:

```
$ sqlite3 bar.db < bar_ingredients.sql
```

Open up bar.db and take a look:

```
$ sqlite3 bar.db
SQLite version 3.7.11 2012-03-20 11:35:50
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
ingredients
```

The `.tables` command shows the database tables. Each table is like a tab in a spreadsheet and usually maps to a "type" of data (e.g. people, drinks, orders, etc).

Now let's take a closer look at the `ingredients` table:

```
sqlite> .schema ingredients
```

This prints out the SQL statement used to create that table. You can see that we defined an `id` which is an `int` (integer), `name` which is text, and `price` and `stock` which are also both `int`.

```
sqlite> .schema ingredients
CREATE TABLE ingredients (
    id int primary_key not null,
    name text not null,
    price int,
    stock int
);
```

The `primary_key` means that this column (`id`) uniquely identifies each separate row in the database, like the row number in a spreadsheet. `not null` is what it sounds like - this value can't be empty.

Now let's use the `select` command to show us the contents.

```
sqlite> select * from ingredients;
```

This prints out each row with a pipe (`|`) joining each different "cell" of data in a row. You can type `.mode columns` to make this a bit more readable.

```
sqlite> select * from ingredients;
1|glug of rum|4|3
2|slug of whisky|3|4
3|splash of gin|3|7
4|olive on a stick|2|5
5|salt-dusted rim|1|20
6|rasher of bacon|3|8
```

The `*` command just means "everything", a convention you may have seen before in Terminal.

If we want to select specific fields, we can.

```
sqlite> select name, price from ingredients;
```

And if we want to restrict by specific criteria we can use a `where` to do that, too.

```
sqlite> select name, price from ingredients where price=3;
```

Let's update the stock level on our bacon item. This has an ID of 6, so we can use that unique identifier to make the update easy (and make sure it only affects the bacon!).

```
sqlite> update ingredients set stock=0 where id=6;
```

Finally, let's add some new items. The insert syntax needs to know which fields you are updating, too:

```
sqlite> insert into ingredients (id, name, price, stock) values (7, 'shake of bitters', 2, 12);
```

What happens if you leave fields out, or try to insert something that is null where the schema says "not null"?

### Getting Interactive

Go to the [SQL Intro](https://github.com/hackbrightacademy/sql_intro) Git repository and copy the URL on the right hand side of the page to clone it locally:

```
$ git clone https://YOU_FIND_THIS_URL.git
```

Go into the directory you just cloned and run the `sql_exercise.py`. This is an interactive tutorial which requires you to read carefully -- there are links throughout to SQLZoo pages which explain more about the different statements.

```
$ cd sql_intro
$ python sql_exercise.py
```

When you've finished, flag someone to check over your answers.

Then head to the [SQL Lesson](https://github.com/hackbrightacademy/sql_lesson) repository, read the instructions there, and work through that exercise too. 