---
layout: post
title: Frontend, Backend, Middleware
week: 4
permalink: front-back-middle/
---

> "Will you walk a little faster?" said a whiting to a snail,

> "There's a porpoise close behind us, and he's treading on my tail.

> See how eagerly the lobsters and the turtles all advance!

> They are waiting on the shingle – will you come and join the dance?

### How Servers, and the Web, Work

We'll go through this in class. If you miss class or want more resources, try these:

* [Frontend vs Backend - Treehouse](http://blog.teamtreehouse.com/i-dont-speak-your-language-frontend-vs-backend)
* [Frontend vs Backend - Skillcrush](http://skillcrush.com/2012/04/17/frontend-vs-backend-3/)
* [Databases - Skillcrush](http://skillcrush.com/2012/04/06/databases/)

You should have answers to the following questions:

* What is the back-end?
* What languages are often used on the back-end?
* What is the front-end?
* What languages are often used on the front-end?
* What does 'full-stack' mean?
* What is a database? Is it part of the front or back end?


### What is an API?

Also see class, but if you miss it, look at these:

* [Google for Entrepreneurs Introduction to APIs](https://www.youtube.com/watch?v=FknvOGcLHmc)
* [HTTP part 1](http://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-1--net-31177)
* [HTTP part 2](http://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-2--net-31155)
* [JSON](http://www.copterlabs.com/blog/json-what-it-is-how-it-works-how-to-use-it/)

Questions:

* What is HTTP?
* What does REST mean?
* What is the HTTP status code?
* What are headers?
* What is an API key? Why do you need one? Why might you not need one?
* What is JSON?

A lot of this will make much more sense when you start actually using APIs, so let's get started!

### Making our first API requests

We can use the [requests](http://docs.python-requests.org/en/latest/user/quickstart/) library in Python to call an API.

To install it, go to Terminal and type

```
$ pip install requests
```

This will use "pip", the Python Package Installer, to get all the code necessary to use `requests`. We'll discuss this in class in more detail later; for now, let's move on with the API!

Sign up at [Weather Underground](http://www.wunderground.com/weather/api/d/login.html).

Get your API key. This is a unique key for your account.

The weather API URL for a city looks like this:

```
http://api.wunderground.com/api/YOUR_API_KEY_GOES_HERE/conditions/q/CA/San_Francisco.json
```

Put your API key in the appropriate spot and then use Terminal to get the data from the API.

```
$ curl http://api.wunderground.com/api/YOUR_API_KEY_GOES_HERE/conditions/q/CA/San_Francisco.json
```

This will print the result out in Terminal.

How do we access this in Python? It's a parallel to how we worked with files earlier. We use the **requests** library, so we need to `import` it.


```
import requests

r = requests.get('http://api.wunderground.com/api/YOUR_API_KEY_GOES_HERE/conditions/q/CA/San_Francisco.json')
```

Can you print out `r.status_code` and `r.json()`?

To access a part of the response, we use the `json()` method to convert the JSON into a Python dictionary, then we access the dictionary.

It's often helpful to look at the [API documentation](http://www.wunderground.com/weather/api/d/docs?d=data/conditions) and, if possible, access the API directly using `curl` or a browser -- so we know which fields we want to get out.

When we do this for this example, we can see there are a whole bunch of fields that we probably don't care much about, but there is one interesting-looking one: `temperature_string`. We can also see this is nested inside `current_conditions`.

```
j = r.json()

temperature = j['current_conditions']['temperature_string']
print temperature
```

Write a function that returns this temperature string.

```
def weather():
   # ...
   return temperature
```

Extend it to take the city state and name as parameters. 

```
def weather(state, city):
   # ...
   return temperature
```

You will need to do some string formatting to get the URL correct for the API, including replacing spaces with underscores.


<pre class="hint">
BASE_URL = 'http://api.wunderground.com/api/YOUR_API_KEY_GOES_HERE/conditions/q/'

def get_api_url(state, city):
    city = city.replace(" ", "_")
    return "{}/{}/{}".format(BASE_URL, state, city)
    
# test
print get_api_url("CA", "San Francisco")
print get_api_url("NY", "New York")
</pre>

Write an app that takes some kind of input for city name and state, and prints out the current temperature. If the city name/state doesn't work, handle it gracefully. (What kind of errors can you cause? How can you break the API call?)

Look at the [API docs for forecast](http://www.wunderground.com/weather/api/d/docs?d=data/forecast). (Hint: there's an example at the bottom of the page!)

Note: You can also experiment using the [API Console](http://www.wunderground.com/weather/api/d/docs?d=resources/apigee-console) for Weather Underground.

Can you create a second function `forecast()` that prints out the forecast for San Francisco? Can you make it do the same for any city?

<pre class="hint">
# The easiest way is to iterate through the forecastday array.

j = r.json()
days = j['forecast']['txt_forecast']['forecastday']

for day in days:
    print day['title'], day['fcttext_metric']
    
# Is this what you want to print out? Are there other pieces of data you could print instead?
</pre>