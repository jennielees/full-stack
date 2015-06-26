---
layout: post
title: Best Practices
week: 8
---

# Authentication

Let's implement OAuth!

We're going to do this in a standalone app for simplicity, but pay attention -- your next task will be to implement this in your Spotify app.

Get [the code here](https://gist.github.com/jennielees/805e93a91b16df14cc63).

Run `app.py` and visit it in a browser -- what happens? Watch the URL bar.

What about if you try to visit the site again ([http://localhost:8080/](http://localhost:8080/))? Do you see the consent screen again or does Google wave you through?

Can you trigger an auth error? What happens?

Could you store the access token somewhere (maybe the session?) to save all the redirecting?

I've set up a Google developer console project and included the secrets in that file, but if you want to set up your own, sign in at [https://console.developers.google.com/](https://console.developers.google.com/).

You will need to go to "APIs & auth > Credentials" and "Create new Client ID" for a Web Application. Make sure you enter your app's callback URL under "Redirect URIs" -- in the case of the sample code, it's `http://localhost:8080/oauth2callback`.


## Adding Spotify OAuth

Spotify also requires OAuth and has an [authorization guide](https://developer.spotify.com/web-api/authorization-guide/) you can check out.

[Register a developer application](https://developer.spotify.com/my-applications/), if you haven't already (you will need a Spotify account - if this is a problem, we can give you developer credentials to use).

You need to implement the authorization code flow detailed in the guide.

Based on the Google code and the documentation, can you build this into your music app? The flow is exactly the same:

* Present the user with a button to click to sign in (we skipped this step in the Google code)
* Redirect the user to the authorization URL, providing your client ID and redirect URL
* Spotify redirects the user back to your application
* You get the code they supplied with the redirect, and POST it back to Spotify to ask for the token
* Get the access token and use it to request the Spotify API endpoints, storing it in the session for reuse (you could also create a user account at this point)

There is an extra layer of fun here -- the `refresh_token`. This allows you to request another access token without the user needing to click anything, because the access tokens expire.

How can you tell if a token has expired? Usually by a failed API request:

```
import requests
# Let's make an unauthorized call to the API
r = requests.get('https://api.spotify.com/v1/users/ainfigree/playlists')
print r.status_code
```

The code `401` means "Unauthorized". We can add an `if` statement and request a new token if we get this -- see step 7 of the Spotify Authorization Guide.

Implement a Spotify login button and get rid of the horribly insecure access token stuff we had before.

Use the `https://api.spotify.com/v1/me` endpoint to retrieve the user's name.

# Moving off SQLite

We've been promising to use non-SQLite databases for a while now, so let's do it. We're going to use PostgreSQL, which is easily available on Heroku and also a relational database (so the code is almost identical).

Let's continue with the Spotify app.

Make sure you got the user's username (Spotify ID) and stored it in the session.

```
token = session.get('access_token')  # assuming that's where you put it
headers = { 'Authorization': 'Bearer {}'.format(token) }
r = requests.post('https://api.spotify.com/v1/me')
session['spotify_id'] = r.json().get('id')
```

We're going to create a SQLAlchemy model to 'heart' playlists. When a user hearts a playlist we will store it in the database.

Create a `models.py` file:

```
from app import db

class MusicHeart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spotify_id = db.Column(db.String(100))
    playlist_id = db.Column(db.String(100))

if __name__ == "__main__":
    print "Creating database tables..."
    db.create_all()
    print "Done!"
```

Now let's add the `db` to `app.py`, this time looking a bit different...

```
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/music'
db = SQLAlchemy(app)
```

Make sure to `pip install flask-sqlalchemy` in your virtualenv. You also need to `pip install psycopg2` for Postgres support.

Let's actually get the database created, too. Install [Postgres.app](http://postgresapp.com/) on Mac; on Windows, you can use the [graphical installer](http://www.postgresql.org/download/windows/) and on Ubuntu, `apt-get install postgresql` should work.

In a terminal, type `psql`.

```
$ psql
psql (9.3.5)
Type "help" for help.

=# create database music;
```

Now we've created our database, run `models.py` and the tables should get created. We can check in Postgres with the `\dt` command:

```
$ psql music
=# \dt
           List of relations
 Schema |     Name     | Type  | Owner
--------+--------------+-------+--------
 public | music_heart | table | you
```

We can also use `\d` to look at a table's schema:
```
$ psql music
=# \d music_heart
                                   Table "public.music_heart"
   Column    |          Type          |                         Modifiers
-------------+------------------------+-----------------------------------------------------------
 id          | integer                | not null default nextval('music_heart_id_seq'::regclass)
 spotify_id  | character varying(100) |
 playlist_id | character varying(100) |
Indexes:
    "music_heart_pkey" PRIMARY KEY, btree (id)
```

If you prefer visual interfaces, try [Postico](https://eggerapps.at/postico/) (Mac only).

## Creating some Data

Create an endpoint to associate a playlist ID with a spotify ID.

```
@app.route(/heart/<playlist_id>)
def heart(playlist_id):
    spotify_id = session.get('spotify_id')
    new_heart = MusicHeart(spotify_id=spotify_id, playlist_id=playlist_id)
    db.session.add(new_heart)
    db.session.commit()
    return 'success'
```

Feel free to add validation and other checks to this endpoint.

Integrate this with your app using jQuery if possible.

Test it out by associating some things and checking what's in the database! (`SELECT * FROM...` is all the same in Postgres.)

## Databases and Heroku

One of the reasons we're doing all this is because using PostgreSQL on Heroku only requires a few small changes.

First, enable the PostgreSQL addon. This level is free but does have size and speed limitations ([more details](https://elements.heroku.com/addons/heroku-postgresql)).

```
heroku addons:create heroku-postgresql:hobby-dev
```

When you've done this you should notice that it sets a variable on Heroku called `DATABASE_URL`. Check with `heroku config`.

All you need to do to get Heroku Postgres working instead of local Postgres is to change the app database URL:

```
import os
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://localhost/music')
```

The second argument in `get` is the default if the setting is missing, meaning it will still use your local database on your local machine.

Don't forget to update your `pip freeze > requirements.txt` to reflect the new requirements, then deploy the new code!

How do you run `models.py` on Heroku?

```
heroku run python models.py
```

Not so tricky. Test and see if this works!

To look inside the remote database, Heroku has a handy shortcut:

```
heroku pg:psql
---> Connecting to DATABASE_URL
::DATABASE=> \dt
```

Bonus: See if you can use the [Flask Heroku](https://github.com/kennethreitz/flask-heroku/) extension to simplify this! Peek inside the code to see what it does.
