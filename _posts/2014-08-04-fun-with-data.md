---
layout: post
title: Fun with Data
week: 2
---


## Comma Separated Victory

Let's look at some real data!

`sweep.csv` is a file containing data about San Francisco street cleaning. This was pulled from [DataSF.org](http://apps.sfgov.org/datafiles/index.php?dir=PublicWorks) and converted to csv format with a Python script! :+1:

Get the `sweep.csv` file from [here](/public/data/sweep.csv). CSV, short for comma-separated value, is a common format and many places can give you CSV data to work with, including your friendly local spreadsheet program.

### Peeking inside the file

It's always good to look at any file before you start trying to do stuff with Python, so you know what to expect.

* Open the file using your text editor first. You should see something that looks a bit like this:

![sweep.csv](/public/sweep_sublime.png)

* There is a Terminal command to just print the first few lines of the file. It's called `head` (and its counterpart, `tail`, prints the last few lines). See if you can figure out how to use `head` on `sweep.csv`. 

    Remember, hitting Ctrl-C usually gets you out of trouble in Terminal.

<pre class="hint">
$ head sweep.csv
CNN,WEEKDAY,BLOCKSIDE,BLOCKSWEEP,CNNRIGHTLE,CORRIDOR,FROMHOUR,TOHOUR,HOLIDAYS,WEEK1OFMON,WEEK2OFMON,WEEK3OFMON,WEEK4OFMON,WEEK5OFMON,LF_FADD,LF_TOADD,RT_TOADD,RT_FADD,STREETNAME,ZIP_CODE,NHOOD,DISTRICT
13798000,Fri,,1642922,R,Corona St,12:00,14:00,False,True,False,True,False,False,221,299,298,222,CORONA ST,94127,Ingleside Terrace,
13576001,Fri,East,1635302,L,West Point Rd,09:00,11:00,False,True,True,True,True,True,1,199,198,2,WEST POINT RD,94124,Hunters Point,
6894003,Thu,,1601353,R,Hester Ave,07:00,08:00,False,True,True,True,True,True,1,99,98,2,HESTER AVE,94134,Visitacion Valley,
6894003,Tues,,1642803,L,Hester Ave,07:00,08:00,False,True,True,True,True,True,1,99,98,2,HESTER AVE,94134,Visitacion Valley,
6894004,Thu,,1601354,R,Hester Ave,07:00,08:00,False,True,True,True,True,True,101,211,210,100,HESTER AVE,94134,Visitacion Valley,
6894004,Tues,,1642804,L,Hester Ave,07:00,08:00,False,True,True,True,True,True,101,211,210,100,HESTER AVE,94134,Visitacion Valley,
5371001,Fri,,1601340,L,Executive Park Blvd,10:00,15:00,False,True,True,True,True,True,1,91,90,2,EXECUTIVE PARK BLVD,94134,Bayview Heights,
5371001,Fri,,1601346,R,Executive Park Blvd,10:00,15:00,False,True,True,True,True,True,1,91,90,2,EXECUTIVE PARK BLVD,94134,Bayview Heights,
4640103,Wed,,1612953,R,De Haro St,12:00,14:00,False,True,True,True,True,True,1357,1399,0,0,DE HARO ST,94107,Potrero Hill,
</pre>

* Try opening the file using a spreadsheet program. I've uploaded it into [Google Docs here](https://docs.google.com/spreadsheets/d/1xmj93394Ce0ImkJtufKeU_IMT8tqG0l4Nm_R3Dha86U/edit?usp=sharing) to save you some time!

What Google Docs (or your spreadsheet program) has done is convert each item between commas into a cell in the spreadsheet. You'll need to do something similar in Python to make the data in the file actually usable.


### Using Python to read the file

* We already saw how to read in a file and split up a string into smaller bits in the superhero exercise, so let's do the same thing again.
* We'll read in the data from `sweep.csv` by using `list()` to get a list, and use `split(',')` to examine it.
* However, if we try `print`ing the whole list, we'll get a bunch of junk scrolling back. 

  This is a nearly 40,000 line file, so let's use the `[:]` operator to access part of the list:

```
>>> with open('sweep.csv') as f:
...    data = list(f)
...
>>> for line in data[0:3]:
...    print line
...
```

To see what the first two lines are all about, [check this diagram](/public/reading_file.png).

`data[0:3]` accesses the first three items in the list `data`, which is a bit more manageable.

### More on :

What just happened? What does `[0:3]` do?

Let's break it down.

![lists](/public/list_slices.png)

Just as we use `mylist[i]` to access the list item at position `i`, e.g. `data[0]` to access the first item in the list `data`, we can use the `i:j` syntax to access the part of the list from position i up to, _but not including_, j. This is really helpful if we don't want to go through a whole long list just to take a look, as above. 

The formal name for this is **array slicing** or **list slicing**.

What happens here? Are there numbers that don't do what you might expect in a slice? What if you don't put a number in?

Remember, `[]` means an empty list.

```
>>> mylist = ['a','b','c','d','e','f']
>>> mylist[2:4]
>>> mylist[0:7]
>>> mylist[0:99999999]
>>> mylist[0:0]
>>> mylist[:4]
>>> mylist[4:]
>>> mylist[:]
>>> mylist[4:2]
```

### A special kind of negative

The value `-1` in lists (and any other negative values) actually do a kinda logical thing. They count **backward** from the end of the list.

As you probably spotted from the last entry above, the numbers in a slice must be in increasing order, i.e. `mylist[4:2]` returns an empty list `[]`. 

When using negative indices, an easy way to think of them is that Python counts how many items are in the list, and translates the negative into the real position you meant. So if your list has 7 items and you are asking for item -1, Python translates that into asking for item 6.

```
>>> mylist = ['a','b','c','d','e','f','g']
>>> mylist[-1]
>>> mylist[-3]
>>> mylist[-3:-6]
>>> mylist[-3:-1]
```

`mylist[-3:-6]` is exactly equivalent -- since `mylist` has 7 items -- to `mylist[7-3:7-6]`, ie `mylist[4:1]`, which is in the wrong order and so empty.

`mylist[-3:-1]` is exactly equivalent to `mylist[7-3:7-1]`, ie `mylist[4:6]`, which is `['e', 'f']`.

Most of the time you'll see this used to chop the end off a list when you don't care about the last thing in it.

### Splitting it further

Going back to your `data` list, right now every single item in it is the same as a line in the `sweep.csv` file, i.e. just a plain ol' string. If you want to access pieces of it, we need to `split()` it up.

Use `split(",")` to split a string into a list, breaking it up wherever there's a comma.

<pre class="hint">
>>> for line in data[0:3]:
...    print line.split(",")
['CNN', 'WEEKDAY', 'BLOCKSIDE', 'BLOCKSWEEP', 'CNNRIGHTLE', 'CORRIDOR', 'FROMHOUR', 'TOHOUR', 'HOLIDAYS', 'WEEK1OFMON', 'WEEK2OFMON', 'WEEK3OFMON', 'WEEK4OFMON', 'WEEK5OFMON', 'LF_FADD', 'LF_TOADD', 'RT_TOADD', 'RT_FADD', 'STREETNAME', 'ZIP_CODE', 'NHOOD', 'DISTRICT\n']
['13798000', 'Fri', '', '1642922', 'R', 'Corona St', '12:00', '14:00', 'False', 'True', 'False', 'True', 'False', 'False', '221', '299', '298', '222', 'CORONA ST', '94127', 'Ingleside Terrace', '\n']
['13576001', 'Fri', 'East', '1635302', 'L', 'West Point Rd', '09:00', '11:00', 'False', 'True', 'True', 'True', 'True', 'True', '1', '199', '198', '2', 'WEST POINT RD', '94124', 'Hunters Point', '\n']
</pre>

**Note** Whenever you print something like this, you aren't actually changing it. It just vanishes when it's done printing.

Let's try another (more appropriate) way of reading the file in first.

### Splitting from split()

This method works for a 'clean' CSV, but .csv files are so common and varied that Python has a way of accessing them more easily, to deal with different standards. For example, the `split` call above fails if there is a comma inside one of the items.

### csv.reader, your new best friend

Python has a whole bunch of built in libraries that do cool stuff. `csv` is one of these (remember `random` from last week?). When you `import csv` you get access to `csv.reader`, which creates a csv reader from your file. You can then loop through the `reader` object and get a nicely-formatted row back.

As with many Python built in libraries, the official documentation here is [pretty intense](https://docs.python.org/2/library/csv.html). However, heading to the [examples](https://docs.python.org/2/library/csv.html#examples) section is actually a useful way to learn more about this library.

You'll be expanding this piece so this would be a good time to put your code in a new file, calling it something like `sweep.py`. 

Run `python sweep.py` from a Terminal to run the file.


```
import csv

with open('sweep.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
```

Notice how `csv.reader` got rid of those pesky newlines? There are no `\n` characters hanging about!

"OMG IT PRINTED A WHOLE BUNCH OF STUFF": It was supposed to. The code above says "With the file sweep.csv open, make a CSV reader and print every row it has". Our file has a **lot** of rows.

How could you fix this?

<pre class="hint">
import csv

max_rows_to_print = 5
rows_printed = 0

with open('sweep.csv') as f:
    reader = csv.reader(f)
    for row in reader:
		if rows_printed < max_rows_to_print: 
            print row
            rows_printed += 1
</pre>

Another way using `reader`'s special `line_num` variable, which keeps track of the current line it is reading, in just the same way as adding 1 to `rows_printed`.

<pre class="hint">
import csv

max_rows_to_print = 5
rows_printed = 0

with open('sweep.csv') as f:
    reader = csv.reader(f)
    for row in reader:
		if reader.linenum < max_rows_to_print: 
            print row
</pre>

Experimenting:

* How much is the `reader` object like a list? Can you access row 30 of the reader? (What happens if you try `reader[30]`?
* Is the `row` object like a list? Can you access item 5 of a row? (What happens if you try `row[5]`?)

<pre class="hint">
You need to try:

print reader[30]

inside your file, if you're using a file.

This won't work. See below for why not.

However, the other one:

print row[5]

should work just fine. It prints the thing at position 5 (in Python speak, remember the first one is 0) for every row.
</pre>


**Iterators**: The `reader` object is a special kind of [iterator](http://anandology.com/python-practice-book/iterators.html), and not the same as a list. It behaves a lot like a list, but for example, you can only loop through it once. If you want to access this data separately, such as from another for loop, you'll need to load it into a new list first. This is often a good point to pull out the parts of the data you actually want.

For example, if you wanted to get all the neighborhoods from the csv, using `csv.reader`:

```
import csv

neighborhoods = []

with open('sweep.csv') as f:

    reader = csv.reader(f)

    for row in reader:

        neighborhood = row[-2]
        # Negative means count from the right, which is easier here

        if neighborhood not in neighborhoods:
            # Append it to the list!
            neighborhoods.append(neighborhood)

print "Found {} neighborhoods".format(len(neighborhoods))
print sorted(neighborhoods)

```

_You can also call them neighbourhoods if you are so inclined. :wink:_

What's going on here? Add `print` statements to get more insight.

What is in `neighborhoods`?

Notice how we said explicitly at the beginning that `neighborhoods` was an empty list. This means we can put stuff in it (using `append`) and that it will stick around after our indented code is finished.

### When is SF at its cleanest?

Using this data (either method), let's see if we can figure out the most popular day of the week for street sweeping. In the individual rows, this is the second item (`row[1]`).

Write this into `sweep.py`, as you'll save yourself typing as we continue.

Hint: One way to do this would be to use a variable for each day, loop through the file, and count up the total number of times each day was seen:

```
monday = 0
tuesday = 0
...

if row[1] == "Mon":
    monday += 1
```

`+=` is a shortcut for a variable adding 1 to itself, instead of typing `monday = monday + 1`.

Do you notice anything slow, or error-prone about this approach?

Let's move on to look for a specific piece of information.

### Exploring the streets

Also known as "Getting down with `if`".

Update `sweep.py` to print out answers to the following questions. 
Explore the file a little before trying to answer the questions. It always helps to be able to answer them without a program, or at least have some idea how!

As well as your usual file viewers, see if you can figure out what these commands do in Terminal:

* `grep Sutter sweep.csv`
* `grep Sutter sweep.csv | less` (hit space to continue, or q to exit)

#### Exploring Questions

* Find your street name (or a street you like, eg Sutter St!)
* Which day(s) of the week is your street swept?
* Which week(s) of the month?
* Can you identify which day your specific section of the  street is swept? (The columns `LF_FADD` and `LF_TOADD` specify left-side from and to numbers; `RF_FADD` and `RF_TOADD` similarly the right-side. You might also need to look near the start of the row for the side of the street that this row is talking about.)
  * **Note on comparing numbers to strings - don't! :)**
  
  
      `LF_FADD` is a _string_, ie. something like `'301'`. If you try to compare this to a _number_, like `301` (no quotes!) it won't work:
  
      ```
  >>> 301 == '301
  >>> 301 == 301
      ```
  
      How do you fix this? One option is to figure out the right block numbers for your street and compare the strings:
  
      ```
  left_from = row[14]
  left_to   = row[15]
  if left_from == '301' and left_to == '399':
      print 'They are the same'
      ```
       
      Another option (more advanced) is to convert the `left_from` and `left_to` variables to numbers, but since this is Real Data, it's messy and doesn't always work. So we need to _try_ converting it and see if it works (we'll cover this more later, trust me.)
     
      
      ```
      # ... [ this goes inside your for loop ] ...
    
      try:
          left_from = int(row[14])
          left_to   = int(row[15])
      except:
          print "This row has some weird data! Boo!"
          continue
      
      # ... [ if you got to this point in the code, then left_from and left_to now have numbers in them] ...
      
      if left_from < 400 and left_to > 300:
          print 'I am on my block'
      ```
  
      The `continue` will go back through the `for` loop again and skip the row with bad data.

### Fun with functions

We've already seen [functions](http://www.learnpython.org/en/Functions) around, but let's get more familiar with them.

What's a function? In short, they are a really good way of wrapping up some code in a neat bundle to run again or re-use.

What does a function look like? With one, your code can move from

```
do this
do that
do this
do that
do this
```

to:

```
def do_this():
    do this
    do that

do_this()
do_this()
do_this()
```

You can imagine, the more you have to do something, the more attractive functions look. There are other reasons, too; putting your code in neat parcels makes it easier to understand, both for your future self and other people, and often saves a whole bunch of typing.

Take the code you wrote above to find when your street was being swept.

Turn it into a function -- without changing the logic, that's as easy as indenting it and adding a 'def'.

```
def sweep_times():
    #  your code here
```

Now to make sure this gets called, or executed, put the command `sweep_times()` in your code right after.

<pre class="hint">
def sweep_times():
    # your code here
    # by the way,
    # lines starting with a pound sign
    # (or hash if you're British)
    # are comments, which can contain anything
    
# to call the function, get out of the indent
# so python knows you are no longer telling it the
# function definition 
# then just invoke the function name

sweep_times()

# if you put this call before the 'def' part, python
# has no idea what you mean, as it steps through
# your file in order - try it!
</pre>

You can also check out the [Codecademy section on functions](http://www.codecademy.com/courses/python-beginner-c7VZg/0/1?curriculum_id=4f89dab3d788890003000096) or [Learn Python the Hard Way 18 and 19](http://learnpythonthehardway.org/book/ex18.html) for more context on functions.

### Parameters (not parking meters)

That's great but your function only does one thing. Fortunately those brackets are just waiting to be filled with a *parameter*, or two...

Parameters let your function take a piece of input and use it locally. Think back to math and f(x): it's the same principle.

Here's a simple function, complete with parameter:

```
def print_hello(name):
    print "Hello, {name}".format(name=name)
```

To call the function, give it something to do:

```
print_hello("Lady Gaga")
print_hello("Benedict Cumberbatch")
```

What happens if you put a number instead of a string inside the parentheses? What if you don't put anything?

### An argumentative interruption

    A: Your function takes a parameter?
       How strange, mine takes an argument!
    B: What, that? You call that an argument?
       That's not an argument.
    A: Oh yes it is!
    B: Oh no it isn't!
    A: *This* is an argument.
    B: Exactly.

In programming sometimes people get very caught up on specific definitions. Here's one of them.

A parameter's the thing in the function definition itself, so the word 'name' in `print_hello(name)` earlier.

An argument is the value you put in *when you call the function*, so the string (e.g. "Benedict Cumberbatch") itself.

Within the function, the argument you put in gets assigned to the variable you defined in the brackets. This works up to as many arguments as you can handle.

```
def many_things(one, two, three, four, five, six):
    print "I have one {one}, two {two}s, three {three}s, four {four}s, five {five}s and six {six}s.".format(one=one, two=two, three=three, four=four, five=five, six=six)

many_things("nose", "ear", "piercing", "limb", "sense", "cousin")
```

What kind of error do you get if you forget an argument? What if you put one extra in? (You'll see these kinds of errors more than you'd think, so get a feel for them!)

### Parameter Street

Re-define your street sweeping function to take a parameter, `street_name`, and use this instead of the hardcoded street name you were using before.

You should be able to call this successfully:

```
sweep_times("Sutter St")
```

and see a print-out of the days this street is swept.

What happens if the street isn't in the sweep.csv list?

(Stuck? Check this [gist out](https://gist.github.com/jennielees/ca5d6a23836b107b31ce) for a skeleton.)


### Command-line parameters

When you run your program itself, it has parameters! The system incantation `sys.argv` (for 'argument values') is a handy way of looking at the parameters supplied when you run the file.

```
python myfile.py one two three
       ^^^^^^^^^^^^^^^^^^^^^^^
       these are all arguments to the 'python' command!
```

Try creating a really simple file, `myfile.py` which just contains the following:

```
import sys

print sys.argv
```

What happens when you run it like above?

How would you get at the argument 'one' in the example?

Can you extend your `sweep_times` file to take a command line argument, e.g.

```
python sweep.py "Sutter St"
```

What happens if you forget the quotes?
