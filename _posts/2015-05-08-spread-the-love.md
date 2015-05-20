---
layout: post
title: Spread the Love
week: 3
---

## Enter Spreadsheets

In class, we heard about how all kinds of data can power an app. We're going to get our feet wet with some spreadsheets at first!

First off, let's look at a simple spreadsheet.

Log into our test Google account and head to [Google Drive](https://drive.google.com/drive/my-drive).

```
username: hbspreadsheets
password: pythonrocks
```

You should see a spreadsheet called ["Simple Sheet"](https://docs.google.com/spreadsheets/d/199UgYhHYOIYRgQez85NNXEE8wGO34IhdkIejd1su1Og/edit#gid=0). Open it up to take a look at what's inside.

We want to build an app that lets our favourite superheroes log in and will automatically order them a serving of their preferred dessert.

First, let's figure out how to access this spreadsheet data in Python!

### GSpread

There is a neat Python library called [GSpread](https://github.com/burnash/gspread) that allows access to Google spreadsheets, so we don't have to write a bunch of Google API code. Yay!

Go to the homepage and read through the README. (The contents of the README are automatically displayed when you visit a GitHub repository's homepage.)

As you can see, this library allows you to select spreadsheets and get values from them. Cool. Let's install it (and two supporting libraries -- the Google OAuth library, and a cryptography library for dealing with secure credentials):

```
pip install gspread oauth2client PyOpenSSL
```

(If you didn't get your virtualenv set up last week, you can choose to set it up now, or to retry the `pip` command with `sudo` in front to run it as an admin.)

In order to authenticate with Google, we need to set up our credentials. This has already been done for the `hbspreadsheets` account. Download [this file](../public/data/spreadsheet_credentials.json) to your working directory.

This "boilerplate" code will handle the authentication step for you. When using data from other sources, we often have to perform a little bit of setup like this first.

Copy this to a file and run it:

```
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('spreadsheet_credentials.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)
```

If it worked, nothing should happen. That's ok.

Can you figure out from the GSpread Readme how to open the spreadsheet called "Simple Sheet" and print out the contents of Sheet1 in sentences, e.g. "Black Widow loves ice cream"? (Don't worry about plurals for now.)

<pre class="hint">
You'll need to figure out how to open the spreadsheet, select the worksheet Sheet1, and then iterate through the contents.

sh = gc.open("Simple Sheet")
worksheet = sh.sheet1

for row in worksheet.get_all_values():
    # do something. row is a list; try printing row, row[0], etc.
</pre>

## Making this into an app

You have two choices when you want to make this into an app.

Firstly, a command-line app that doesn't use the web at all. Sometimes it's a lot easier to test out ideas this way. However, this is a class about web development, so we'll skip this for now. If you want to figure out how to do this, start with `raw_input()`.

Secondly, Flask!

The breakdown of our Flask app is as follows:

* A page where the user can enter the hero name into a form
* A page that receives the submitted form and prints out the result

If you worked on form POSTing last week, you can jump right in. If not, here's how it works.

### POSTing data

Most basic web requests use GET. POST is useful, however, when you want to send data along with your request. You get to do so in a safer manner than GET,which puts all the data into the query string.

Create a simple Flask app that has two routes.

```
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=['POST'])
def submit():
    return render_template("submit.html")

if __name__=='__main__':
    app.run(debug=True)
```

Notice the `methods=['POST']` inside the route declaration for `submit()`. That means we are only expecting requests to POST to us -- any GET requests will fail.

Create the required HTML pages too. At first, make `index.html` have a simple form in it that POSTs a text field called `name` to `/submit`, and `submit.html` can be empty.

With just these pieces, try running the app and submitting the form. If you saw the contents of `submit.html`, you're good!

#### Getting the data out

So how do we get the contents of the `name` that was submitted with the form?

`request.form`.

Try printing the contents of `request.form` inside `submit()`. Make sure you added `request` to the import line (see above)! You should see something like

```
ImmutableMultiDict([('name', u'whatever you entered')])
```

This funky-looking thing is really just a wrapper around `dict`, our friendly dictionary class. It behaves just like a normal dictionary. So, to get `name`, we just need to do `request.form.get('name')`.

Get the submitted name and using the templating syntax we learnt last week, pass it through to the `submit.html` template.

### Making it smart

OK, so we can get the submitted name. How do we combine that with the spreadsheet code we just got working?

First, let's wrap the spreadsheet code in a function so our code stays nice and clean. Paste it into your app file:

```
def get_spreadsheet_data():
    # your code here
    # ...
```

Pull out the `import` lines and put them at the top with the others.

Instead of printing out the contents of the sheet, make the function `return` the values of the spreadsheet.

[Reference solution here.](https://gist.github.com/jennielees/533418775d09fd187f40)

Now you need to loop through those values and find the row that matches the entered name.

<pre class="hint">
data = get_spreadsheet_data()
dessert = 'unknown'  # so that we have a default value
for row in data:
    if row[0] == name:
        dessert = row[1]
</pre>

Finally, put that value in the template so our app actually works. You can get creative here - but start simple to make sure it is doing the right thing. What happens if you put in a name that isn't recognised? Can you put in a helpful message here?

Step back a moment once you get it working: you just built a data-driven app! AWESOME!

### Challenges

Change the text box into a drop down list of possible names.

How can you avoid having to go check the spreadsheet every time the form is submitted?

How could you deal with the user's capitalization? Methods like `.lower()`, `.title()`, and `.upper()` could be of use here.

Can you figure out how to change data in the spreadsheet using `gspread`? Make a copy of the spreadsheet before doing so, and point your code at that, so others don't end up broken. Share your copied spreadsheet with `81471696663-0pbl7nl2tl26l7qjiqogct3580ilkuu5@developer.gserviceaccount.com` so gspread can read it.

Add a third (or more) column to the spreadsheet with extra data and enhance the app. Ideas could include pictures of the superheroes or desserts, calories or ass-kicking values, etc...! (If changing the spreadsheet, remember to make a copy and work on that.)

Create your own spreadsheet (or use one you have handy) and build a similar app around it! There is a street sweeping data sheet in the google account, if you want a real challenge.