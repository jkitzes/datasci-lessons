---
layout: lesson
root: ../..
title: Creating a Reproducible Workflow
---

Introduction
------------

We're now in the home stretch of the workshop - congratulations! Up to this 
point, we've talked about how to make your code efficient (good programming 
practice), accurate (testing), and maintainable (modularization + version 
control). Now we're going to talk about a final and very important concept 
known as reproducibility. Victoria Stodden has written extensively about the 
idea of reproducibility in scientific software - you may want to look up [some 
of her papers](http://www.stanford.edu/~vcs/Papers.html) for reference.

For our purposes, we can summarize the goal of reproducibility in two related 
ways, one technical and one colloquial.

In a technical sense, your goal is to __have a complete chain of custody (ie, 
provenance) from your raw data to your finished results and figures__. That is, 
you should _always_ be able to figure out precisely what data and what code 
were used to generate what result - there should be no "missing links". If you 
have ever had the experience of coming across a great figure that you made 
months ago and having no idea how in the world you made it, then you understand 
why provenance is important. Or, worse, if you've ever been unable to recreate 
the results that you once showed on a poster or (gasp) published in a 
paper...

In a colloquial sense, I should be able to sneak into your lab late at night, 
delete everything except for your raw data and your code, and __you should be 
able to run a single command to regenerate EVERYTHING, including all of your 
results, tables, and figures in their final, polished form__. Think of this as 
the "push button" workflow. This is your ultimate organizational goal as a 
computational scientist. Importantly, note that this rules out the idea of 
manual intervention at any step along the way - no tinkering with figure axes 
in a pop-up window, no deleting columns from tables, no copying data from one 
folder to another, etc. All of that needs to be fully automated.

As an added bonus, if you couple this with a version control system that tracks 
changes over time to your raw data and your code, you will be able to instantly 
recreate your results from any stage in your research (the lab presentation 
version, the dissertation version, the manuscript version, the Nobel Prize 
committee version, etc.). Wouldn't that be nice?

To illustrate these ideas, we'll set up a small but realistic research project 
that follows a reproducible workflow. Just like you would in your own research 
projects, we'll go through the following key steps:

1.	Create a clear and useful directory structure for our project.
2.	Set up (and use) Git to track our changes.
3.	Add the raw data to our project.
4.	Write the core "scientific code" to perform the analysis, including tests.
5.  Create a "runall" script to generate results for our specific project.
6.	Push the button and watch the magic.

One final note - the workflow that we're following here is just a suggestion. 
Organizing code and data is an art, and a room of 100 scientists will give you 
101 opinions about how to do it best. Consider the below a useful place to get 
started, and don't hesitate to tinker and branch out as you get a better feel 
for this process. You also might want to review [William Noble's 
paper](http://dx.doi.org/10.1371/journal.pcbi.1000424) on this topic for more 
ideas.

1.	Setting up the project directory
------------------------------------

Let's create a project (a reasonably self-contained set of code, data, and 
results to answer a discrete scientific question) that will count the animals 
sighted in two years of camera trap surveys. We begin by creating a directory 
called `camera_analysis` in a convenient place on our hard drive. You might 
want to create a main directory called `Projects` or `Research` in your home 
folder or in your Documents folder to hold the directories for all of your 
individual research projects.

Now, within the `camera_analysis` directory, create four subdirectories:

    .
    |-- data
    |-- man
    |-- results
    |-- src

The `data` directory will hold all of the raw data associated with the project, 
which in this case will be just a single large csv file containing data on the 
animal sightings. The `man` folder, short for manuscript, will (someday) 
contain the manuscript that we'll write describing the results of our analysis 
(you were planning on using version control for your manuscript too, weren't 
you?). The `results` folder will contain the results of our analysis, including 
both tables and figures, and the `src` directory will contain all of our code.

In a more complex project, each of these directories may have additional 
subdirectories to help keep things organized.

For bonus points, do this all from the command line.

2.	Initialize a Git repository
-------------------------------

Since we want to use version control to track the development of our project, 
we'll start off right away by initializing an empty Git repository within this 
directory. To do this, open a Terminal window, navigate to the main 
`camera_analysis` directory, and run the command `git init`.

As you add things to the project directory, and modify old things, you'll want 
to frequently commit your changes as we discussed in the Git tutorial.

3.	Add raw data
----------------

Often, we start a project with a particular data file, or set of data files. In 
this case, we have the file `sightings_tab_lg.csv`, which contains the records 
that we want to analyze. Download this file [here](sightings_tab_lg.csv) and 
place it in the `data` subdirectory.

Now we reach an interesting question - should your `data` directory be placed 
under version control (ie, should you `git add` and `git commit` these files)? 
Although you might automatically think that this is necessary, in principle our 
raw data should never change - that is, there's only one version (the original 
version!), and it will never be updated. As a result, it's not necessarily 
useful to place this file under version control for the purpose of tracking 
changes to it.

