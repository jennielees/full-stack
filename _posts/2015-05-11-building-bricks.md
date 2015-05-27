---
layout: post
title: Building Bricks Behind Apps
week: 4
---

## Code Review

The first thing we're going to do tonight is pair up and review each other's code from last week. It doesn't matter if you finished the app - as an open-ended exercise, you should be able to learn something however far you got.

Sit next to someone new and share your code. If you can get it working on the pairing machines, more the better, but you can use your laptops if that's easier.

Code review guidelines:

* Start by running your app and demonstrating what it does to your partner.
* Let your partner give feedback, and take notes (adding comments in-line is a good way to note without breaking the app). The goal is not to live-edit the code, but to learn from it so you can write better code in future.

As the reviewing partner:

* Read through the code and trace what happens when each piece runs.
* Ask questions!
* Suggest improvements (constructively)
* Try to think what might go wrong. Is there input that could break this code? 

## Model, View, Controller

When building the ingredients app, you may have found that you had to repeat some things, or that parts of your code did related jobs but things got a bit messy along the way.

That's ok, but as you might've noticed, can be difficult to come back to after a few days away - and just as difficult to build upon, as you make your app more complex!

We're going to use a **model-view-controller** approach, which is a pattern that has been around since the 1970s!

In this world (aka [MVC](http://code.tutsplus.com/tutorials/mvc-for-noobs--net-10488)), we have three main things.

**Models** represent the underlying data, and deal with figuring out how the database-level details make it into code.

**Views** represent what the user sees. They are often powered by templates.

**Controllers** handle the stuff in between; how the data gets into the view.

We are going to build an app using this kind of approach. This is going to be the first part of our Pinterest app -- handling users.

### Models

We'll start with models.

We want to handle users, so we'll set up a few attributes for our users.

A user has the following:

* ID
* username
* email address
* password
* real name
* avatar image URL

Create a SQL `'CREATE TABLE'` statement for the `users` table, and then create the database, as you did with the ingredients last time. ([Refresher](http://www.tutorialspoint.com/sqlite/sqlite_create_table.htm)) ([Solution](https://gist.github.com/jennielees/40de2da674c4bc9cfbe8))

OK, you should now have an empty `users` table in a database. I'll assume the database is called `users.db` from here.

Now we want to create a new Python file with some functions relating to users. Call this file `models.py`. This is the outline of the file: you need to fill in the insides! ([Download file](https://gist.githubusercontent.com/jennielees/ba4201ee51bf14a01318/raw/b5237d701c9ed5ecd00038690ea54aa4a923954e/models.py))

```
import sqlite3

DBFILE = 'users.db'  # This defines which file on disc to look in

def connect_to_db():
    """ Get a connection and a cursor. """
    conn = sqlite3.connect(DBFILE)
    db = conn.cursor()
    return (conn, db)


def list_users():
    (conn, db) = connect_to_db()
    ### Get all the users from the database
    conn.close()
    ### Return the list of users


def get_user(id):
    (conn, db) = connect_to_db()
    ### Get the user matching the supplied ID
    conn.close()
    ### Return the user


def get_user_by_username(username):
    (conn, db) = connect_to_db()
    ### Get the user matching the supplied username
    conn.close()
    ### Return the user


def create_user(username, email, password, realname, avatar):
    (conn, db) = connect_to_db()
    ### Use the function arguments - username, etc - to INSERT a new user
    conn.close()
    return 'success'


def update_user(id, attribute, new_value):
    (conn, db) = connect_to_db()
    ### Update user by setting attribute to new_value
    conn.close()
    return 'success'
```

We're going to make sure this code can pass a few **tests** before we release it into the wild.

[Here](https://gist.github.com/jennielees/f6bb1fcbf002b0559fb9) is the test file - save this code as `test_models.py` ([raw](https://gist.githubusercontent.com/jennielees/f6bb1fcbf002b0559fb9/raw/e68e22be3acec31057a335074ddd54ebe93490bc/test_models.py)).

Run `test_models.py`. Pretty dismal, huh? Why do some of them pass already? Should they?

See if you can make all the tests pass (by editing the code they are testing, inside `models.py`). Feel free to improve them if you need to. Are some of the tests linked? Is it easier or harder to make them pass if they are intertwined?

Can you add a test called `test_get_nonexistent_user` that calls the function `get_user_by_username` with a username that doesn't exist? What do you think should happen in this case?

### Not working?

With inserts and updates, don't forget to call `conn.commit()` to make sure any changes you made actually hit the database.

Also remember to call `conn.close()` to clean up the connection after yourself, so you don't end up accidentally locking the database.

## From Models to Views

Now create the views. Make these **totally independent** of the models file you just created and got working.

You are going to want the following HTML pages:

* Log in page (submit a form containing username and password)
* Sign up page (enter email, username, password, etc, to create account)
* Admin page (list all users)
* Some kind of index page to prompt the user to sign up or log in
* Some kind of "Congrats, you are logged in" page

Hook these up to basic Flask routes in a new app -- without any database work. Make sure they all fit together and that a user can submit the sign up or log in forms successfully. [Skeleton Reference](https://gist.github.com/jennielees/26e1f5703b2ba29471bd)

## And now... the controllers...

There isn't a great deal of controller logic needed for these routes, but there is some. You might have spotted it as you were hooking things up in the last section.

Expand the login, signup and list pages to use the database model methods we created before. Nice and clean!

[Here](https://gist.github.com/jennielees/1a5b65edf983fa299393) is a template with some guiding comments.

### Fun stuff

There are some notes in the template above relating to the signup form. How can you check the signup information is valid? What should you do if the username is already taken?

**Logging in a user** is a great use of the [Flask session](http://flask.pocoo.org/docs/0.10/quickstart/#sessions). The session keeps some state on the server, and uses [cookies](http://en.wikipedia.org/wiki/HTTP_cookie) - tiny text files stored in your web browser and sent back to the server - to match that state to the user making the request.

To "log in" a user, first make sure you have imported the session - you'll also need to set up an app secret key.

```
from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = 'thisisasecret'
```

Now, inside your login method:

```
session["username"] = username  # for example, this sets a username for the user
```

You can then check if the user is logged in from **any** function:

```
if session.get('username'):
   # this will be executed if 'username' is present in the session
```

And you can delete the `username` key to log the user out

```
del session['username']
```

Using sessions, log the user in properly. Add a `/logout` method.

### Extra Credit

Have time left or want to dig deeper? Great!

Create a user settings page where the user can change their password.

Can you make this "safe"? (i.e. the user has to enter their old password and retype the new one twice)

Can you think of a better way to store passwords than in plain-text? [This tutorial](http://www.pythoncentral.io/hashing-strings-with-python/) might be interesting.

Create a `delete_account` method inside `models.py` and then hook that up to the admin page (and the user settings page, if you created it). Does this seem a little dangerous to you? Can you think of a better way to allow the user to 'delete' their account without potentially totally destroying it?

Can you figure out how to do a "forgot password" flow? Create the web pages and HTML routes first, then create a function that would generate a new password, and a second function to email the user the new password. Actually sending the email is something we will cover in a couple of weeks, but if you are really keen, [see this guide](https://bradgignac.com/2014/05/12/sending-email-with-python-and-the-mailgun-api.html).