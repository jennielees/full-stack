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
   # and False if there was an exception
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

We'll discuss in class (see _Week 5_) how we could set this to automatically run, making it a 'real' app! We'll also talk about design considerations when making this into an app.