---
layout: post
title: Project Resources
week: 9
---

This page has two sample projects. The 'Pirate Bar' project is broken out in detail step-by-step, though has some open-ended pieces at the end. The 'Street Sweeping' project is left at a high level as an exercise for you.

## Sample Project 1: Pirate Bar

We are going to write a bar manager for a pirate bar. The goal of this app is to **take input** and **use a database**.

The bar manager will:

* Keep track of drink stock
* Keep track of customer preferences
* Suggest drink recipes when a customer orders
* Keep track of the bill for each customer

We will start out by sketching the skeleton of our app. But first, a new slate:

```
$ mkdir barrr
$ cd barrr
$ touch barrr.py
```

In `barrr.py`:

We outline the main logic of our app in the `main()` function and define 'empty' functions for the logic steps we've identified.

Our app needs to keep track of customers, so we need some way of asking the customer who they are. Then we need to make them a drink. This function will have to do the heavy lifting around preferences and stock levels. Finally we charge the customer for the drink we made.

```
def look_up_customer(name):
    return

def make_drink(customer):
    return

def charge_customer_for_drink(customer, drink):
    return

def main():
    # Ask customer for name and look up their saved preferences
    customer_name = raw_input("What be yer name, swab? ")
    customer = look_up_customer(customer_name)
    
    # Make the customer a drink
    drink = make_drink(customer)
    
    # Charge it to the customer's bill
    charge_customer_for_drink(customer, drink)

if __name__=="__main__":
    main()

```

Let's fill in the functions in order.

We need to save customer data and look customers up, so `look_up_customer` needs to have an accompanying database model too. Let's define that first.

What do we need to save for a customer? Their preferences and their name, along with their bill. In a separate file called `models.py` we'll create this `Customer`:

```
from peewee import *

db = SqliteDatabase('peewee.db')

class Customer(Model):
    name = CharField()
    likes_strong = BooleanField()
    likes_sweet  = BooleanField()
    likes_salty  = BooleanField()
    likes_bitter = BooleanField()
    likes_fruity = BooleanField()
    bill = IntegerField()
```

Now, back in `barrr.py`, we add the import to the top of the file so we can access `db` and `Customer`:

```
from models import *
```

And we start filling out `look_up_customer`.

```
def look_up_customer(name):
    # Get the customer from the database by name
    
    # If the customer isn't found, create a new one
```

```
def look_up_customer(name):
    # Get the customer from the database by name
    try:
        cust = Customer.get(Customer.name=name)
        return cust
    # If the customer isn't found, create a new one
    except:
        cust = Customer(name=name)
        
        strong = raw_input("Do ye like yer drink strong? ")
        if strong.lower() == "yes" or "y":
            cust.likes_strong = True
        else:
            cust.likes_strong = False
        
        ...
```

That "strong" exchange would be copied and pasted five more times, which seems tedious. Let's use some Python-ninja skills to condense it down.


```
def look_up_customer(name):
    # Get the customer from the database by name
    try:
        cust = Customer.get(Customer.name==name)
        return cust
    # If the customer isn't found, create a new one
    except:
        cust = Customer(name=name)
        
        for flav in ('strong', 'salty', 'bitter', 'sweet', 'fruity'):
            likes = raw_input("Do ye like yer drink {}? ".format(flav)).lower()
            likes_bool = likes in ('yes', 'y')
            # setattr sets the value of the attribute by name
            # so setattr(cust, name, 'bob')
            # sets cust.name = 'bob'
            # in this following code we use string formatting
            # to dynamically set likes_strong, likes_salty etc.
            # since flav iterates through 'strong', 'salty', ...
            setattr(cust, 'likes_{}'.format(flav), likes_bool)
        
        cust.bill = 0
        cust.save()
        
        print cust # a good bartender repeats back!
        return cust
```

Printing the `Customer` object is kind of messy now, so let's update it with a method that makes it printable:

```
class Customer(Model):
    name = CharField()
    likes_strong = BooleanField()
    likes_sweet  = BooleanField()
    likes_salty  = BooleanField()
    likes_bitter = BooleanField()
    likes_fruity = BooleanField()
    
    def __repr__(self):
        return """Customer: {}
    Likes strong: {}, 
    Likes sweet: {},
    Likes salty: {}, 
    Likes bitter: {}, 
    Likes fruity: {}""".format(self.name, self.likes_strong, self.likes_sweet, self.likes_salty, self.likes_bitter, self.likes_fruity)
```

To **test**, we run twice with the same pirate name. Unless we made a typo, we should only be asked for the preferences once. 

Sweet.

### Making the drink

Now let's fill out `make_drink`.

```
def make_drink(customer):
    # pick randomly from each set of ingredients for each flavour type the customer likes
    
    # decrease the stock when we use up each ingredient

```

So it looks like we probably need some ingredients, right? Back to `models.py`. Since 'salty', 'sweet' etc are categories of ingredients, let's model them as such:

