---
layout: page
root: ../..
title: Scientific Programming Basics
---

Scientific Programming Basics
=============================

The purpose of this section is to teach you the basic, core concepts of programming that transcend languages, how they fit together, and how you can use them to become a better scientist. Although these lessons use Python to teach these concepts, they are applicable to nearly all programming languages that you might use for your scientific work.

We (the instructors) recognize that you all unavoidably have come with very different backgrounds in Python programming. We expect that some of you may be familiar with basic Python, while a few of you of you have experience with additional modules such as numpy and scipy --- for those in that latter category, this section of the lessons may not be as novel as the other sections. However, we hope that the method of presentation will help to solidify your existing knowledge. We also encourage you to take the opportunity to ask the instructors and volunteers about more advanced techniques that you might have heard of but do not know how to use well.

For those who have no (or almost no) background in programming in any language, you may find that these lessons proceed quickly. We encourage you to make liberal use of the helpful volunteers as we proceed through these lessons. You may also wish to consider working together with a partner to complete the exercises as a team.

Regardless of your background, you will probably feel like trying to take in all of this material is like trying to drink from a firehose. That's OK - the idea is to introduce you to a wide variety of topics, with the hope that you (a) will get to reinforce the most important concepts during exercises, and (b) will be able to come back to these materials later to continue mastering the concepts.

The Seven Core Concepts
-----------------------

These lessons are organized around the [seven core elements](http://software-carpentry.org/2012/08/applying-pedagogical-principles-in-this-course.html) shared by all programming languages:

1.	Individual things (the number 2, the string 'hello', a figure)
2.	Commands that operate on things (the + symbol, the len function)
3.	Groups of things (lists, arrays, tuples, dictionaries)
4.	Ways to repeat yourself (for and while loops)
5.	Ways to make choices (if and try statements)
6.	Ways to create chunks (functions, objects/classes, modules)
7.	Ways to combine chunks (function composition)

In practice, the lines between these categories can be blurry --- for example, a string in Python actually mixes some characteristics of a thing, a group, and a "chunk". It's important to remember that these distinctions provide a conceptual framework that will help you, the programmer, to make sense of your programs. In the lessons below, we'll focus on the first six of these steps, as the seventh isn't as common in scientific Python and is a bit more conceptually advanced than the others.

Don't worry if you don't already know what all of the above examples mean --- 
you'll know by the end of this lesson.

The Lesson Files
----------------

Our Python lessons are divided into two main parts. In Scientific Programming I, we'll walk through these steps using a simple example of calculating time series data using a difference equation. This lesson will introduce you to the concepts described above and show how they can help structure your thinking about programming. In Scientific Programming II, we'll follow the same steps again, but using a more complex and real-life example of reading and analyzing a small data set. There's also an extra lesson below with some helpful tips on making publication-quality plots.

Each of these lessons relies on several files that you should download and save in an easily accessible location on your hard drive (perhaps a folder on your Desktop). Make sure that when you save each file in your browser, the appropriate file extention (i.e., .ipynb) is retained.

During the workshop, you should open and fill out the Student Notebooks below --- the Master Notebook is the same as the Student Notebook but has the answers to all of the exercises filled in. Feel free to review the Master Notebooks if you're stuck or if you are reviewing the lessons outside of a workshop.

{% assign nbvurl = site.workshop_site | remove: 'http://' %}

*   Scientific Programming I: Logistic growth
    - Student Notebook: [Download](python1-student.ipynb), [View](http://nbviewer.ipython.org/url/{{nbvurl}}/lessons/python/python1-student.ipynb)
    - Master Notebook: [Download](python1-master.ipynb), [View](http://nbviewer.ipython.org/url/{{nbvurl}}/lessons/python/python1-master.ipynb)

*   Scientific Programming II: Analyzing bird counts
    - Student Notebook: [Download](python2-student.ipynb), [View](http://nbviewer.ipython.org/url/{{nbvurl}}/lessons/python/python2-student.ipynb)
    - Master Notebook: [Download](python2-master.ipynb), [View](http://nbviewer.ipython.org/url/{{nbvurl}}/lessons/python/python2-master.ipynb)
    - Data Tables: [Small table](birds_sm.csv), [Large table](birds_lg.csv)

*   Extra: Plotting
    - Master Notebook: [Download](matplotlib-master.ipynb), [View](http://nbviewer.ipython.org/url/{{nbvurl}}/lessons/python/matplotlib-master.ipynb)

Starting a Jupyter Notebook
---------------------------

To learn about these core concepts and the Python language, we'll start off by working within a Jupyter notebook. These notebooks are not just for teaching --- many scientists, myself included, use them as part of our "regular" software development process.

To start up a notebook, open a Terminal window and navigate to the folder containing the Jupyter notebook files that you wish to open. Once in the directory, run the command `jupyter notebook`, which will launch a 
local webserver and open your default browser. From there you can open an 
existing notebook, create a new notebook, and start working.

Note that if you are on a Windows machine, this command may not run under Git Bash. If it doesn't, open a Command Prompt (click on the Start menu and type `cmd` in the search box or click on Run then type `cmd`), navigate to the appropriate directory, then run the command `ipython notebook`.
