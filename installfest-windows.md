---
layout: page
title: Installfest (Windows)!
permalink: installfest-windows/
---

####A little extra setup to get things working really smoothly on Windows.

See [Installfest](../installfest) - do this first.

You need to have:

* Installed git bash
* Installed Python 2.7

#### Test Python

Open Git Bash and type `python --version`.

If you get something that looks like "Python 2.7.8", you're good. Go on to "pip"!

If you get a "sh.exe: python: command not found" error it's because Git Bash doesn't know about Python yet. We need to tell Windows where to find the Python program that will turn our Python scripts into machine code, so we give it a `PATH`, a list of folders it can look in.

Open Notepad and create a new file containing:

```
export PATH=/c/Python27:/c/Python27/Scripts:$PATH
```

(If you changed the default install directory for Python then change it here too.)

Save the file with the name `.bashrc` -- including the dot in front -- in your main user folder (mine is called 'Jennie' and located at C:\Users\Jennie). Notepad will probably be super helpful and try to save it as `.bashrc.txt`, so let's fix that.

Open Git Bash and type in `ls` to list the files. If you have loads of files this doesn't really help you much, so type `ls .bashrc*` to only list the files that start with `.bashrc` and end with anything (the `*` is a shortcut meaning 'match anything or nothing').

If you see `.bashrc` you're fine, if you see `.bashrc.txt` then type in `mv .bashrc.txt .bashrc` to move the file to the right name. (Yep, in UNIX terminology "rename" is just a kind of "move".)

Close and restart Git Bash and try `python --version` again!

```
$ python --version
Python 2.7.8
```

#### Pip

Pip is an awesome package manager for Python and we'll be using it a lot. It makes it super easy to get off-the-shelf libraries and code to supercharge your applications. If you've used JavaScript libraries or Rails gems before, you'll appreciate having something similar for Python!

Download this file: [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and save it somewhere you can find it, like your user folder.

In Git Bash, type `python get-pip.py` to run the Python script and get pip.

If you saved it somewhere else, you might change that command to `python Downloads/get-pip.py`.

Try the command `pip` once it's finished. It should Just Work, since it gets installed into C:\Python27\Scripts which you already added to your PATH earlier. Yay!

```
$ pip
....lots of stuff ending in...
  --cert <path>       Path to alternate CA bundle.
```

#### Virtual Environments

We will be installing `virtualenv` on Macs and Linux since it is a great way to manage your Python dependencies (the list of installed packages via pip) across projects. On Windows, this install is more tricky, but let's give it a shot.

In Git Bash, type

```
pip install virtualenv
```

and then

```
pip install virtualenvwrapper
```

Test it by making a new virtual environment:

```
mkvirtualenv hackbright
sh.exe": mkvirtualenv: command not found
```

Oh noes!

We have to jump through two more hoops to get this working (telling Windows where `mkvirtualenv` lives). [Source](http://www.asyndetic.com/2012/05/01/virtualenvwrapper-is-for-windows-users-too/)

1. Download [mktemp.exe](http://gnuwin32.sourceforge.net/packages/mktemp.htm) - extract it from this ZIP (todo: link directly to exe) and put it in your C:\Program Files (x86)\Git\bin directory, or wherever your Git install is.

2. Add a few more lines to your `.bashrc` file, directly underneath the $PATH line above.

        export MSYS_HOME='/c/Program Files (x86)\Git'
        export WORKON_HOME=$HOME/.virtualenvs
        if [ -e /c/Python27/Scripts/virtualenvwrapper.sh ]; then
            source /c/Python27/Scripts/virtualenvwrapper.sh
        fi

3. Restart Git Bash.

Try `mkvirtualenv hackbright` again, hopefully it should work now!

If it still doesn't, don't panic. We'll live without it. Especially if you got an error like "virtualenvwrapper could not create a temporary file name", this is kinda tricky to fix and fortunately `virtualenvwrapper` is not required, it's just nice to have.