```
class Category(Model):
    name = CharField()

class Ingredient(Model):
    name = CharField()
    stock = IntegerField()
    category = ForeignKeyField(Category, related_name='members')
    
    def __repr__(self):
        return "{} {}s".format(self.stock, self.name)
```

We also need to save some ingredients. Let's do that in the python console.

```
$ python
>>> from models import *
>>> salty = Category(name='salty')
>>> salty.save()
>>> strong = Category(name='strong')
>>> strong.save()
>>> # ... etc
>>> rum = Ingredient(name='a glug of rum', stock=30, category=strong)
>>> rum.save()
```
(Could you think of a way to do this with less typing?)

Check the ingredients saved:

```
>>> for i in Ingredient.select():
...    print i
```

Back to `barrr.py` we're ready to start filling things in. We add `import random` at the top of our file, then:

```
def make_drink(customer):
    # pick randomly from each set of ingredients for each flavour type the customer likes
    ingredients_used = []
    
    if customer.likes_salty:
        cat = Category.get(Category.name=='salty')
        # turn category members into a list
        random_candidates = []
        for item in cat.members:
            random_candidates.append(item)
        # now pick randomly
        chosen = random.choice(random_candidates)
        ingredients_used.append(chosen)
    
    
    # decrease the stock when we use up each ingredient

```

This is already looking pretty heavy, so let's do two things. Give the choice its own function, and try to rewrite it with a list comprehension, Python's way of making the `for` loop above more compact.

```
def get_random_ingredient(category):
    random_candidates = [i for i in category.members]
    return random.choice(random_candidates)
```

These two pieces of syntax create identical lists:

```
mylist = [i for i in category.members]

mylist = []
for i in category.members:
    mylist.append(i)
```

Let's also rewrite to use `getattr`, a fun helper that can save us more typing!


```
def make_drink(customer):
    # pick randomly from each set of ingredients for each flavour type the customer likes
    ingredients_used = []
    
    for flav in ('salty', 'sweet', 'bitter', 'strong', 'fruity'):
        # getattr(customer, 'name') is the same as saying
        # customer.name
        # so we can dynamically create it here
        if getattr(customer, 'likes_{}'.format(flav)):
            cat = Category.get(Category.name==flav)
            ing = get_random_ingredient(cat)
            ingredients_used.append(ing)    
    
    # decrease the stock when we use up each ingredient
            ing.stock -= 1
            ing.save()
          
    # convert the Ingredient list into a list of strings
    # then join together with a comma for printing  
    drink_string = ", ".join([i.name for i in ingredients_used])           
    print "Made a drink with: {}".format(drink_string)
            
    return ingredients_used
```

Note: What happens if the customer doesn't like anything? What if we have no 'base' drink to offer - is it ok to just serve up a cherry and nothing else?

What happens if the ingredient is out of stock?

Finally, we'll charge the customer for the drink.

```
def charge_customer_for_drink(customer, drink):
    # drink is a list
    # let us charge based on how many ingredients we used
    
    ingredient_charge = 3
    drink_price = ingredient_charge*len(drink)
    
    customer.bill += drink_price
    customer.save()
    
    print "Charged {} ${} for this drink. Total bill unpaid: ${}".format(customer.name, drink_price, customer.bill)
    
```

Here's all that code [in a gist](https://gist.github.com/jennielees/e86f7e4ad223575aedc2) for you to check against.

### Next Steps

This is a complete app - you can easily imagine how the web front-end would fit together with this. However, you might want to add more functionality. For example:

* Let the customer pay their bill
* Let the manager restock the bar
* Add a specials menu (or any kind of menu)

Perhaps you could use `sys.argv` to run the app in 'manager mode', eg. by typing `python barrr.py manager`.

Perhaps when the customer tells you their name, instead of automatically serving a drink, you ask them what they would like to do.


## Sample Project 2: Street Sweeping Alerts

Be sure to have [worked through the street sweeping database](http://labs.bewd.co/data-meet-app/) exercise first.

We have a mini app (from that exercise) that will:

* Given a street number and name, look up the times for that block

We want to extend that to:

* User can save their street number and name
* User can get alerted by text or email if their street is going to be swept tomorrow
* User can cancel alerts

How will the user enter their details in the first place? We will start off using the command line and show you how to make a simple Flask app to join things together.

Create a `User` model and a `UserBlock` model. Extend your existing app to:

* Ask the user for their name, and either their email or phone number
* Ask the user for a block they want to monitor, or if they are already a user, ask if they want to cancel monitoring or add more blocks.
* Save this data to the database

Then make your app perform the following logic:

* When run, check through all users who have got monitoring enabled
* Select all blocks for each user
* Print out the time that each block is next swept for that user
* If the time is tomorrow, print "ALERT ALERT"

The final step is to figure out how to change the "print ALERT" to sending a real one via Twilio and Mandrill (or other email API).

_Alternatively_ you could extend to take input via twitter not command line, and reply via twitter as well. People might not want to openly send their addresses by tweet, so you may need to think about direct messages.

The Flask section is coming soon! :)

