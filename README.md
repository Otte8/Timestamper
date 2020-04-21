<h1 align="center">
  <br>
  Timestamper
  <br>
</h1>

<h4 align="center">Script to log timestamps.</h4>

<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Made%20With-Python%203.8-blue.svg?style=for-the-badge" alt="Made with Python 3.8">
  </a>
</p>

# Overview

Timestamper is a very small Python script designed to take timestamps from the time the script was executed by the click of a button. The script was developed with streaming in mind, and the original purpose of the script was to log timestamps for creating montages from your stream.
This is only one thing Timestamper can be used for of course. Use it however you like!

[Installation](#installation) is easy, and you do **NOT** need to know anything about coding! Everything needed to change the way timestamps are logged is descriped in [Change Key](#change-key).


# Installation

**Only Windows 10 is officially supported, but Timestamper should work on MAC and Linux** 

## Windows
### Needed software

<a href="https://www.python.org/downloads/">Python 3.8.2</a> - Python 3.5+ will work, but is not tested - Choose the option to add Python to PATH)

<a href="https://git-scm.com/downloads/">Git</a> - Choose the option to "Git from the command line and also from 3rd-party software" in Git's setup

### Installing dependancies

Timestamper only has one Python library as a dependancy and is easily installed.

Start with opening a command prompt (open Start, search for "command promt" or "cmd", then click it)

In the command promt type the following and hit enter:

```
pip install pynput
```

After pynput is installed you can download and run the script. To download the script type the following in the command prompt and hit enter:

```
git clone https://www.github.com/Otte8/Timestamper.git
```

When it is done downloading, edit the timestamper.bat file in the Timestamper directory. It should say:

```
python C:\Users\username\Desktop\Timestamper.py
```

Change the path to the path, where your Timestamper.py script is located. I recommend moving the timestamper.bat file to the desktop for convenience, as that is the file you have to run and the .txt file it outputs will be located where the timestamper.bat file is.

Now the setup of Timestamper is complete! You can now double-click the timestamper.bat file and the script is running!

# Change Key

To change the key used to log a timestamp all you have to do is to edit the Timestamper.py file.

```python
if key.char == "q":
```

is on line 18. You can change the q inside the quotation marks to a different letter. This can be changed whenever you want it, and the effects take place, when you run the script the next time.
