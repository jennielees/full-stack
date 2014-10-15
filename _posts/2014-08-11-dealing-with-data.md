---
layout: post
title: Dealing with Data
week: 4
---

### Connecting the Dots

So far we've written several isolated functions that do cool things. Now we're going to take a look at putting them together.

Create a new function that generates random (real) place names using `random.choice`. You can start with a list, for example:

```
source_places = [ ('New York', 'NY'), ('San Francisco', 'CA'), ('Seattle', 'WA'), ('Houston', 'TX') ]
```

Notice how each of the elements in this list looks a bit funky? This is a [tuple](http://openbookproject.net/thinkcs/python/english3e/tuples.html). A tuple is just a fixed, comma-separated list of values. You can access elements in a tuple like you can a list:

```
ny = source_places[0]
print ny[0]
print ny[1]
```

However, you can't assign new values to them.

```
ny[0] = "New New York"
```

So, first of all, you need to create a function that has a _signature_ like this:

```
(city, state) = get_random_place_name()
```

Having a tuple on the left here is perfectly valid and makes life a lot easier!

Now, once you have that function, chain it together with the weather (or forecast) function we wrote in the previous exercise.

```
(city, state) = get_random_place_name()
the_weather = weather(city, state)
print the_weather
```

We assign the output of our first function to the variables `city` and `state`, then use those variables in the next function.

How does this relate to back-end development?

Most back-end development involves chaining together functions like this!

This is where **testing** our code becomes really important. If we break down our code into small, one-job functions, we can test each function individually, so when we put them all together we know that it works.

### Text me, maybe?

Let's play with another API and chain things together!

The [Twilio](http://www.twilio.com/docs/api/rest/sending-messages) API lets you send and receive calls and SMS messages.

Sign up for [Twilio](https://www.twilio.com/try-twilio).

Load up the [SMS Quickstart](https://www.twilio.com/docs/quickstart/python/sms/sending-via-rest) documentation.

You'll note it says that with trial accounts, you can only send SMS messages to verified numbers. Go to your [account page](https://www.twilio.com/user/account/phone-numbers/incoming) and verify your phone number so you can test. They will call or text you with a verification code.

While you are there, set up your trial Twilio number and note down where your credentials are ([Account SID and Auth Token](https://www.twilio.com/user/account)). You'll need them in a minute.

Work through the Quickstart. To get the Twilio library, use `pip` again:

```
$ pip install twilio
```

Following the Quickstart, create `send_sms.py` and replace the credentials and numbers with your own. Don't forget to keep the `+1` in front of the phone numbers, e.g `+14155551234`

Run `send_sms.py` - you should receive a SMS! It's that simple. (Don't worry about the MMS part of the Quickstart.)

What happens if you put the phone number in differently? Try variants like:

* 4155551234
* (415) 555-1234
* +1 (415) 555.1234
* 415 555 1234

(if you pay by the message to receive texts, you can test this out by setting up a free Google Voice account and disabling text forwarding to your phone; there are probably other ways to do this too.)

What happens if you put a number in that you didn't verify?

### gr8 fun(ctions)

Turn the contents of `send_sms.py` into a function.

Expand the function to take a message and a phone number, so it looks something like this:

```
def text_this(number, message):
   # ... sends a message to the number supplied
   # returns True if the message sent OK
   # and False if the message failed for some reason
```

Right now, this function should return False if you use any number you didn't verify.

#### For Testing Only

You don't want to spam up your inbox when testing, so one thing worth doing here is creating a **test mode**.

Add a new optional parameter to `text_this` called `test`, default to `False`. If it is set to `True`, print out a message instead of sending the SMS.

<pre class="hint">
def text_this(number, message, test=False):
    if test:
        print "This would have sent a SMS to {}. Message: {}".format(number, message)
        return True
    # ... send SMS code here...
</pre>

#### Chaining 

Now let's put this together with our weather function.

Instead of printing out the weather, text it.

<pre class="hint">
(city, state) = get_random_place_name()
the_weather = weather(city, state)

message = "The weather in {}, {} is {}".format(city, state, the_weather)
my_phone_number = "415 555 1234"
test_mode = True # Change this to False to send a SMS!

success = text_this(my_phone_number, message, test_mode)
</pre>

We can keep passing data around like this and building on it.

However, an app that texts a random place's weather isn't that useful. Go back to the weather exercise from the previous page and pick something more interesting, such as tomorrow morning's forecast -- make a mini app that texts this.

We'll discuss in class how we could set this to automatically run, making it a 'real' app! We'll also talk about design considerations when making this into an app.

### Twitter for Fun and Profit

Twitter and SMS apps have a lot in common - there's an input and an output, at least. However, Twitter's API is a little more complex to work with thanks to something called OAuth.

OAuth is an authentication handshake that stops you having to give your username and password to apps, and allows developers to only ask for the permissions they need. You use it when signing into an app with Facebook, for example.

* [OAuth Explained](http://blog.varonis.com/introduction-to-oauth/)
* [More on OAuth](http://aaronparecki.com/articles/2012/07/29/1/oauth2-simplified)

As a developer, you usually follow the same dance with every OAuth-enabled app. You have some basic credentials, often called the Client ID and Client Secret, but also known as the Consumer Key and Consumer Secret. From these keys, a unique code is generated. 

Your user visits the provider's site with that code and sees a "Do you want to grant permission?" dialog. When saying yes, the user is usually redirected back to your app with a new code. You then exchange that code, with the keys that only you know, for an access token. With that token, you can make API calls on behalf of the user.

Implementing all that is a bit of a headache and fortunately done so often that there are plenty of pieces of code around to do it for you.

[Here's one.](/public/data/twitter_oauth.py)

If you run this code (read it first!), you'll be given a URL to visit. Paste that into your browser to get a code; paste the code back into Python, and your credentials are stored.

You can see in the `main()` function in that file how to call the Twitter API itself. It's just like our previous API requests using, yup, `requests.get`.

#### Get it working

* [Sign up for an application](https://apps.twitter.com/) on Twitter
* Get the consumer key and secret 
* Edit `twitter_oauth.py` to have your credentials
* Authorize it by visiting the link it prints out in a browser and pasting the code back in

#### Take it further

Using Twitter's developer documentation as reference:

* Print the author and text of the recent tweets on your timeline (start from what's already in `twitter_oauth.py`)
* Similar, but for [your @mentions](https://dev.twitter.com/rest/reference/get/statuses/mentions_timeline)
* Pick a [user](https://dev.twitter.com/rest/reference/get/statuses/user_timeline) and print out their 10 most recent tweets 
* Use the [Search API](https://dev.twitter.com/rest/reference/get/search/tweets) to get all recent tweets mentioning Hackbright

Tip: if you need to print a JSON response to look at it more closely, and it's coming out all squashed, you can use the `pprint` utility to pretty-print:

```
from pprint import pprint

pprint(json_response)
```

Look at the mentions timeline again.

Can you pull out the `location` field for a tweet author? It's under `user` and then `location`.

How might you chain this with previous work, so that if someone @mentions you with the phrase "What's the weather?", you can tweet back at them?

To send a tweet, you need to `POST` to `statuses/update.json`. And have permission to post. You might want to create a new Twitter account for this kind of thing.

<pre class="hint">
TWEET_URL = API_URL + "/1.1/statuses/update.json"

data = { 'status': STATUS_GOES_HERE }
response = requests.post(TWEET_URL, data=data, auth=auth)
</pre>

Sweet! Now we can tweet! That was a lot - pat yourself on the back for getting through it. :-)