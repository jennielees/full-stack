---
layout: post
title: ORM Wrestling
week: 5
---

## What's an ORM?

This week we will be working with ORMs. An ORM (short for Object Relational Model) is a mega-convenience that translates a relational database into a set of Python objects. It's much easier to work with Python objects than construct raw SQL statements all the time, as we shall (hopefully) see!

There are lots of ORMs to choose from. We will be using one of the most popular Python libraries [SQLALchemy](http://sqlalchemy.org). I use this in production every day and it's super powerful, but as with any powerful tool, can take a bit of getting used to. Because we're using Flask, we can also use the [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/) library which makes things a bit easier.

Let's start by installing them:

```
pip install sqlalchemy flask-sqlalchemy
```

## An interactive example

**Work in pairs** for this exercise. Explaining what the code does to someone else will help you understand it a lot more easily than running through it in your head! Use the pairing workstations or your own laptops.

Clone [this sample app](https://github.com/jennielees/flask-sqlalchemy-example) locally.

```
git clone https://github.com/jennielees/flask-sqlalchemy-example
```

Create the database tables:

```
python models.py
```

Then run the app:

```
python app.py
```

Check it out. What does it do? Add an item or two.

### Inside the Models

Open `models.py` and take a look at the model definitions.

Now open up SQLite and compare what's in the database to the Python file:

```
sqlite3 desserts.db
sqlite> .schema
CREATE TABLE menu (
    id INTEGER NOT NULL,
    name VARCHAR(100),
    PRIMARY KEY (id)
);
CREATE TABLE dessert (
    id INTEGER NOT NULL,
    price FLOAT,
    calories INTEGER,
    name VARCHAR(100),
    PRIMARY KEY (id)
);
```

And let's see how those desserts you created in the app look:

```
sqlite> SELECT * FROM dessert;
```

As you can see, lines like

```
name = db.Column(db.String(100))
```

become SQL like:

```
name VARCHAR(100)
```

and Flask-SQLAlchemy takes care of stuff like NOT NULL, table names, and even constructing and running the SQL statement for us. (The line at the bottom of `models.py`, `db.create_all()`, is where it actually gets created.)

Pretty neat, huh. We also don't have to worry too much about primary keys. Simply defining `primary_key=True` on an `Integer` means that SQLAlchemy will take care of updating it for us, as long as we ignore it when creating items:

```
dessert = Dessert(new_name, new_price, new_calories)
```

Notice how there is no `id` provided. Yet when you did the `SELECT` to see what was in the database, your items should have had an ID!

You can also access these models from the command line. This is super useful for debugging and testing. Let's play with them now:

```
python
>>> from models import *
>>> for dessert in Dessert.query.all():
...     print dessert.name
```

When we run `from models import *`, that imports everything defined within `models.py`. So in the example file, that will import `Dessert`, `Menu` and `create_dessert`. Remember stuff inside a function is local to that function only.

`import` statements do not trigger `if __name__ == '__main__'` lines. That 'if' statement only runs if the file is run directly. This allows us to do useful things like put our "create database tables" code in a sensible place, while also ensuring that it doesn't get run every time we want to use our models. You can experiment with this by moving the `db.create_all()` statement outside the `if`. What happens now when you `import`?

(Nothing bad, but the app will be trying to create the database tables whenever you import, which is a little unnecessary. For databases other than SQLite, this tends to throw a nasty "Oi mate, the tables already exist" error.)

## SQLAlchemy Commands

Here are the main commands you'll be using to interact with database items now. I'm using `Dessert` as an example, but all of these apply to **any** class that inherits from `db.Model`, so in the example provided, they would also work just as well on `Menu`.

[Reference](https://pythonhosted.org/Flask-SQLAlchemy/queries.html)

`Dessert.query.all()` fetches all the Dessert items in the database. This returns a list.

`new_dessert = Dessert('chocolate', 5, 200)` creates a Dessert instance. This doesn't alert the database to its existence -- it's the exact same syntax as creating any kind of object.

`db.session.add(new_dessert)` tells the database to keep track of `new_dessert`, which is presumably the thing you created with the previous line. This doesn't save it to the database yet.

`db.session.commit()` saves all pending state (since you last did a `commit`) to the database.

Try adding (and committing) new desserts using the command line.

`Dessert.query.filter_by(price=5)` filters the items in the database by the provided criteria, in this case, `price=5`. Try it! What does it return? How can you iterate through it?

`dessert = Dessert.query.get(1)` gets the item with ID 1. This is really useful when trying to access a specific item! It just returns a single item.

`db.session.delete(dessert)` deletes the `dessert` you retrieved above. You need to commit to make it reality, though.

To update an item, you just need to get hold of it, via a query or a `get`, and then change its attributes.

```
dessert = Dessert.query.get(1)
dessert.price = 20  # Raising the prices due to rent increase
db.session.commit()
```

You only need to `add` an item to the session if it's brand new. If you got it from the database in the first place, as in this example, the session already knows about it. This works for groups of objects too:

```
desserts = Dessert.query.all()
for dessert in desserts:
    dessert.price += 10  # It's a really bad rent increase
db.session.commit()
```

In this snippet, I called `commit` once I'd gone through every dessert. The `commit` operation is quite heavyweight as it has to do a bunch of sanity checking and data saving. It's usually best to call this outside a for loop rather than inside it, but for small apps, it doesn't make a huge difference.

You should be able to figure out the SQL equivalents for all of these commands. Luckily, you don't have to write it any more (and I'm not going to test you on it!), but it's really useful to know what's happening under the hood.

Reference: [Last week's Users exercise](https://gist.github.com/jennielees/1801044b5c2975a358d1) rewritten with SQLAlchemy instead of raw SQL.

## Building our app out

You probably noticed our app was... missing some useful functionality. Let's add it!

First, let's make it look a bit nicer with Bootstrap. I've used a **branch** in git to create a modified version of the app with Bootstrap enabled.

```
git branch
```

This command shows you all the branches in the git repository. To get the Bootstrap one:

```
git checkout bootstrap
```

If you made local changes, Git will usually be cool with a branch change and keep your changed files. However, if the changes conflict with mine, you'll see an error message (in this example I changed my `index.html`):

```
error: Your local changes to the following files would be overwritten by checkout:
    templates/index.html
Please, commit your changes or stash them before you can switch branches.
Aborting
```

To temporarily hide your changes and get my version of the files, you can `stash` them.

```
git stash
```

Then `git checkout bootstrap` should work. To get your changes back, you can run `git stash pop` to pop them off the stash. However, you will probably see a **merge conflict** warning, which means that whichever files were modified have a great big ugly merge message inside them:

{% raw %}
```
<<<<<<< Updated upstream
{% include 'header.html' %}
=======
<h3>Jen's Awesome Dessert Menu</h3>
>>>>>>> Stashed changes
```
{% endraw %}

In this case, the code above the `====` is the stuff from the `bootstrap` changes, and the stuff below the `====` is my stashed change. I can choose which bits to delete or update, but I need to get rid of all the `===`, `<<<<` and `>>>>` lines at least, or my app will run into problems.

## Bootstrap Integration

The bootstrap integration is pretty straightforward. I'm using bootstrap as an easy way to make the app look a bit nicer, but you can spend some time improving it if you like (I recommend you follow the rest of this lab through before doing so, to minimize git merge errors).

[Blasting Off With Bootstrap](https://www.codeschool.com/courses/blasting-off-with-bootstrap) // [Bootstrap Reference](http://getbootstrap.com/components/)

In order to integrate Bootstrap, I added a `header.html` template with the Bootstrap links, and then used {%raw%}`{% include 'header.html' %}`{%endraw%} at the top of my other templates.

## Validation

You probably noticed that there are some serious flaws in our "create a dessert" process. For one, the user could leave boxes empty and we don't do anything about it!

Let's add **validation**. Check out the `validation` branch:

```
git checkout validation
```

This branch adds two main things.

Firstly, we updated the `create_dessert` method in `models.py`. Check it out!

Secondly, we added a (hopefully familiar) `test_models.py` file that helps us test our `create_dessert` function in a reliable way, without having to reload and submit the form a gazillion times.

The pattern we are using is a 'try-except' one. [Codecademy: Exceptions Practice](http://www.codecademy.com/courses/python-intermediate-en-D8LVD/0/1)

Inside our `add` view, we'll **try** to create a dessert and if that fails, our **except** will do something about it.

We then use this on the other side inside our `create_dessert` function. If the input we got wasn't right, we can `raise` an Exception and tell the caller!

Finally, inside our tests, we use a bit of sneaky Python to make sure that the creation didn't work:

```
    dessert = None

    try:
        dessert = create_dessert(None, None, None)
    except Exception:
        pass
    
    assert dessert is None
```

If a function like `create_dessert` raises an `Exception`, it means that it didn't succeed, so nothing ever gets assigned to `dessert` inside the `try` block. So we expect the function to cause an error, catch it harmlessly (with the do-nothing keyword `pass`) and then check that `dessert` is still `None`.

We need to initialize the `dessert` variable beforehand, though, otherwise the final line in the code above won't know what `dessert` is. Try commenting out the first line in your tests and see what happens. Does it have to be `None` or could the "original" value of `dessert` be anything?

## Deleting Items

To round out our app, let's introduce item deletion. In order to do this we'll create an 'item details' page which we can delete from.

```
git checkout details
```

In this code, we're using the `dessert.id` that we sort of forgot about. This primary key is a completely unique identifier for each dessert, so perfect for use when viewing or deleting items.

What's changed since the previous code?

We added a couple new views, a new template, and a `delete_dessert` method with tests. Try it out.

That's all there is in the git repository, so now we can make some changes without worrying about future merge conflicts :)

## Extending the App

Pick and choose from the following challenges! We will continue working on these on Thursday.

## Better Validation

The validation we introduced isn't particularly clever. For one thing, it doesn't check if an item already exists with the same name. Secondly, it doesn't check if the price and calories values are sensible ones (for example, I could create a chocolate dessert with 10000000 calories).

Extend the validation to be a bit more realistic.

## Are You Sure?

Deleting is pretty scary! Ask the user if they are sure they want to delete.

This could happen a couple of different ways:

* Javascript [confirm dialog](https://developer.mozilla.org/en-US/docs/Web/API/Window/confirm) saying "Are you sure? (OK/Cancel)"
* Javascript [prompt](http://www.codecademy.com/glossary/javascript/popup-boxes) that requires you to type in the dessert name to confirm
* Bootstrap [alert](http://www.tutorialrepublic.com/twitter-bootstrap-tutorial/bootstrap-alerts.php) in the same vein
* Python Flask view that requires you to click or type in something to confirm

Or think up your own!

## Updating an Item

Add the functionality to edit / update an item. You will probably want to reuse the `add.html` template. In order to make it easy to update an item, you can pre-populate the template with the existing item's values like this:

{% raw %}
```
<input  class="form-control" id="name_id" name="name_field" type="text" value="{{ dessert.name }}"/>
```
{% endraw %}

## Search

Add a search box to the index!

This search box should submit to a new Flask view that gets all the desserts matching the name entered by the user. Remember `Dessert.query.filter_by()` from earlier? You're gonna want to use that.

To extend this, you could also add an Advanced Search that gets all the desserts above or below a certain calorie or price threshold. Unfortunately `filter_by` only works for `=` type queries; if you want to filter for items above or below a value, you need to use the more clunky `Dessert.query.filter(Dessert.price >= 5)` syntax.

## Locally Grown

Add a new field to the `Dessert` model for the `origin` of the dessert. Changing existing SQL tables is funky. The easiest way is to delete the database and recreate it, but you will **lose all your data** this way:

```
rm desserts.db
python models.py
```

If you don't want to lose your data, you have two options.

First, you can manually write the SQL query to add the new field.

```
ALTER TABLE dessert ADD COLUMN location VARCHAR(100);
```

This could go wrong though, especially if you make a mistake in the query (SQLite doesn't let you remove columns, only add them).

Secondly, you can copy the data out, and then load it back in. You'll have to write a [little Python script](https://gist.github.com/jennielees/472e926f4d924c4d1634) to do that.

## Spruce it Up

Add a new field to `Dessert`, `image_url`, that you can use to save the URL to a picture of the dessert. Then use that in your HTML template to make your dessert list look a lot more tasty.

Also, dive into the Bootstrap world and see if you can make the whole thing look nicer.

If things like the decimal point formatting of prices has been annoying you, look at some of the Jinja options, [like this one](http://stackoverflow.com/questions/12681036/is-there-a-direct-approach-to-format-numbers-in-jinja2).

## Ordering

Add UI options to the dessert list to order by name, price or calories, using the server-side `Dessert.query.order_by('name')` syntax. You will need to add a parameter to your list route.
