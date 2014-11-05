---
layout: post
title: Week 7 Extra Credit
week: 7
permalink: week-7-extra/
---

* [Hackbright SQL Intro](https://github.com/hackbrightacademy/sql_intro)
* [Hackbright SQL Lesson](https://github.com/hackbrightacademy/sql_lesson)

###[Learn SQL the Hard Way](http://sql.learncodethehardway.org/book/):

Work through [Lessons 1-4](http://sql.learncodethehardway.org/book/ex1.html).

Create a new, blank database, and then write SQL code that accomplishes the following:

* Create a species table. This table should have a single column for "name", which should be a string value.
* Create a breed table. This table should have a column for "name" (text) and species (foreign key to species table).
* Create a pet table. This table should include the following columns: name (text), dead (integer), breed (foreign key to breed table), adopted (integer). Note that both the dead and adopted fields are intended to use 0 and 1 to refer to boolean values.
* Create a person table with first name, last name, age, email address, and phone number.
* Insert some values for species, breed, pets and people.
* Insert some values into the person_pet table to capture relationships.

Although you can enter the commands for each of these steps into the interactive console for the database, you ultimately should end up with a single SQL file that you can run from the command line that accomplishes each of these steps.

Work through [Lessons 5-11](http://sql.learncodethehardway.org/book/ex5.html)

Working with the same database you ended with in the previous assignment, write SQL statements to achieve each of the following:

* Select all the cats
* Update all cats to set adopted to False
* Select all the pets belonging to a specific person
* Update all the cats belonging to a specific person to set adopted to True.

Work through [Lessons 12-15](http://sql.learncodethehardway.org/book/ex12.html).

Read about [foreign key constraints](https://www.sqlite.org/foreignkeys.html#fk_basics) to preserve integrity.