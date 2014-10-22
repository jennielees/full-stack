---
layout: post
title: A RESTful Interlude
week: 5
---

### APIs, Continued...

This week we're going to continue poking around with APIs and build our own API-powered app!

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

* Sign up for a Twitter account if you need to
* [Sign up for an application](https://apps.twitter.com/) on Twitter
* Get the consumer key and secret 
* Edit `twitter_oauth.py` to have your credentials
* Authorize it by visiting the link it prints out in a browser and pasting the code back in

#### Take it further

Using Twitter's developer documentation as reference, try these:

* Print the author and text of the recent tweets on your timeline (start from what's already in `twitter_oauth.py`)
* Similar, but for [your @mentions](https://dev.twitter.com/rest/reference/get/statuses/mentions_timeline)
* Pick a [user](https://dev.twitter.com/rest/reference/get/statuses/user_timeline) and print out their 10 most recent tweets 
* Use the [Search API](https://dev.twitter.com/rest/reference/get/search/tweets) to get all recent tweets mentioning Hackbright

Tip: if you need to print a JSON response to look at it more closely, and it's coming out all squashed, you can use the `pprint` utility to pretty-print:

```
from pprint import pprint

pprint(json_response)
```

### Not just GET, but POST

To build an app, we probably want some kind of input and some kind of output.

How might you chain your Twitter code above with previous work, so that if someone @mentions you with the phrase "What's the weather?", you can tweet back at them?

We need to do three things:

* To check for tweets with the question
* To pass some input into a function that can check the weather
* To tweet the response back!

#### Tweetin', tweetin'

To send a tweet, you need to `POST` to `statuses/update.json`. And have permission to post. You might want to create a new Twitter account for this kind of thing, otherwise your normal account could get a bit... messy. But you don't need to create a new app.

<pre class="hint">
TWEET_URL = API_URL + "/1.1/statuses/update.json"

data = { 'status': STATUS_GOES_HERE }
response = requests.post(TWEET_URL, data=data, auth=auth)
</pre>

Sweet! Now we can tweet!

Turn this into a function called `make_tweet(status_message, auth)`.

**If it doesn't work**: 

* Check if your Twitter app has permission to actually post tweets. Go to [apps.twitter.com](http://apps.twitter.com) and go to the 'Permissions' tab for your app. Make sure [Read and Write](/public/twitter_perms.png) is set.
* Check you authorized the app you are using, if you switched accounts:
 
  You do **not** need to create a new app - you can use the same app (and therefore the same `CLIENT_KEY` and `CLIENT_SECRET` as before). But you **do** need to generate a new authorization for the new user by generating a new `access.json` file:

    ```
$ mv access.json access_oldaccount.json
$ python twitter_oauth.py
    ```
* Try `print` on the `response.json()` to see what Twitter actually says, and google the error! :)

#### Connecting it up

##### Check for tweets

Create a function called `get_weather_mentions` that checks your @mentions for the phrase 'What's the weather?' and returns all the users who asked. Why not make it a general function that can check for _any_ phrase?

Note that we are using the `json()` method on the response - all it does is turn API responses (which are in [JSON](http://json.org/) format) into Python dictionaries.

<pre class="hint">
# .. at the bottom of your twitter_oauth.py file ..

# Check if a phrase is contained in another phrase
def phrase_contains(to_check, target):
    if target.lower() in to_check.lower():
        return True
    else:
        return False

def get_phrase_mentions(mentions, phrase):
""" Return a list of the users who match a phrase.
"""
    matching_users = []
    for mention in mentions:
	    text = mention['text']
	    user = mention['user']
	    # TODO:
	    # check if phrase is contained in text
	    # if so, add this user to matching_users
	    # and maybe print something 
	    # if not, do nothing
	return matching_users 
	
def get_weather_mentions(mentions):
    return get_phrase_mentions(mentions, "What's the weather?")

def main():
    response = requests.get(MENTIONS_URL, auth=auth)
    mentions = response.json()

    matching_users = get_weather_mentions(mentions)
    
if __name__=="__main__":
    main()

</pre>

##### To test or not to test

In order to test your code, make sure someone has tweeted "What's the weather?" at your account! If you are having trouble ask the instructor/TA to tweet or to give you the password to a test account.

What happens if there are no matching tweets?

##### Getting the location

To reply to this user, you probably want to find out where they are so you can answer their question with a personal touch.

You'll need a function `get_user_location(user)` that can take one of the user dictionaries and return a plain location. Remember to `print` or `pprint` things if you want to quickly see their structure!

<pre class="hint">
def get_user_location(user):
    # from pprint import pprint
    # pprint(user)
    return user['location']
</pre>

##### Querying the weather

Remember all that weather stuff we did? Let's bring it back!

If you don't have your code handy, [use this](https://gist.github.com/jennielees/2be3a1611a4b95aeaacd) - or take a look to compare.

Make sure you have a function that can `return` a nice sentence to tweet back.

Our weather API call needs a city and state, so let's use `split()` to separate out our locations! We can pass `, ` into `split` to separate based on commas.

<pre class="hint">
def get_city_and_state(location):
    l = location.split(", ")
    if len(l) > 1:
        return (l[0], l[1])
    else:
        return (l[0], '')

# Try pasting this into the Python console to figure out what it does.
print get_city_and_state("San Francisco, CA")
print get_city_and_state("New York, NY")
print get_city_and_state("Brighton, England")
print get_city_and_state("San Francisco")
print get_city_and_state("Your mom's house")
</pre>

Now, a harsh truth. **Real world data sucks**. Twitter users have all kinds of locations like 'The Moon', 'Behind you!' or even just plain old cities without states ('San Francisco'). This is great for humans but not so great for the Weather API.

Let's use our `get_city_and_state` function to try and get a sensible input:

```
# inside your main() function:
for user in matching_users:
    location = get_user_location(user)
    (city, state) = get_city_and_state(location)
    sentence = get_weather_sentence(city, state)
```

You might get a `KeyError: 'current_observation'` when you run this. That's ok. Python is looking for `current_observation` but the Weather API isn't giving it to you, probably because the location wasn't useful enough.

We can add two checks to make sure our code doesn't fall over horribly here. We know it will fail if `state` is empty, and we can look for an exception with `try`.

```
# inside your main() function:
for user in matching_users:
    location = get_user_location(user)
    (city, state) = get_city_and_state(location)
    if state == '':
        print "This user doesn't have a good location: {}".format(location)
	else:
		try:
	        sentence = get_weather_sentence(state, city)
	    except:
	        print "Couldn't query for this location: {}".format(location)
	
	# let's check if our sentence was created or not
	if not sentence:
	    # choose what to do: print a message, do nothing, or try again
	    # with a default location
	else:
	    tweet_reply(sentence, user, auth)
```

##### Tweetin' it back

Now fill out the `tweet_reply` function. We have the basics already in `make_tweet`, but you also want to pull out the username to send the tweet! Posting a tweet needs authorization, so you'll want to pass that along.

<pre class="hint">
def make_tweet(status_message, auth):
    data = { 'status': status_message }
    response = requests.post(TWEET_URL, data=data, auth=auth)
#    print json.dumps(response.json(), indent=4)

def tweet_reply(message, user, auth):
    username = user['screen_name']
    reply_message = "@{} You ask, I answer! {}".format(username, message)
    make_tweet(reply_message, auth)
</pre>

Phew!

Test it out, and commit your code to GitHub!
