---
layout: post
title: First Steps with Flask
week: 2
---

## Installing Flask

Before we can import the Flask code into our own app, we need to install Flask. The Python Package Index (aka `pip`) is our friend here - it's a central repository of all Python packages, so we don't need to jump through hoops to install things. All we need to do is type this in a terminal:

```
pip install flask
```

Oh. That probably didn't work. 

If you got **command not found**: go to the [pip install page](https://pip.pypa.io/en/latest/installing.html), and follow the instructions to download `get-pip.py` and run it.

You will probably have to run it as an administrator using the `sudo` (super-user do) command:

```
sudo python get-pip.py
```

Read any error messages carefully!

If you ran pip successfully but it failed because of **permissions**, that's because you were running it as your local user, not an administrator.

There are two options here.

First, you can simply override and use `sudo` to install it as an administrator. This is quick but it can also lead to trouble, especially if you are working with multiple apps on your computer that might need different versions of the same libraries.

The "right" way to do it is with a `virtualenv`. This [nifty command](https://virtualenv.pypa.io/en/latest/) creates isolated virtual environments on your machine.

To [install virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/), start with `pip` and install it systemwide with `sudo`:

```
sudo pip install virtualenv
```

Then make a new environment:

```
virtualenv venv
```

This will create a new virtual environment located inside the `venv` directory. You can call it anything you like instead of `venv` - just note that you need to remember where you put it, so you can get into it at any time:

```
source venv/bin/activate
```

You'll need to do this whenever you open a new terminal window, and this command is relative, so only works if you are in the directory which contains `venv`.


Reference: [So You Want To Install A Python Package](http://dubroy.com/blog/so-you-want-to-install-a-python-package)

## A Basic App

Phew. So we have Flask!

To create a basic app that just has one route, start with this:

```
from flask import Flask
app = Flask(__name__) 

@app.route('/')
def index():
    return 'Hello'

if __name__=='__main__':
    app.run()
```

Save as something like `app.py` and then run from your terminal:

```
python app.py
 * Running on http://127.0.0.1:5000/
```

Open up [http://localhost:5000/](http://localhost:5000/) from your web browser. If using Firefox, you might find it easier to go to [http://127.0.0.1:5000](http://127.0.0.1:5000/) -- these are the same thing.

You should see a pretty ugly "page" with just the word 'Hello'! Look at the terminal and check out what it's printing -- you should see the incoming HTTP requests, e.g. `"GET / HTTP/1.1"`.

### Adding a Template

Flask has a built in function `render_template` which looks in the `templates` directory and returns the matching file.

In order to use this function, you need to **import** it: change your import line to look like

```
from flask import Flask, render_template
```

Create a `templates` directory and a HTML file with some simple content. We can then serve this up from a view function: the following function will map the URL `http://localhost:5000/hello` to the contents of `templates/hello.html`.

```
@app.route('/hello')
def hello():
    return render_template('hello.html')
```

If you are adding it on top of your `index` function, make sure they have different names. You can't redefine the same function twice.

Run your server and visit your new route. You should see your page!

### Pro Tips

By default Flask doesn't reload when the file changes, but to save ourselves a bunch of stopping and starting, we can run it in debug mode:

```
app.run(debug=True)
```

Flask dynamically loads HTML files when they're requested, so you don't need to reload if you're only making HTML changes.

### Stylin'

We also might want to serve up some CSS and JavaScript files to make our HTML file pretty. Flask also has a built-in place to look for these: the `static` directory. This is mapped directly to the `/static/` URL: a file called `style.css` living in the `static` directory locally has the URL `/static/style.css`.

Try adding a really simple CSS file to your HTML page. ([Reminder](https://www.washington.edu/accessit/webdesign/student/unit5/module2/lesson1.htm))

### Template Variables

Serving up static files is fun, but what about some dynamic stuff?!

Flask allows us to "pick out" variables from the URL path. For example:

```
/articles/politics
```

could map to an `articles` function with the variable `politics`. This saves us a bunch of time, as we don't have to manually define the same function over and over again, and is also a lot more flexible!

The way that we do this is firstly by modifying the route:

```
@app.route('/hello/<name>')
```

This means that Flask will match routes of the kind `/hello/something` and put the "something" into the variable `name`.

We then need a place to receive this, which is on the next line, when we define our function signature:

```
def hello(name):
```

The arguments inside the parentheses for your view functions have to match the "patterns" defined inside angle brackets in your route. ([Need a refresher on functions?](http://learnpythonthehardway.org/book/ex18.html))

Together this looks like:

```
@app.route('/hello/<name>')
def hello(name):
   ...
```

You should notice that if you don't change anything else, the output of the view is no different. That's because we have to do one final thing with the `name` variable, send it through to the template. (But we can do a lot more with it too!)

Firstly, we add `name` as an extra argument inside the template render function. Any local variable can go in here -- it doesn't have to be one that came from the route.

```
render_template('hello_name.html', name=name)
```

And finally, we tell the template to insert the name in the HTML:

```
<h1>Hello, {%raw%}{{name}}{%endraw%}</h1>
```

The `{%raw%}{{ name }}{%endraw%}` syntax is [Jinja](http://jinja.pocoo.org/docs/dev/templates/), but also affectionately called "handlebars style" or "mustaches" (not to be confused with a couple of Javascript libraries which are actually called Handlebars and Mustache!).

Try putting this all together.

What happens if you visit just `/hello/`?

Can you break it by putting in strange inputs?

Can you add an `if` statement to send a different template depending on what `name` is?

### More Exciting Variables

Let's do something more fun inside the template. Well.. a little more fun.

Create a new view called `count`.

```
@app.route('/count')
def count():
   ...
```

Now create a HTML page called `counter.html` that has the following content:

```
<ul>
{% raw %}
{% for number in numbers %}
  <li>{{ number }}</li>
{% endfor %}
{% endraw %}
</ul>
```

The `for` loop inside Jinja uses the `{% raw %}{% .. %}{% endraw %}` syntax and must be closed with an `endfor` statement. This does pretty much what you'd expect - it loops through a variable called `numbers`, assiging each item to the local variable `number`. I can then print `number` out within a `<li>` element.

To get `numbers` into the template, it's the same idea as with the name above. Although, we need to actually define it first, as we're not relying on the route this time.

```
@app.route('/count')
def count():
    numbers = range(3)   # the range(n) function generates a list:
                         # [1, 2, .. n]
    return render_template('counter.html', numbers=numbers)
```

Can you make it say "ah ah ah!" after each number?

Can you use the `{% raw %}{% if %}{% endraw %}` statement in the template to only say "ah ah ah!" sometimes? ([Jinja reference](http://jinja.pocoo.org/docs/dev/templates/))

If you want to visualise what's going on here, use the `print` command to print out whatever you like inside the view function. This will appear in your terminal output. Sadly you can't `print` in the template, but using the `{{ foo }}` syntax will insert the contents of the variable `foo`.

### Enter Pinterest

We're going to be building our own Pinterest app. The first step is getting the static front-end working!

Clone [this GitHub repo](https://github.com/penelopy/pin_a_latte):

```
git clone https://github.com/penelopy/pin_a_latte.git
```

See if you can get Flask to serve this site up as-is. You'll need to move some files around...

Now pick an element (or more) from the page and turn it into a **dynamic** element. For example, try changing the hardcoded name "Stephanie" to something that comes from the URL.

Can you figure out how to put the contents of each "pin" into a Python list of dictionaries and use that to populate the page?

You will need to send the pins down inside `render_template` and use a `for` loop inside Jinja. 

Your data structure might look something like this:

```
    pins = [
        {
            'image': '/static/images/paws.jpg',
            'caption': 'Paws',
            'avatar': '/static/images/android_boy.jpg',
            'name': 'Dwayne Stewart',
            'category': 'Latte Art'
        },
        {
            'image': '/static/images/pretty.jpg',
            'caption': "Is this a swan? Whatever - it's pretty!",
            'avatar': '/static/images/woman_italy.jpg',
            'name': 'Nuria Cohen',
            'category': 'Love My Latte'
        },
        ...
    ]
```

(Notice how I use single quotes mostly, but when my string contains an apostrophe, I'm forced to use double quotes. Python doesn't care which you use.)

The goal here is not to spend forever typing out the pin content -- just do a few. You should be able to access the contents inside the for loop like this:

```
{% raw %}
{% for pin in pins %}
   .. {{ pin.image }} ..
   .. {{ pin.avatar }} ..
   .. {{ pin.name }} ..
   etc.
{% endfor %}
{% endraw %}
```

### Challenges (Optional)

Can you use a dynamic URL route to filter pins by creator? Try doing it by looping through the dictionary on the server and then try it inside the template. Which felt easiest? What problems did you encounter?

Can you use a dynamic URL with the search form to implement a basic search? The `methods` argument to `route` allows you to receive POST data, and `request.form` will give you the form contents. ([Documentation](http://flask.pocoo.org/docs/0.10/quickstart/#the-request-object))

```
@app.route('/search', methods=['POST'])
def my_search():
    print request.form
    ...
```

Set a favicon for the page.

Make the page fluid (you might need to copy-paste a few more pins to do this). Every N-th item, you'll see a new `<div class="col-5">` statement in the HTML (and the previous `<div>` will be closed). 

Using the `loop.index` variable in the template, you can use an `if` statement with the modulo operator:

```
{%raw%}{% if loop.index % 10 == 0 %}{%endraw%}
```

This will evaluate to True for every 10th item, as an example. Given this, can you add in the new `<div>` columns?