A reasonable rule of thumb for getting started is that if the file is 
realatively small (ours is < 100k), go ahead and commit it to the Git 
repository, as you won't be wasting much hard disk space. Additionally, the 
file will then travel with your code, so if you push your repository to Github 
(for example) and one of your collaborators clones a copy, they'll have 
everything they need to generate your results.

However, if your file is realatively large AND is backed up elsewhere, you 
might want to avoid making a duplicate copy in the `.git` directory.

In either case, you'll want to ensure that every one of your data files has 
some sort of metadata associated with it to describe where it came from, how it 
got to you, the meaning of the columns, etc. There are many formats for 
metadata that vary from simple to very complex. If you're interested in 
following good ecological best practices, you may want to review the 
[Ecological Metadata Language](http://knb.ecoinformatics.org/software/eml/) 
standards and the tool [Morpho](http://knb.ecoinformatics.org/morphoportal.jsp) 
for creating metadata files. For your own private work, make sure that, at a 
minimum, you create a `README.txt` file that describes your data as best you 
can.

Copy and paste the text below into a `README.txt` file and place it in the data 
subdirectory. Remember that this is a bare-bones description - in your own 
work, you'll want to include as much information as you have.

	Data received via email on April 1, 2013 from Professor Smith. Includes 
	records from camera trap surveys conducted by John Doe and Jane Doe from 
	2011-2012. Method of collection, site locations, and additional 
	descriptions are found in John Doe's dissertation, Chapter 3 Appendix, 
	filed August 2012 at UC Berkeley.

At this point, your project directory should look like this:

	.
    |-- data
    |   |-- README.txt
    |   |-- sightings_tab_lg.csv
    |-- man
    |-- results
    |-- src

Commit both the data and README files to your git repository.

What about the case in which your raw data is hosted elsewhere, on a SQL 
server, for example, or a shared hard drive with your lab? Now your data is 
living somewhere else, and you don't necessarily have direct control over its 
provenance (what if someone changes it while you weren't looking?). In this 
situation, you should try to make your `runall.py` script (see below) make a 
copy of the metadata associated with the dataset (it does have metadata, 
doesn't it?), which hopefully will include something like a version number and 
a last-updated date, and store this along with your results. That way you'll at 
least have some information on the version of the data that was used. If 
there's no metadata, try to shame your collaborators into creating some. If all 
else fails, at least record the date on which your analysis was run so that, in 
principle, you could later try to find out what state the raw data was in on 
that date. If you're really nervous about the data changing, though, you might 
want to look into making yourself a local copy.

4. Write code to perform analysis
---------------------------------

Now for the real work - writing the code that will perform our analysis. We'd 
like to generate two outputs. First, we want to make and save a table that 
contains a column with the names of the four mammalian carnivores found in our 
data set - Fox, Wolf, Grizzly, and Wolverine - and a second column that 
contains the total number of records associated with each species. Second, we'd 
like to create and save a simple histogram that shows this result visually.

### Modules

We've already done the work of writing much of this code earlier today, so at 
this point, we can simply copy and paste the file `mean_sightings.py` that you 
created earlier in the testing lesson into your `src` subdirectory. Or you can 
download a complete copy of this file [here](mean_sightings-full.py), making 
sure to delete the "-full" from the end of the file name.

Note that, by itself, the code in our `mean_sightings.py` file doesn't actually 
generate any results for us - this file just contains the core functions that 
we have written to perform our analysis. Later on, we'll write a small 
`runall.py` script that imports these core functions and generates our results 
for this particular project. In small projects, you can combine these two 
files, but it's good practice to keep your actual analysis code in a separate 
module where it can easily be tested and reused later on. This separation of 
files also supports a mental separation of roles - the module is where you 
write and test the guts of your code (the stuff that "does science") whereas 
the `runall` script is just the few lines that take this "science" and applies 
it to your particular data set to generate your particular results (the stuff 
that spits out "these results"). If you wanted to perform the same analysis on 
a different data set or with a different set of input parameters, for example, 
you should be able to accomplish that by modifying just the `runall` file that 
we'll discuss later.

Note, of course, that copying and pasting in a completed module is not the 
normal workflow for this step. Normally, you'd spend days/weeks/months working 
in the `src` directory, writing code and tests, generating results, looking at 
the results, writing new code and tests, generating new results, etc. This 
iterative cycle isn't unlike writing a paper - you spew out a draft that's not 
too bad, then go back and revise it, then spew out some new material, revise 
that, etc.

Different people have different favorite approaches and tools for this 
iterative cycle.

One strategy is to simultaneously work on three files at once - a module like 
`mean_sightings.py`, a file to test the functions in your module like 
`test_mean_sightings.py`, and a third script that calls various functions from 
your module and runs them so that you can see whether your code is doing what 
you want it to do. I sometimes call this `scratch.py` or something like that, 
and fill up my Terminal window with hundreds of lines of `python scratch.py` as 
I modify my code and look at the results that are saved, results that are 
printed to the Terminal window, and errors that pop up.

Another strategy is to take advantage of the IPython notebook, where you can 
write your code in individual cells and easily execute each one sequentially, 
make sure each cell executes properly, and review the values of variables after 
each step. This can be great and efficient in the event that you really don't 
have any idea what your final code will look like. The downside here is that, 
at the end, you'll be left with one enormous notebook file (probably without 
unit tests), and you'll need to go back at the end to properly modularize your 
code into functions and separate files, similar to the structure that we're 
using in this exercise, so that you can have a fully reproducible workflow. 
Plus you may end up writing your unit tests at the end (you are going to write 
them, aren't you?) rather than iteratively with your code as you go. All that 
said, though, this is a great strategy if you think you need to feel your way 
around for a while.

### Documentation

Documentation is an important part of creating a reproducible workflow - rather 
than simply reproducing results, you can think of documentation as helping you 
to reproduce the thought process that led you to design your code in a 
particular way. Being able to call up and recreate the thought process that led 
to your code is imporant both for "future you", who will eventually come back 
to this code in other projects, or at a minimum when writing the manuscript for 
this project, and for other users who might need to apply or maintain your code 
in the future.

Every programming language has its own guidelines and style for documentation - 
regardless of what language you're using, I'd suggest Googling something like 
"<my language name> style guide", and similar strings, to read about common 
conventions for that language. Below, we'll briefly discuss documentation in 
the context of Python modules, but a similar high-level conceptual framework 
will apply to any language.

In short, I would suggest mentally dividing your documentation into four basic 
levels, ranging from the smallest to the broadest scale.

#### 1. Line-level comments

At the smallest scale are line-by-line comments on your code, such as

    # If animal is not present, set mean counts per sigting to zero
    if totalrecs == 0:
        meancount = 0
    else:
        meancount = np.mean(tab['Count'][isfocus])

Code comments such as these should generally be restricted to one line, 
although two or three lines would be OK for cases that require more 
explanation. Most importantly, comments should __describe what the code is 
intended to do and why__, not simply repeat literally what the code does. The 
above comment, for example, explains the purpose of the subsequent lines. In 
contrast, the comment below is basically useless, as it simply repeats what 
anyone reading the code could have already told you.

    # Set x to zero
    x = 0

A better option would be

    # Initialize running count of individuals
    x = 0

There's an art to determining how many comments are too many. I tend to 
personally be quite verbose with my comments, as I tend to use comments as 
markers to help me find the sections of my code that perform particular 
conceptual steps. Most of my code thus has a comment every three to five lines 
or so, although some would find this excessive.

Finally, make sure not to let your comments get out of date - when you update 
your code, you __must__ update the corresponding comments. An out of date or 
incorrect comment is worse than no comment at all.

If you haven't done so already, open your `mean_sightings.py` file and add a 
few code comments.

#### 2. Function-level definitions

All languages have conventions surrounding how to document the operations of a 
function. We've see lots of function definitions throughout this bootcamp 
whenever we looked up how to use a function like `np.array` (recall that you 
can call `np.array?` from an IPython notebook, for example, to see its function 
definition). In Python, a description of a function is known as a docstring. 
Many scientific Python packages use a convention similar to the below.

    def get_sightings(filename, focusanimal):
        """
        Get number of sightings of a focus animal in a data set.

        Parameters
        ----------
        filename : str
            Path to file containing sightings data
        focusanimal : str
            Name of focus animal (not case sensitive)

        Returns
        -------
        result : tuple
            Tuple containing total count of number of focus animal seen and mean
            count of individuals per sighting event.

        Notes
        -----
        Data file must be csv format with Animal and Count columns containing
        animal name and count of individuals per sighting, respectively.

        """

Note a few important features of this docstring. First, it's indented, just 
like all of the other code within a function. Second, it starts immediately 
after the line defining the function, and starts and ends with three quotation 
marks (which, in Python, defines a multi-line string). Third, the first line of 
the docstring is a single line describing the high level purpose and/or 
function of the function. The rest of the docstring structure is not as 
standardized, but the above example is a basic form that's common in scientific 
Python packages.

As we previously discussed, a nice feature of docstrings is that they integrate 
nicely into the ways of getting help in IPython, for example, as well as with 
other documentation tools such as Sphinx that we'll mention later. See 
[PEP257](http://www.python.org/dev/peps/pep-0257/) for some additional 
information and standards for docstrings.

If you haven't already, add a nice docstring to your function(s) in 
`mean_sightings.py`.

#### 3. Module-level documentation

At a higher level, you should also provide some overarching documentation of 
each of your Python module files. This is usually a relatively short summary, 
compared to a function-level docstring, that states the purposes of the module 
and lists what the module contains.

    #!/usr/bin/env python

    """
    Module containing functions to calculate mean number of sightings of a given
    animal in a given sightings csv file.

    Functions
    ---------
    get_sightings - get number of sightings of focus animal in data set

    """

As with function docstrings in Python, a module docstring is set off by triple 
quotes and appears at the very top of the module.

If you haven't already, add a short module docstring to `mean_sightings.py`.

#### 4. Package-level and user documentation

At the highest level of documentation, we find information that is intended 
(mostly) to be read by users of your code to gain an overview of everything 
that your code does. We won't talk about this level in detail, as it only 
matches the other three levels in importance for larger projects that are 
shared widely and maintained on an ongoing basis (which may not apply to many 
of your research projects). If you are interested in learning more about this 
process for Python packages, I'd suggest having a look at 
[Sphinx](http://sphinx-doc.org/), which is the tool used to create 
documentation for Python itself as well as most of the main scientific 
packages. The websites documenting [core Python](http://docs.python.org/2/), 
[matplotlib](http://matplotlib.org/), and 
[numpy](http://docs.scipy.org/doc/numpy/) provide some useful examples of 
Sphinx in use as well as some general documentation styles that you might wish 
to review.

### Testing

OK, back to our project. We now have the file `mean_sightings.py` in our `src` 
directory. Now copy in your file `test_mean_sightings.py`, which contains the 
unit tests that you wrote for the functions in `mean_sightings.py` (or download 
a copy [here](tes_mean_sightings_full.py), making sure to change the file name 
to start with "test").

You may recall that our test functions made use of a small data set, 
`sightings_tab_sm.csv` (which you can download [here](sightings_tab_sm.csv) if 
you need to), that we created specifically for the purpose of testing our code. 
It can be a bit awkward deciding where to place this csv file - you could 
potentially put it in `data`, or here in the `src` directory, or perhaps in a 
subdirectory of `src` called `tests` or something like that. This is somewhat a 
matter of personal preference - for now, just copy and paste it here into the 
`src` directory (even though it's not technically code). You may want to create 
a readme file for this test data set as well so that you can remember how you 
created it.

Just to be sure we did everything right, go ahead and run `nosetests` from the 
Terminal and make sure that your functions still pass. If they don't for some 
reason, you can try to debug your function or just cheat by copying the master 
`mean_sightings.py` and test files linked above into your `src` directory. Be 
sure to remove the `-full` portion of the file names and to add a second `t` to 
the word `test` in the second file name if you do this.

At this point, your project directory should look like this:

	.
    |-- data
    |   |-- README.txt
    |   |-- sightings_tab_lg.csv
    |-- man
    |-- results
    |-- src
    |   |-- mean_sightings.py
    |   |-- sightings_tab_sm.csv
    |   |-- test_mean_sightings.py

Add and commit these three new files (your module, test file, and test data 
set) to your git repository. You can commit these together, or separately if 
you think it would be useful to add a different commit message for the 
different files.

5. The runall script
--------------------

Now that we have our core functions and tests in place, it's time to create the 
"button" for our push-button workflow - the `runall.py` script. The idea is 
that you will be able to start with an empty results directory, execute the 
line `python runall.py` in Terminal, and have our table and figure saved in the 
`results` directory.

Create a new text file called `runall.py` and copy and paste the following code 
into it.

	#!/usr/bin/env python

	'''
	Script to create all results for camera_analysis project.
	'''

	import numpy as np
	import matplotlib.mlab as ml
	import matplotlib.pyplot as plt
	from mean_sightings import get_sightings


	# ------------------------------------------------------------------------
	# Declare variables
	# ------------------------------------------------------------------------

	# Set paths to data and results directories. Note that this method of
	# relative paths only works on *nix - for Windows, see os.path module.
	data_dir = '../data/'
	results_dir = '../results/'

	# Set name of data file, table, and figure
	data_name = 'sightings_tab_lg.csv'
	table_name = 'spp_table.csv'
	fig_name = 'spp_fig.png'

	# Set names of species to count
	spp_names = ['Fox', 'Wolf', 'Grizzly', 'Wolverine']


	# ------------------------------------------------------------------------
	# Perform analysis 
	# ------------------------------------------------------------------------

	# Declare empty list to hold counts of records
	spp_recs = []

	# Get total number of records for each species
	for spp in spp_names:
		totalrecs, meancount = get_sightings(data_dir + data_name, spp)
		spp_recs.append(totalrecs)

	print spp_names
	print spp_recs

We won't go over this code in too much detail, as you should now have the 
background to understand what's happening on your own. Right up front, after 
importing the necessary modules, we have set up variables that define the 
locations of the `data` and `results` directories (relative to the `src` 
directory where our `runall.py` file is located) as well as the names of our 
input data file and the table and figure that we will create. We also declared 
the list of species names here. The purpose of declaring these variables up 
front, rather than just typing these names into the code later on where they 
appear, is to make it easy to change these later on if, for example, we want to 
analyze a different set of species or use a different data file.

After those declarations, we simply set up a `for` loop that goes through each 
of our species names and uses our previously-written function to get the number 
of records for that species. At the very end, we print out the lists of species 
names and records just to have a look at the output.

Now, go back to your Terminal window, navigate to the `src` directory, and run 
the command `python runall.py`. You should see the species names and records 
printed in your Terminal window - this shows that our code is running without 
errors to this point.

Now let's add some code to save the table. Erase the print lines from the 
bottom of `runall.py`, and add the text below.

	# ------------------------------------------------------------------------
	# Save results as table 
	# ------------------------------------------------------------------------

	# Put two lists into a recarray table
	table = np.array(zip(spp_names, spp_recs),
					 dtype=[('species', 'S12'), ('recs', int)])

	# Save recarray as csv
	ml.rec2csv(table, results_dir + table_name)

This code simply takes our two lists, the list of species names and of records, 
and creates a record array from them. The syntax to do this might seem 
confusing, and at this point, it's probably just best to start by memorizing it 
as the "recipe" that one uses to turn several lists into a record array. The 
`dtype` variable is used to name each "column" in our recarray and to tell 
Python the format of each column. The first column, called 'species', is given 
the format 'S12', which means a string of up to 12 characters. The second 
column, recs, is given the format int, which stands for an integer. We then use 
a helper function from `mlab` to save our recarray as a csv file.

Once again, go back to your Terminal window and execute this file. Check to see 
that the csv file was correctly created and saved in the `results` directory.

Last but not least, let's add some code to make and save a bar chart that 
visually displays the data that's in our table. Add the code below to the 
runall file.

	# -----------------------------------------------------------------------
	# Save results as figure 
	# -----------------------------------------------------------------------

	# Set up figure with one axis
	fig, ax = plt.subplots(1, 1)

	# Create bar chart: args are location of left edge, height, and width of bar
	ax.bar([0,1,2,3], spp_recs, 0.8)

	# Place tick marks in center of each bar
	ax.set_xticks([0.4, 1.4, 2.4, 3.4])

	# Set limits to give some white space on either side of first/last bar 
	ax.set_xlim([-0.2, 4])

	# Add species names to x axis
	ax.set_xticklabels(spp_names)

	# Save figure
	fig.savefig(results_dir + fig_name)

This code does just what the comments say that it does. The resulting figure 
looks OK, and you would probably want to spend more time adding additional 
lines here to adjust the formatting.

Don't forget to add `runall.py` to your git repo.

6. Run the push button analysis
-------------------------------

Now with everything in place, we're ready for the magic. Just for good measure, 
delete any files that are hanging around in your `results` directory. Then, 
execute `python runall.py` from your `src` subdirectory and marvel at your 
fully reproducible workflow! (If you've been making a lot of changes to your 
code, and aren't quite sure what's in your `results` directory, you may want to 
periodically clear out this folder and re-run everything to make sure that 
everything is regenerating properly.)

At this point, your directory should look like the below.

	.
    |-- data
    |   |-- README.txt
    |   |-- sightings_tab_lg.csv
    |-- man
    |-- results
    |   |-- spp_table.csv
    |   |-- spp_fig.png
    |-- src
    |   |-- mean_sightings.py
    |   |-- runall.py
    |   |-- sightings_tab_sm.csv
    |   |-- test_mean_sightings.py

At this point, a natural question to ask is whether you need to add the 
contents of your `results` directory to your git repository. The answer should 
be obvious - you do not need to do this, since the files in your `results` 
directory contain no unique information on their own. Everything you need to 
create them is contained in the `data` and `src` directories. One exception to 
this, though, might be if your analysis takes a very long time to run and the 
outputs are fairly small in size, in which case you may want to periodically 
commit (so that you can easily recover) the results associated with 
"intermediate" versions of your code.

While many of your projects will be nearly this simple, some will be more 
complex, sometimes significantly so. You will eventually come across the need 
to deal with modules that are shared across multiple projects, running the same 
analysis on multiple sets of parameters simultaneously, running analyses on 
multiple computers, etc. While we don't have time to go into these extra bits 
in detail, feel free to ask the instructors about any specific issues that you 
expect to encounter in the near future. Rest assuered that no matter how 
complicated your situation is, Python will provide you with a (relatively) 
efficient and robust way to accomplish your goals. 

And that just about does it. Good luck!
