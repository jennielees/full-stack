---
layout: post
title: Mashup Briefing
week: 9
---

For the final two weeks of class, we will be using the time to work on individual projects.

Create a Python app which does one or more of the following:

* Takes user input
* Reads a file
* Connects to an API
* Saves and/or loads data from a database

We've already built several apps doing these things, so use that code as a starting point.

If you are short on inspiration, here are a few ideas:

* Export your Google address book to a CSV file and write a Python app to clean it up
  * Extension: you could look at other APIs to improve your address book
* An app that you type a daily message into, e.g. an affirmation, diary entry, food diary, "what I did today", saving these in a database.
* Inspire me: the opposite of the above, inspirational quotes on demand
  * Extension: text the quotes to the user
* "UmbrellaMe": constantly running app which checks if it will rain today, displaying an appropriate message (ASCII art could be great here).
  * Run this on a Raspberry Pi near your front door! (I would totally use this.)
* Random movie picker - use a movie data set to get ideas for what to watch! (User types in a category or an actor, perhaps..?)
* Spending Tracker: Use your bank transactions (which you can usually download via CSV) to answer some questions about your personal finances.
* House Hunter: Use craigslist data and something like [import.io](https://magic.import.io/?site=http:%2F%2Fsfbay.craigslist.org%2Fsearch%2Fapa) to automate your apartment search! 
* Look through the [Data Sources list](/data-sources) and see if anything sounds interesting!

## Scoping the Project

Talk to us to make sure you have picked something doable in the time you have.

In [Project Resources](/project-resources) you'll find two sample projects to measure against, or to work through if you don't have a great idea handy.

### Breaking it Down

Your first step should be to break down the project into smaller pieces.

What does the user do? How do they interact with the app? Do they need to type anything in, or perhaps use Twitter?

What does Python need to do? Do you have an idea of how you might do this? Have you done something similar in class?

Do you plan to use any APIs? Have you checked them out to see how easy or difficult they look? How are they authenticated?

Are you saving or loading data? To a file or to a database? Have you thought about what format the data will be in?

We are here to help you answer these questions!

### Getting Started

If you are not sure where to begin, try writing out the functions you will need and then filling in the details. Our example projects will do this. Alternatively, if it is close to something you did earlier, take that code and start changing it.

### Git 'er Done

Add and commit your code to Git every day you work on the project, ideally multiple times a night as you finish standalone chunks. 

If you make a mistake, or want to go back to an earlier version of your code, having this history will save you a lot of frustration. 

### Test Thoughts

Don't forget to think about testing. How will you make sure your code works? What inputs do you need to put in to test the range of things you are doing?

### Breaking Bad

Try to break your code as you go. If you assume input is a number, for example, try putting in a string when you are testing it. Try putting in nothing, or values you know aren't in your data. Better that you break it and fix it, than a user breaks it!

## Good Luck!