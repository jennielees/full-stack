---
layout: post
title: Persistence Pays Off
week: 7
---

## Databases in Practice

We're going to work through this [SQL Lesson](https://github.com/hackbrightacademy/sql_lesson) to get an idea of how we might use a database in practice to power an app. The lesson uses a student database and goes over many of the SQL statements you already encountered.

Head to [the lesson](https://github.com/hackbrightacademy/sql_lesson) and work through the steps outlined in the README file (which is shown when you visit the GitHub page -- it starts with "SQL and Relational Databases"). 

You will be thinking about data *modeling* - that is, how to represent some real world data (like students and projects) in a database.

Throughout the lesson, you will be entering SQL statements in. Remember that you have to be inside `sqlite3` for them to work, so start the lesson off by creating (and working on) a database file from Terminal:

```
$ sqlite3 hackbright.db
```

As you work through the lesson, make a cheat sheet for yourself with the SQL syntax you are using.

You may find this [visual guide to JOINs](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/) helpful.

## Python and Persistence

Now we have a passing familiarity with SQL, we're going to introduce it into an app! Python can speak to databases, and we'll start off by getting Python to talk SQL.

Work through [Part 2](https://github.com/hackbrightacademy/sql_lesson/blob/master/PART2-HB_APP.md) of the SQL Lesson.

If you haven't already, clone the GitHub repository so you can access the Python file it refers to:

```
$ git clone https://github.com/hackbrightacademy/sql_lesson.git
```

Then work through the lesson to learn:

* What is a cursor?
* How do you tell Python to connect to a database?
* How do you execute a SQL query using Python?
* How can you get rows from the database?
* What must you do when you are finished with the database connection?

## Viewing Visually

To look at the contents of a database in a more visual way, you can use a client like [Induction](http://inductionapp.com/). For Linux and Windows, [RazorSQL](http://www.razorsql.com/), [SQLite Browser](https://apps.ubuntu.com/cat/applications/sqlitebrowser/) (Ubuntu), and [DB Browser](http://sqlitebrowser.org/) are all (untested) options.

For Induction, the easiest way to get going is to drag and drop the database file on top of the app icon. 