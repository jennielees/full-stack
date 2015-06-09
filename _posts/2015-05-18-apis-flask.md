---
layout: post
title: APIs and Flask
week: 6
---

## What is an API?

We're going to learn what an API is and how to send email using one. To start, we'll actually use our own API!

First, we'll familiarise ourselves with [JSON](http://www.copterlabs.com/blog/json-what-it-is-how-it-works-how-to-use-it/). This [Chrome extension](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?hl=en) makes it easy to look at JSON inside your web browser, and [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) is a great Chrome app that makes testing APIs easy. If you aren't using Mac OS, I recommend installing both (or Firefox equivalents).

[Here is the source code](https://gist.github.com/jennielees/cebac0ac3f11c3c85040) to a really simple API. Grab it, and run it locally:

```
python static_api.py
```

Now, let's interact with the API. It should be running on [http://localhost:5000](http://localhost:5000), so visit that in a web browser.

Compare what you see to the source code.

Neat, huh? Instead of serving up a HTML page, we're exposing the data directly as JSON using Flask's `jsonify` method.

### Accessing via other means

As our API usage gets more complex, just visiting in a web browser won't be enough. If you installed Postman, try using it to make a `GET` request to `http://localhost:5000/` and see what shows up.

You can also use `curl`, a command-line Linux tool which is handy for fetching URLs and especially handy for APIs. Try it:

```
curl http://localhost:5000/
```

What do you get? Note: by default, `curl` prints everything out rather than saving it.

## What can we do with APIs?

Most modern web services (Twitter, Facebook, Google, etc) have APIs -- sometimes several! They expose a computer-friendly way to use the service. There are also companies offering APIs for everything from sending mail and SMSes to checking sports scores and weather information.

Let's start with one of them - [Weather Underground](http://wunderground.com).

In order to access most commercial APIs, we need to have some kind of authentication. This is often via an "API Key", a unique string that is tied to your account with the service.

Try signing up for your own API key at Weather Underground.

The weather URL for a specific city looks like this:

```
http://api.wunderground.com/api/YOUR_API_KEY_GOES_HERE/conditions/q/CA/San_Francisco.json
```

Put your API key in the appropriate spot and then use Terminal to get the data from the API. I've put my API key in the following URL as an example, but use your own -- otherwise my account might get locked!

```
curl http://api.wunderground.com/api/9286261a1046d6b5/conditions/q/CA/San_Francisco.json
```

This URL results in a bunch of JSON. Eek. This is something that is easier to look at in Chrome, so try the same URL in a browser or Postman. Again, it's a `GET` request.

# API-speak in Python

Seeing the data is all very well, but how do we access it in Python?

The `requests` library lets us GET and POST data wherever we like, using `requests.get` and `requests.post` (and so on). Inside your virtualenv, `pip install requests`.

Now let's try it in Python:

```
python
>>> import requests
>>> result = requests.get('http://api.wunderground.com/api/9286261a1046d6b5/conditions/q/CA/San_Francisco.json')
>>> print result.json()
```

Calling `.json()` on the result from a request turns the data into a Python dictionary that we can move around:

```
>>> weather = result.json()
>>> weather.keys()
[u'current_observation', u'response']
```

### A side note on Unicode

Unicode is an extended character set that allows Python to deal with characters with accents and other extensions to the basic, English-friendly alphabet. [This page](https://docs.python.org/2/howto/unicode.html) contains more than you ever need or want to know on the subject.

In Python, we've seen `str` to represent a string. Actually, there is another kind of string too, `unicode` -- which represents a string that uses this extended character set. When we print unicode strings inside Python, they look like the ones above: `u'something'`. However, that is mostly for debugging purposes - they look and behave like standard strings pretty much everywhere else.

When we deal with APIs and the `json()` function, because of the sheer amount of potential data an API can contain, you'll almost always see `unicode` instead of `str` strings.

### And Now, The Weather

Using our Python dictionary skillz, we can navigate through the JSON object to find the current temperature in San Francisco.

```
>>> weather['current_observation']['temp_f']
79.4
```

See if you can get Python to print out the following, too:

* The string description of the current temperature - `Something F (Something C)`
* The string description of the current weather - `Partly Cloudy`
* Whether it is raining or not

Now, look at the [API documentation](http://www.wunderground.com/weather/api/d/docs?d=data/forecast) for Weather Underground.

Change the URL you are requesting to get the 3-day forecast (you will need to do `requests.get` again on the new URL), and get Python to figure out if it will rain in the next three days.

# Your own API

That's pretty much how interacting with APIs goes. You can also use `POST` to make a request that sends data, which we'll see shortly to send "forgot password" emails.

Creating your own API is as simple as the code example at the start of this lab. Simply import `jsonify` from Python, and return a dictionary wrapped inside `jsonify` instead of a `render_template` HTML page.

Copy the code you have to print out the list of desserts and create a new route that returns the list of all desserts (not specific to a user) as JSON.

How can you test that this is working?

Why don't we restrict it to a single user? Can you walk through what that would entail and spot any problems?