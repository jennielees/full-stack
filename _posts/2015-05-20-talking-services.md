---
layout: post
title: Talking to Services
week: 7
---

If you didn't run through the [APIs and Flask](/full-stack/apis-flask) section from last week, please start off by doing so. You should have connected to Weather Underground and got the weather report via API.

We're going to stick with the weather for a bit more, and then integrate it with a couple of other APIs.

## Create a weather function

In a new, standalone Python file (eg. `weather.py`) create a new function. We are going to hook this up to different services, so let's make it a pretty general function that makes a request to the Weather Underground API and gets the current temperature for that city and state. (If the city and state are invalid, Weather Underground guesses the next-best thing, so your API requests will always work. For cities outside the U.S., country works instead of state.)

```
def weather(city, state):
    # ...
    return temperature
```

We saw that the format of the Weather Underground API URL includes the city and state, so you'll have to construct your own URL from the inputs provided. The default looks like this:

```
http://api.wunderground.com/api/YOUR_API_KEY/conditions/q/CA/San_Francisco.json
```

* Construct the right URL
* Make a `requests.get` request to it
* Convert the result into a Python dictionary using `.json()`
* Extract the current temperature
* Return it

## Doing more

The first thing we can do with this is create a Flask app around it, so we could host a simple site that just told you the weather. While this sounds a bit trivial, some people have done just that.

We're going to do a bit more, though.

### Enter Twilio

One API that's super fun is [Twilio](http://twilio.com), which allows you to send and receive text messages.

[Sign up](https://www.twilio.com/try-twilio) and check out the [SMS Quickstart](https://www.twilio.com/docs/quickstart/python/sms/sending-via-rest).

You'll note it says that with trial accounts, you can only send SMS messages to verified numbers. Go to your [account page](https://www.twilio.com/user/account/phone-numbers/incoming) and verify your phone number so you can test. They will call or text you with a verification code.

While you are there, set up your trial Twilio number and note down where your credentials are by hitting ["Show Account Credentials"](https://www.twilio.com/user/account/voice-sms-mms). Get your Account SID and Auth Token. You'll need them in a minute.

Twilio has a python library, but you can also use `requests` to send SMS. All you have to do is make an authenticated POST request.

```
import requests

acc_id = "YOUR_ACCOUNT_ID"
auth = "YOUR_ACCOUNT_AUTH"

url = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json".format(acc_id)

message = {
    'Body': "This is a python sms!",
    'To': "ANY_NUMBER",
    'From': "YOUR_TWILIO_NUMBER"
}
    
r = requests.post(url, auth=(acc_id, auth), data=message)
print r.json()
```

Replace the appropriate pieces of the above code and see if you can get it to send you a SMS!

Wrap this up in a function:

```
def send_sms(number, message):
    # sends a SMS with body 'message' to 'number'
```

Now see if you can chain the two API calls together:

```
sf_weather = weather('San Francisco', 'CA')
weather_message = 'The weather in San Francisco is {}'.format(sf_weather)
send_sms('YOUR_NUMBER', weather_message)
```

Getting a bit more useful. As you can hopefully imagine, we could combine this functionality this with things like the future weather forecast to potentially warn of rain before your commute home, or alert you before you travel.

Let's try sending email as well as SMS. This is a really useful thing to be able to do when you're building a web app, from "forgot password" emails to more engagement-focused campaigns.

## Enter Mailgun

[Sign up](https://mailgun.com/signup) for Mailgun. While many servers can send email directly using programs on the server itself, these can be painful to use and unreliable; using a cloud API is a lot easier these days.

Once you've finished signup, Mailgun should show you a sandbox. Click on 'Python' and copy the code sample into a file. It should start with `def send_simple_message()`.

Run the function. Yep, that's it. You can now send email. Of course, you might want to change the data in the email some day. :)

Don't worry about adding your own domain (yet), for development purposes we are all set. With this kind of account, you can change the "name" on your From: address, but not the email (it has to be the @mailgun.org address).


## And Flask?

Flask is great for combining functionality from different APIs and data sources (including its own database) and packaging it up into a neat web app.

We're going to put together some of the stuff we've done so far into a small travel app.

Pick a few of your favorite cities and make a Flask app with two routes:

```
/                --> should return a page with some city names
/city/<state>/<city>  --> should return a page for that individual city
```

How can we hook these up? Well, we can create some links that pre-fill in the right format.

```
<a href="/city/CA/San Francisco">San Francisco, CA</a>
<a href="/city/UK/London">London, UK</a>
```

Your individual city route can work with the usual decorator:

```
@app.route('/city/<state>/<city>')
def get_city(state, city):
   # .. do stuff with state and city
   return render_template('city.html', ...)
```

So, what's that "stuff"?

First, use the weather function we wrote to go fetch the weather for that city, and pass that through into our template.

Once you've got that working, how about adding some pictures?

### Insta-Awesome

Where can we find pictures? Let's try [Instagram](http://instagram.com)!

You can sign up for your own developer account on Instagram, or use my client ID (click in the next section to reveal).

<pre class="hint">
INSTA_CLIENT_ID = 4284d7cbe97f482cacb55e48cd6ec745
</pre>

To search Instagram by location, we need to convert a place into latitude and longitude. Fortunately, we don't need to learn a new API to do that - Weather Underground actually provides this information for us!

We need to change up our `get_weather` a bit so we don't end up calling the same API twice. See if you can figure out a way to change things so you can get the latitude, longitude and temperature back -- there are a couple of options!

Now you have the latitude and longitude, use this [Instagram API](https://instagram.com/developer/endpoints/media/) documentation page to write a method that takes the lat and long and returns a list of photos. **Note on Auth:** Use `client_id=INSTA_CLIENT_ID` (your Instagram client ID) instead of the `access_token=ACCESS-TOKEN` -- you do **not** need to use OAuth or otherwise authenticate to get public data. (We'll cover OAuth next week.)

Hit the "Response" dropdown on the documentation page to get an easy preview of the data the API gives you.

You can convert the list of photos (as JSON response) into something more lightweight, maybe starting with a list that just contains the URLs to the photo image. Alternatively, you can pass the whole thing into your template and make the template do the work.

### More of an App

Add two links to your individual city page: "Text Me This" and "Email Me This".

Create two new routes that both look something like:

```
from Flask import url_for, redirect

@app.route(/text/<state>/<city>)
def text_me(state, city):
    # .. send a text message with the state and city in
    return redirect(url_for('get_city', state=state, city=city))
```

`url_for()` is a [more robust way](http://flask.pocoo.org/docs/0.10/quickstart/#url-building) of hand-writing the URL for a specific route.

Although you have a bunch of stuff pretty hard-coded, like the "to" email and SMS number, this is already getting dynamic!

### Work It

If you have a bit of time left, you can spend it doing any of these:

* Make the app look less crappy than the default layout
* Figure out how to load multiple pages of photos from Instagram
* See if you can get the visitor (we're not doing a full user system) to give you their phone number or email so you don't always just send to yourself
* See if you can integrate more APIs or functionality into your city page. Note that many APIs might not be available or might require approval to use.

All optional!