---
layout: post
title: Deploying to the Outside World
week: 8
---

# Review: Flask and Forms

[Fork, then clone this app](https://github.com/jennielees/funky-music) and discuss in pairs.

What do you think is going on with the HTML pages? 

Check out the original source of the CSS (look in the files for a hint as to where to find it). Do you understand what Skeleton is?

How does data get into the form?

How does data get back to the browser?

Where does AJAX come into it? Can you think of a better way to do this?

What is Spotify's role in the app? Can you match the displayed information to the API data? [API Reference](https://developer.spotify.com/web-api/search-item/)

Can you fix the links to open the Spotify playlists properly? (Hint: look for `uri` not `href`)

## Form Quick Recap

Handy Form Checklist:

* Is the `action` set to the Flask server URL?
* Is the `method` set to POST?
* Do the `input` elements have names?
* Is there a `submit` button?

Handy Flask Checklist:

* Does the route have `methods=['POST']`?
* Do the names you are getting from `request.form` match the "foo" in `<input name='foo'>` in your HTML?
* Do you need to do any checks or validation?

# Let's Deploy!

We're going to push this app live so anyone can access it.  Sweet!

## How the Web Works

Web servers are, underneath it all, just computers running programs that know how to listen for HTTP requests. We've been writing these programs throughout the class. However, we've mostly gotten our servers to work on our local machines.

How does that translate to the outside world?

We could set up a Linux machine in a remote data center, install everything we need (Python, etc) and start our app running. Then instead of accessing http://localhost:5000/, we can just go to whatever the IP address of the machine is, and get our website. We can even register a domain name and point it at that IP address to make things easier to remember.

This is quite a lot of work, especially keeping everything up to date with the latest security fixes. So we're going to use Heroku to take care of a lot of the tedious parts for us.

## What Heroku Is and Isn't

Heroku provides a virtual web server, as opposed to a physical one; they create a 'sandbox' environment for you, where your code is running on the same machine as several other apps, but is completely unaware of that fact. As a result, you don't have all the same tools you might have on your local machine, but Heroku provide a lot of equivalents.

To get code on Heroku, you set up a new Git remote and just push your code to it. There are a couple things you need to do to make it a "runnable" app, but we'll go through those!

First, [create a Heroku account](https://signup.heroku.com/www-home-top) if you don't already have one.

Then [install the Heroku Toolbelt](https://toolbelt.heroku.com/). This set of tools makes it really easy to work with Heroku.

## Getting the Code Ready

To make our code into a Heroku app, we're going to basically follow the [Heroku Getting Started Guide](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) and the [Flask-specific help](https://devcenter.heroku.com/articles/getting-started-with-python-o).

First, log into Heroku:

```
$ heroku login
Enter your Heroku credentials.
Email: python@example.com
Password:
Authentication successful.
```

Install the Python package `gunicorn`, which is how we're going to run our app:

```
$ pip install gunicorn
```

We'll create a `Procfile`, which tells Heroku how to run the app. Put this line in a new file and save it as `Procfile`:

```
web: gunicorn app:app --log-file=-
```

Check this works with `foreman`, Heroku's tool for running apps locally.

```
$ foreman start
```

Notice how it ignores the port in `app.py` and binds to port 5000? We aren't triggering that `if __name__ == '__main__'` check, since gunicorn imports the app (`gunicorn app:app` is shorthand for gunicorn using `from app import app`).

Now, we need to make a `requirements.txt` file. This captures the Python libraries that we installed via Pip. Assuming you are working within a [virtual environment](https://github.com/kennethreitz/python-guide/blob/master/docs/dev/virtualenvs.rst), you can 'freeze' the libraries you have installed:

```
$ pip freeze > requirements.txt
```

You should only really have two main dependencies for your app, `requests` and `flask`, so your `requirements.txt` file should look something like this:

```
$ cat requirements.txt
Flask==0.10.1
Jinja2==2.7.3
MarkupSafe==0.23
Werkzeug==0.10.4
gunicorn==19.3.0
itsdangerous==0.24
requests==2.7.0
wsgiref==0.1.2
```

If there are a lot of other entries in this file, your virtualenv probably has a bunch of libraries you installed for other projects. When you deploy to Heroku, it will install all of these, which is pretty unnecessary --  make a clean virtualenv for this project, and freeze again. 

```
$ virtualenv musicapp
$ source venv/bin/activate
$ pip install flask requests gunicorn
```

Tip! For easier virtualenvs, try [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/).

Add the `requirements.txt` and `Procfile` to the git repo.

```
$ git add requirements.txt Procfile
$ git commit -m "Getting ready for Heroku"
```

## Pushing to Heroku

Creating a new Heroku app is simple with the toolbelt installed: there are a whole host of `heroku` commands we can now use!

```
$ heroku create
```

This creates a new app and sets up the Git remote `heroku` for you to push code to.

To deploy, push the code via Git:

```
$ git push heroku
```

You should see a bunch of stuff like:

```
remote: -----> Python app detected
remote: -----> Installing runtime (python-2.7.10)
remote: -----> Installing dependencies with pip
```

If you don't, perhaps you forgot to commit the `Procfile` or `requirements.txt`.

When your deploy is done, you should see the URL of your new Heroku app:

```
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing... done, 37.2MB
remote: -----> Launching... done, v3
remote:        https://desolate-beyond-5764.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy.... done.
To https://git.heroku.com/desolate-beyond-5764.git
```

You can then visit that URL in your browser, or use the command `heroku open`, to view it!

## What's going on?

The command `heroku logs` will show you some of the activity on your app. Using the `-t` flag shows a view of the latest logs that live-updates - try it and see what it does!

```
$ heroku logs -t
```

Ctrl-C will exit.

Heroku shuts down apps after a while so it costs them less to run. This means that sometimes apps take a little bit of time to load the first time they are visited.

## What's in a name?

First, you can rename your Heroku app from the random words it picks to something better. You can do this via the web (sign in to your [Heroku dashboard](https://dashboard.heroku.com/apps), go to the app, go to Settings and change the name) -- or via the command line:

```
$ heroku rename myappnewname
```

Putting your app behind a domain name (something.com instead of something.heroku.com) is pretty straightforward and explained in the [Custom Domains](https://devcenter.heroku.com/articles/custom-domains) article. You also need to tell Heroku about the new domain in the settings page for your app.

# Customizing things further

We're going to add a couple of new features to our music app.

First, let's show the contents of the playlists.

Add a new route:

```
@app.route('/playlist/<username>/<playlist_id>')
def playlist(username, playlist_id):
   ...
   return render_template('playlist.html', tracks=tracks)
```

You will need to:

* Change the links in the results page to link to `/playlist/<username>/<playlist_id>`. You can get the username (aka user ID) and playlist ID from the playlist dictionary you already have.
* Create a method `get_playlist_tracks(username, playlist_id)` that calls the corresponding [Spotify API endpoint](https://developer.spotify.com/web-api/console/get-playlist-tracks/#complete)
* Return those tracks and render them in the template. (Don't worry about the Javascript part to load more, unless you really want to.)

## Calling an authenticated API

We can start by testing out the code to call the Spotify API. We'll quickly find out that it requires authentication.

From the API docs, we can see that the URL for a playlist's tracks is:

```
https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}/tracks
```

However, if we try that with a sample playlist from the search 'happy', we get:

```
https://api.spotify.com/v1/users/russhitt/playlists/5PqcmszU9oDOpp7rDV1kuH/tracks
```

which, when we visit it, tells us we need authentication.

We're going to cheat (a little) and do our authentication via Spotify. In the [API page](https://developer.spotify.com/web-api/console/get-playlist-tracks/#complete) -- you will need a Spotify account -- hit "Get OAuth Token". Make sure you tick the 'view collaborative playlist' box.

Copy this token to a temporary text file or other good location.

Now, inside the Python interpreter, try this:

```
import requests
token = 'YOUR_TOKEN_YOU_JUST_COPIED'
headers = { 'Authorization': 'Bearer {}'.format(token) }
url = 'https://api.spotify.com/v1/users/russhitt/playlists/5PqcmszU9oDOpp7rDV1kuH/tracks'
requests.get(url, headers=headers).json()
```

This "Bearer" token with your pre-saved token should work to authenticate you. (Disclaimer: The token may expire after a while. We'll do proper OAuth on Thursday!)

Committing tokens like this to GitHub is a **bad idea**. They are sensitive and give anyone who has them access to do whatever they like with your account!

Instead, we can use **environment variables**.

Try this in your Terminal:

```
export SPOTIFY_TOKEN='YOUR_TOKEN_AGAIN'
```

and in Python:

```
import requests
import os
token = os.environ.get('SPOTIFY_TOKEN')
headers = { 'Authorization': 'Bearer {}'.format(token) }
url = 'https://api.spotify.com/v1/users/russhitt/playlists/5PqcmszU9oDOpp7rDV1kuH/tracks'
requests.get(url, headers=headers).json()
```

This should work just the same as before. Your Python code is actually asking your underlying operating system for the token! Note that the "export" is limited to the Terminal window you have open. You have to re-export every time you open a new window. (If this gets frustrating, see if you can figure out [autoenv](https://github.com/kennethreitz/autoenv).)

Finish up your playlist tracks method and endpoint.

### On Heroku

Heroku has support for this, too!

```
heroku config:set SPOTIFY_TOKEN='YOUR_TOKEN_ONCE_MORE'
```

This will do the exact same thing as 'export' locally.

To see everything you've set:

```
heroku config
```

## Running a Timed Script

We're going to learn how to automatically run code on Heroku!

Create a new file, `scheduled.py` that does something when run. Perhaps you can get it to send you a SMS or email with a random playlist or track? (Or just a static message).

The [Heroku Scheduler](https://addons.heroku.com/scheduler) addon allows us to run a file from our project at a regular, specified interval.

You can add it via the web, or from the command line:

```
heroku addons:create scheduler
```

The [Scheduler dashboard](https://scheduler.heroku.com/dashboard) lets you specify the file to run and when to run it. To get to the right dashboard from your app, do `heroku addons:open scheduler` from your app directory, or click through from your app's page in the Heroku dashboard.

Add your new job (with `python` in front, e.g. `python scheduled.py`) and set a time for it. That's all it takes!

# Adding a Database

Let's combine the scheduler and playlists to make a new feature that emails someone daily with a playlist suggestion. 

You don't need to set up a whole user system -- make a form that allows the user to "subscribe" to a playlist search by entering their email address, and create a database model to save the search term and email together using SQLite (we'll move to a better database after this).

Once you have saved people's email preferences, create the other half of the app. This will be a standalone script that:

* Gets all the email/search combinations from the database
* For each combo, get the first 10 playlists for that search term
* Pick a random playlist
* Email the user (using Mailgun) suggesting "You should listen to:" and linking to the Spotify URI for that playlist.

We'll set this script to run every day. You can probably think of improvements to this -- please implement them!

How can you stop the app from emailing the same person multiple emails? 

Can you keep track of playlists that have already been sent? 

How can you use the API to make sure there are a certain number of tracks in the playlist?

Can you change the database model to allow 'unsubscribe'?