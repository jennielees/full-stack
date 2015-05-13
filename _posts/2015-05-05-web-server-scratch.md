---
layout: post
title: Web Server from Scratch
week: 2
---

### What does a web server do?

The goal of this lab is to work through some of the basic functionality of a web server, so we can better understand web frameworks.

* [Longer explanation of the anatomy of a web request](http://robrich.org/slides/anatomy_of_a_web_request/#/31)
* [HTTP Status Codes](http://httpstatus.es/)
* [What happens when you type an address into the address bar and hit enter?](https://github.com/alex/what-happens-when)

### Building our own

We're going to look at three things.

* Handling connections and incoming requests
* Mapping URL paths to responses
* Returning appropriate error codes


#### Handling responses

In order to allow browsers to connect to our server, we'll open a **socket**. Once the socket is open we can listen for data, and send it back. When we are done sending, we'll close the socket.

This uses the `socket` module. Don't feel you have to learn this syntax - this is more for illustration. The other two parts of the server are more important!

```
import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', 5000))
print "Web server running..."
server_sock.listen(10)

while True:
    client_sock, addr = server_sock.accept()
    print 'We have opened a socket!'
    print client_sock.recv(100)  # these are the incoming headers

    output = "<h1>Hello Client</h1>"
    client_sock.send("HTTP/1.1 200 OK\n")
    client_sock.send("Content length: "+str(len(output)))
    client_sock.send("Content-Type: text/html\n\n")
    
    client_sock.send(output)
    client_sock.close()
```

Save this code as a file (maybe `server.py`) and run it. Connect to http://localhost:5000 in a web browser. What do you see?

Can you get the `client_sock` to send the contents of a file, instead of the string HTML?

#### Mapping paths to responses

Look at the printout from your `client_sock`. The first part shows the headers from the incoming request.

You should see a line that looks something like

```
GET / HTTP/1.1
```

This contains the path being requested (`/`).

What happens if you try to visit [http://localhost:5050/kittens](http://localhost:5050/kittens)?

Can you use this knowledge to use `if` statements and return a different HTML file if a different path is being requested? You'll probably want to make a couple of different test files for this, and you might find the `split()` and `startswith()` functions helpful.

Is there a way to do it without having a lot of `if`s? Maybe some other way you could store the paths and filenames...

#### Handling errors

To return an error code, we need to make sure we start our response with a status line:

```
client_sock.send("HTTP/1.1 200 OK\n")
```

If we change this to a code that isn't 200, we're telling the client that something "not OK" is happening. (This doesn't always mean an error - 301 Redirect is perfectly normal, but the client has to follow it and request a new page.)

Try changing a `200 OK` somewhere to `404 Not Found`. Visit the page in your browser and look at the Network Inspector (you may have to reload the page). If your status code was sent back correctly, it'll show up there!

Can you combine this with the previous section to return a 404 for paths that haven't been explicitly defined?

#### Optional Challenges

Pick another [error code](http://httpstatus.es/) and implement it. 301, 418 and 500 are all good starting points.

So far, you've only implemented GET to get a single page. Can you deal with query strings (`/kittens?number=10&type=cute`)? Make your code do something different based on the query string -- you can go back to the "HTML as strings" to do this.

Building on this, see if you can figure out a way to combine the HTML page itself with the query string variable. You might want to define a specific page and syntax to make this concrete:

kittens.html
```
<img src='http://placekitten.com/g/SIZE/SIZE'/>
```

and somewhere in your code you might read the contents of that file into a variable called `html_string`, and then, assuming you got a variable called `querystring_size` and put something from the query string in it:

```
html_string = html_string.replace('SIZE', querystring_size)
```

Finally, last super optional challenge: can you implement POST as well as GET?

### Extra Reading

* [Let's Build a Web Server](http://ruslanspivak.com/lsbaws-part1/)