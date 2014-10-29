---
layout: post
title: Fun and Functionality
week: 6
---

### In the Belly of the Beast

When enmeshed in the depths of an app project, sometimes it's easy to get confused and a little overwhelmed with all the functions and logic going on. This lab helps us step out from the weeds and play around with the big picture.

### Meet Hugbot

We're going to write a little robot that has two functions. She can talk and she can hug.

Let's start by creating a blank file and calling it `hugbot.py`.

```
   
```

Now let's give our robot a name:

```
HUGBOT_NAME = 'Henrietta'
```

If you run the file now (`python hugbot.py`) nothing will happen. Let's continue...

#### Letting Hugbot Talk

Create a `speak` function that takes an argument for the message, and `print`s that message out.

From here on, other than debugging, **do not use any other `print` statements in the hugbot code**.

<pre class="hint">
def speak(message):
    print message
</pre>

If you run `python hugbot.py` now, still nothing will happen. We have defined a function, but not run it.

Add a line **before** your speak function for Hugbot to say something:

```
speak("Hello, my name is " + HUGBOT_NAME)
```

What happens?

```
NameError: name 'speak' is not defined
```

This is because Python runs everything in the file in the order it sees it. If you put the `speak("...")` function call before you tell Python what `speak` means, it will get confused.

Move the `speak("Hello")` line **after** your speak function.

Now Hugbot should print something out. Whee!

#### Letting Hugbot Hug

Now let's create a simple function called `hug` that doesn't take any arguments, and makes Hugbot `speak` the message `**hug**`.

<pre class="hint">
def hug():
    speak("**hug**")
</pre>

Since `hug` needs to know about `speak`, make sure it is declared after `speak`.

Running the file won't do anything different yet, so let's add a call to `hug()` at the bottom of our file - and check it works.

