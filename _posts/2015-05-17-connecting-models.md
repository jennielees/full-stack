---
layout: post
title: Connecting Models
week: 6
---

## Connecting Models

How do we relate models to each other?

Remember the "foreign key" from our SQL exercises? Any SQL table can have a field that relates to the ID of a different table. Then we can just query the other table by ID to connect the dots.

We're going to add a `User` model and link it to desserts. Each dessert was submitted by a User, so we add the user ID field to Dessert, and make sure our `User` has an `id` to link back to. A simplified version of our tables looks like this:

![Relationships](/full-stack/public/relationships.png)

Let's look at the `relationships` branch in the GitHub repo from last class to see what this looks like. Since you should've made a bunch of changes, you have two choices:

1. Look at the code online [on GitHub](https://github.com/jennielees/flask-sqlalchemy-example/tree/relationships) and/or pull a fresh repository

2. Check out the new Git branch and go through your code trying to fix the merge conflicts. 

### Git Pull

If you choose option (2), here's how to do it safely. Since you checked out the Git repository before the `relationships` branch existed, you need to update your local state of things:

```
git fetch --all
```

Now you can get the new code, **but before you do this**, commit your local changes first so you can always go back to the current state of things:

```
git add .
git commit -m "your message"
```

Merge my branch into yours, combining both of our changes:

```
git merge relationships
```

If things don't look good, you will get some fun merge conflicts in your files. You'll see a message like `Automatic merge failed; fix conflicts and then commit the result.`. 

Look through your files for lines beginning with `>>>>` and `<<<<`, and delete the code you don't want to keep. Please ask for help with this if things seem kinda scary! Then `git add` and `git commit` the resulting files. 

If you're not sure what's going to happen, you can cancel the merge and go back to the way things were: `git merge --abort`.

If you've done the merge but things are totally broken, and you want to go back to your changes and throw mine away, find the **commit hash** of the commit you made above.

```
$git log
commit 5ccd62e66548ee9a46fb77fc813915241b4c0e82
Author: Your Name <you@something.com>
Date: Thu Jun 4 ....

your message
```

Then reset everything to that commit:

```
git reset --hard 5ccd62e66548ee9a46fb77fc813915241b4c0e82
```

(Changing the hash to the one you saw in your log, of course).

#### Getting out of weird editor screens

Some of the git commands will throw you into a Vim editor, which is a bit painful to get out of. Hit escape, then type `:q` to quit.

Others, like `git log`, throw you into a scrolling screen. You just need to hit `q` to get out of this one.

If you got through the merge without giving up and looking at the code in the web browser, give yourself a well-deserved pat on the back. This stuff trips up experienced engineers frequently, and really does take some getting used to. Feeling a bit lost? [Try Git](https://try.github.io/levels/1/challenges/1) is a great resource.

## Model Changes

To connect our models together, I've changed `models.py` to have a new model definition for `User`. I've also added a new `user_id` into `Dessert`,  which I specify is a foreign key back to User, and added a special `user` relationships on `Dessert`:

```
user = db.relationship("User")
```

This automatically uses the `user_id` field. SQLAlchemy is smart like that.

I can create the new `User` table easily by running `models.py` directly, which invokes `db.create_all()`.

```
python models.py
```

However, if you go into your database via `sqlite3`, you'll see that the `Dessert` table didn't change. Boo!

The easiest way to fix this is just to delete the table and re-create it, but if you experimented with other ways in the challenges before, feel free to do it differently. This [backup script](https://gist.github.com/jennielees/472e926f4d924c4d1634) helps save you from re-adding all your data, but you have to run it **before** adding the new `user_id` column, or comment that out temporarily.

```
$ python backup.py
$ sqlite3 desserts.db
sqlite3> DROP TABLE dessert;
$ python models.py
# uncomment load_data and comment out save_data at the bottom of backup.py
$ python backup.py
```

Now your `.schema` should show the `dessert` table having a `user_id`, which is going to be null for everyone at first if you did the backup and import routine.

## Accessing Data

Create a User using Python for now.

```
$ python
>>> from models import *
>>> my_user = User('jennie', 'secret', 'jennie@hackbrightacademy.com', 'Jennie', '')
>>> db.session.add(my_user)
>>> db.session.commit()
```

Check using SQLite or Python that the user ID is 1. Now run a manual "fix-it" SQL statement to make all those existing desserts belong to this user:

```
$ sqlite3 desserts.db
sqlite> UPDATE dessert SET user_id=1;
```

OK, back to Python.

```
$ python
>>> from models import *
>>> for dessert in Dessert.query.all():
...     print dessert.user.name
```

What happened? What if you change `name` to something else?

Can you go from `User` to `Dessert`?

Change the `db.relationship` line to be:

```
user = db.relationship("User", backref="desserts")
```

Now you should be able to access the user's desserts via `user.desserts`, too!

Creating a relationship works the same way.

```
my_user = User.query.get(1)  # get the User with id 1
dessert = Dessert('Chocolate', 5, 100)
dessert.user = my_user
db.session.add(dessert)
db.session.commit()
```

You can also update an existing dessert just by setting `dessert.user` equal to a `User` object.

## The Hard, Vague Part You Have To Do

Using the user-management code you already wrote (yay!) - you can find a gist of the SQL functions we wrote together converted to SQLAlchemy [here](https://gist.github.com/jennielees/1801044b5c2975a358d1) - add user login into your desserts app.

* The user should have to log in (or create an account) first.
* The desserts list should only show that user's desserts.
* When the user creates a dessert, the app should associate the dessert with that user.
* When the user tries to delete a dessert, the app should check that the dessert belongs to that user.

Feel free to extend this to do even more if you have time.

How can you test this automatically? What manual testing do you have to do?

### A note on Sessions

To keep track of the user who is logged in, we can follow this outline logic:

* log the user in
* set a "session" variable so that user's browser gets associated with the user server-side
* check if there is a stored user before performing other actions, like listing desserts

You need to import `session` from Flask ([documentation](http://flask.pocoo.org/docs/0.10/quickstart/#sessions)). Once done so, you can treat it like a dictionary that has a special association with a specific browser (because it's stored a cookie on that browser). When the browser makes a new request, it sends along the cookie, which the Flask app decodes to get the right session dictionary.

Once the user logs in, you can store their ID:

```
session["user_id"] = user.id
```

Then for other functions, like adding a dessert, you can check if there is a user present in the session - remember `.get()` on a dictionary returns `None` by default if there's nothing stored:

```
user_id = session.get("user_id")
if user_id:
   # ... user is logged in ...
   user = User.query.get(user_id)
else:
   # ... no user is logged in ...
```

**Why store the id and not the user object?** Well, the database connection only exists for the lifetime of the request, so it gets thrown away when we've finished sending our page to the user. If we try doing stuff to the `User` object without an active database connection, SQLAlchemy gets very unhappy. Try it and see!
