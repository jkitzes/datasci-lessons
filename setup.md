---
layout: page
root: .
title: Setup Instructions
---

To complete the lessons on this site, you'll need to install a few software packages. Below are instructions for setting up the Bash shell, a scientific Python distribution, git, and a text editor on Mac, Linux, and Windows systems (thanks to [Software Carpentry](http://github.com/swcarpentry/workshop-template) for many of the ideas below).

### Bash

Mac users can access a Bash shell through the Terminal program found in the Applications folder, in the Utilities subfolder. Linux users likely have Bash set as their default shell (if not, type `bash` after opening a terminal window).

Windows users should download and install [Git for Windows](https://git-for-windows.github.io/). During installation, make sure that you check the options for __Use Git from the Windows Command Prompt__, __Checkout Windows-style, commit Unix-style line endings__, and __Use Windows' default console window__ when they appear.

### Python

On all platforms, you can easily install Python 3 and all of the necessary 
scientific packages by installing the [Anaconda scientific python 
distribution](http://continuum.io/downloads). Follow the instructions on the download page, and make sure that you check the option to __Make Anaconda the default Python__ when installing, if it appears.

### Git

Mac users with OS 10.9 or above should download the most recent available installer from [this link](http://sourceforge.net/projects/git-osx-installer/files/). Linux users may already have git installed (check by typing `git` from a terminal window). If not, git can be installed from the system's package manager (e.g., `sudo apt-get install git` for Ubuntu/Debian). Windows users who have installed Git for Windows do not need to install anything else.

### Text Editor

First, you'll need the `nano` command line editor, which should already be
available on Mac and Linux systems. Windows users should download the [Software Carpentry Windows Installer](http://files.software-carpentry.org/SWCarpentryInstaller.exe) and double click to run it. Note that you'll need to be connected to the internet for this installer to work.

Second, you'll probably want to install a more powerful plain text editor. On 
Windows, you can use [Notepad++](http://notepad-plus-plus.org/). Mac users can use [Text Wrangler](http://www.barebones.com/products/textwrangler/), and Linux users can use [Kate](http://kate-editor.org/).

### A Special Note for Windows Users

You should be aware that Windows users consistently run into more trouble with installation and configuration than than Mac or Linux users. If the above instructions aren't working or if you see error messages while working through the lessons, you can instead use a self-contained Linux virtual machine maintained by Software Carpentry.

To use the virtual machine, download and install [VirtualBox](https://www.virtualbox.org/) and [this virtual machine image](https://docs.google.com/uc?id=0B4Kr6DYkzkQtSTZLQzF4aVB4NDQ&export=download). Open VirtualBox and go to File -> Import Appliance and select the virtual machine image file. You can accept all of the recommended configuration options. VirtualBox will then open a Linux desktop environment that you can use to complete the lessons on this site. In the future, you can simply open VirtualBox to return to your virtual machine (you can also now delete the image file).

### More Help

If you have trouble with this setup process, or if you receive error messages as you work through the lessons, refer first to the Software Carpentry Wiki page on [installation and configuration issues](https://github.com/swcarpentry/bc/wiki/Configuration-Problems-and-Solutions). Google is probably a reasonable next step. If all else fails, you can try using the Virtual Machine described above.