[Check your hugbot against mine so far!](https://gist.github.com/jennielees/21066b173f74b4887f6f)

#### Giving Hugbot a Brain

Let's make Hugbot more intelligent with a `brain` function. This is going to be the default mode of operation for Hugbot. Let's put our `speak("Hello...")` and `hug()` instructions into this function, so that we only have to run `brain()` to operate Hugbot.

```
def brain():
    speak("Hello, my name is " + HUGBOT_NAME)
	hug()
	
# Make sure you remove these lines from elsewhere in the file or they will run twice!
```

Top it off with a call to `brain()` at the bottom of the file. When you run it, it should output the same thing as before.

[Checkpoint](https://gist.github.com/jennielees/275c2560d71b8548e6af)

#### More Brains

Let's give Hugbot a "boot-up" sequence that plays when she is first started. Replace your "Hello" `speak` call with a call to a function `boot()`:

```
def brain():
    boot()
    hug()
```

Now we need to make the `boot()` function work. Create it, with the `speak` line from before.

<pre class="hint">
def boot():
    speak("Hello, my name is " + HUGBOT_NAME)
</pre>

Add some more flavour in there if you want, like:

<pre class="hint">
def boot():
    speak("0101010101110110111000000.... Ready")
    speak("Hello, my name is " + HUGBOT_NAME)
</pre>

[Checkpoint](https://gist.github.com/jennielees/becde32635af89bf2110)

### Returning Stuff

So far our functions don't really interact with each other, they are just a nice way to group up our logic so it's easier to understand and to read.

Let's change that and pass some things between functions so they are a little more aware of each other!

#### Say My Name

Create a little function called `get_name` that takes no arguments and returns the hugbot's name.

```
def get_name():
    return HUGBOT_NAME
```

Now in `boot`, where we speak the name, we want to call this function instead of using `HUGBOT_NAME` directly.

<pre class="hint">
def boot():
    bot_name = get_name()
    speak("Hello, my name is " + bot_name)
</pre>

We are taking the output of `get_name()` and storing it in a variable called `bot_name`, then using that to `speak`.

#### Status Affirmative

Let's check that the boot worked ok. We don't want to ask Hugbot to do things if she didn't boot up properly.

Modify `boot` to return a `True` value and in `brain`, check that `boot` returned `True`.

<pre class="hint">
def boot():
    bot_name = get_name()
    speak("Hello, my name is " + bot_name)
    return True
    
def brain():
    booted_ok = boot()
    if booted_ok:
        hug()
</pre>

Change `boot` to return `False` (temporarily) and test that hugbot doesn't hug.

[Checkpoint](https://gist.github.com/jennielees/0d368793f9c5a4922097)

#### On the Fritz

Use `random` to decide whether Hugbot boots successfully or not.

Also, do something in `brain` if Hugbot doesn't boot up - have her `speak` an error.

```
# at top of file
import random

boot_options = [True, False]

...

def boot():
    ...
    random_outcome = random.choice(boot_options)
    return random_outcome
```

Your `imports` should always be right at the top of the file.

Since you are putting your `random.choice` result into a variable and then immediately `return`ing that variable, you can shortcut:

```
    return random.choice(boot_options)
```

What happens if you don't have a `return` line?

[Checkpoint](https://gist.github.com/jennielees/4d2c6156b9de6562e890)

### Giving Hugbot New Tricks

Pick a new piece of functionality for Hugbot. We'll use `wave` for this example but feel free to choose your own.

Define a function that has Hugbot `speak` a new thing.

```
def wave():
    speak("**wave**")
```

First, add this to Hugbot's `brain` after she calls `hug()`.

#### Hugbot Logic Core

Let's use `if` to make Hugbot do one of our two actions, and use `random.choice` to decide which one.

```
hugbot_actions = ['hug', 'wave']

def brain():
    booted_ok = boot()
    if booted_ok:
        action = random.choice(hugbot_actions)
        if action == 'hug':
            hug()
        if action == 'wave':
            wave()  
    else:
        speak("System failure :(")
```

(You can take the random system failure out if this is a little _too_ random for you. To do so, just have `boot` return `True`.)

[Checkpoint](https://gist.github.com/jennielees/3d4ce7b6b61737ae0058)

Add another `hugbot_action` of your own choice.

### Controlling Hugbot

Instead of `random.choice` it would be cool if we could just type in commands.

Fortunately `raw_input` fits in pretty neatly.

```
def brain():
    booted_ok = boot()
    if booted_ok:
        action = raw_input("What should Hugbot do? ")
        if action == 'hug':
            hug()
        if action == 'wave':
            wave()  
```

How to deal with unexpected input? Choose one of the following (or a different strategy)!

* Check if it is in `hugbot_actions` and if not, print an error (you can also do this by `if/else`)
* Assume the user is trying to have a conversation and repeat what they said back to them (like a good listener)

[Checkpoint](https://gist.github.com/jennielees/8207d99aeda752e2a122)

#### Setting Hugbot's Name

Add a line to `boot` that asks the user for Hugbot's name.

If they don't enter anything, make the `boot` function return `False`.

[Checkpoint](https://gist.github.com/jennielees/9583b0d14d038d12bb93)

#### Continuous Operation

Using a `while` loop, once Hugbot has responded to the user's request, just go round again and ask them for a new thing to do.

```
    while True:
        action = raw_input("What should Hugbot do? ")
        # ... do something ...
        # at the end of this loop we will return to the start!
```

Extend this by exiting the function (with `return`) if the user types in 'quit' as the answer to that question.

```
    if action == 'quit':
        return
```

[Checkpoint](https://gist.github.com/jennielees/540e3426a7532c5f0d85)

Now let's build out Hugbot to do a whole bunch of awesome things.

### Action, Camera, Lights

Define an `perform_action` function that takes a verb and prints out an "action" style message, adding 's' to the verb.

Sample usage:

```
HUGBOT_NAME = 'Henrietta'
perform_action('wave') => "Henrietta waves"
perform_action('dance') => "Henrietta dances"
perform_action('sit') => "Henrietta sits"
```

You will need to change `boot` to `return` the bot name, not True.

Extension: Use a dictionary to extend this beyond just adding 's'.

```
action_map = { 'dance': "boogies like it's 1999" }

perform_action('dance') => "Henrietta boogies like it's 1999"
```

Change the previous actions (e.g `hug`) to this new format, and change `brain` to use this instead of the `if` statements. 

How are you going to handle `perform_action()` with an empty action, and actions that aren't in your dictionary?

### Dictionary Discourse

Using a dictionary of input sentences to output sentences, have Hugbot make witty replies to whatever the user types in.