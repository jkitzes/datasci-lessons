---
layout: lesson
root: .
title: Setup Instructions
---

To complete the lessons on this site, you'll need to install a few software 
packages on your computer. Below are instructions for setting up a scientific 
Python distribution, the Bash shell, git, and a text editor on Mac, Linux, and 
Windows systems (thanks to [Software 
Carpentry](http://github.com/swcarpentry/bc) for many of the ideas below).

### Python

On all platforms, you can easily install Python 2.7 and all of the necessary 
scientific packages by installing the [Anaconda Scientific Python 
Distribution](https://store.continuum.io/cshop/anaconda/).

### Bash

Mac users have the Bash shell already set up, and Linux users likely have Bash 
set as their default shell (if not, type `bash` after opening a terminal 
window).

Windows users should install [Git 
Bash](http://code.google.com/p/msysgit/downloads/detail?name=Git-1.8.4-preview20130916.exe). 
(Note that this link intentionally points to Git Bash v1.8.4, as the more 
recent v1.8.5 has a bug that causes problems with GitHub.) Next, download this 
[additional installation 
script](https://raw.github.com/swcarpentry/bc/master/setup/swc-windows-installer.py) 
and place it on your Desktop. Open Git Bash and you'll see a black window with 
a blinking underscore. Type the following three commands, pressing enter after 
each one.

    cd
    cd Desktop
    python swc-windows-installer.py

After the last command, it will look like nothing is happening for a minute, 
but eventually you'll see the blinking underscore again. At that point you can 
close Git Bash.

### Git

Mac and Linux users can download git [here](http://git-scm.com/downloads) or 
install it through a package manager. Windows users who have installed Git Bash 
do not need to install git separately.

### Text Editor

First, you'll need the `nano` command line editor, which should already be
available on Mac and Linux systems and will be available to Windows users who 
have run the additional installation script described above.

Second, you'll probably want to install a more powerful plain text editor. On 
Windows, you can try [Notepad++](http://notepad-plus-plus.org/). Mac users can 
try [Text Wrangler](http://www.barebones.com/products/textwrangler/), and Linux 
users can try [Kate](http://kate-editor.org/).

### A Special Note for Windows Users

You should be aware that Windows users consistently run into more trouble with 
installation and configuration than than Mac or Linux users, and you should try 
to use a non-Windows system for these lessons if you have a choice. If the 
above instructions aren't working or if you see error messages while working 
through the lessons, you can instead use a self-contained Linux virtual machine 
maintained by Software Carpentry.

To use the virtual machine, download and install 
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [this virtual 
machine image](http://ktzs.us/4m1q7). Open VirtualBox and go to File -> Import 
Appliance and select the virtual machine image file. You can accept all of the 
recommended configuration options. VirtualBox will then open a Linux desktop 
environment that you can use to complete the lessons on this site. In the 
future, you can simply open VirtualBox to return to your virtual machine (you 
can also now delete the image file).

### More Help

If you have trouble with this setup process, or if you receive error messages 
as you work through the lessons, refer first to the Software Carpentry Wiki 
page on [installation and configuration 
issues](https://github.com/swcarpentry/bc/wiki/Configuration-Problems-and-Solutions). 
Google is probably a reasonable next step, and if all else fails, you can try 
[contacting me](mailto:jkitzes@berkeley.edu).
