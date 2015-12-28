---
layout: page
root: ../..
title: Reproducible Workflows
---

Reproducible Workflows
======================

We're now in the home stretch of the workshop --- congratulations! Up to this point, we've talked about how to make your code efficient (good programming practices), accurate (testing), and maintainable (modularization + version control). Now we're going to talk about a final and very important concept known as reproducibility.

For our purposes, we can summarize the goal of reproducibility in two ways, one of which is a hard requirement and the other of which is an aspirational goal (sometimes, but not always, attainable).

First, as a hard requirement, you should always __have a complete chain of custody (i.e., provenance) from your raw data to your finished results and figures__. That is, you should _always_ be able to figure out precisely what data and what code were used to generate what result --- there should be no "missing links". If you have ever had the experience of coming across a great figure that you made months ago and having no idea how in the world you made it, then you understand why provenance is important. Or, worse, if you've ever been unable to recreate the results that you once showed on a poster or (gasp) published in a paper...

Second, as a more aspirational goal, I should be able to sneak into your lab late at night, delete everything except for your raw data and your code, and __you should be able to run a single command to regenerate EVERYTHING, including all of your results, tables, and figures in their final, polished form__. Think of this as the "push button" workflow. This is your ultimate organizational goal as a computational scientist. As an added bonus, if you couple this with a version control system that tracks changes over time to your raw data and your code, you will be able to instantly recreate your results from any stage in your research (the lab presentation version, the dissertation version, the manuscript version, the Nobel Prize committee version, etc.). Wouldn't that be nice?

In practice, the aspirational, push button goal will be achievable for nearly all of your research projects with one key exception, which are projects that require the use of a proprietary software tool somewhere along the line that only has a graphical interface. In this case, you should still focus on making as much of your workflow as automated as you can. For the portion of the research that cannot be easily automated, carefully document exactly what version of the software you used, what exact menu options that you checked, what data you used for input, and where the output was saved. You will often be able to achieve a sort of modifed push button workflow in which you push one button to do some work, then follow a carefully described manual procedure in the middle, then push another button to finish generating the output.

In many simple research projects, including the example project that we've built in this workshop, a fully automated push button workflow is not only possible but relatively easy to construct. This lesson will illustrate the basic steps needed to achieve this:

1.  Create a clear and useful directory structure for our project.
2.  Set up (and use) Git to track our changes.
3.  Add the raw data to our project.
4.  Write the core "scientific code" to perform the analysis, including tests.
5.  Create a "runall" script to generate results for our specific project.
6.  Push the button and watch the magic.

One final note --- the workflow that we're following here is just a suggestion. Organizing code and data is an art, and a room of 100 scientists will give you 101 opinions about how to do it best. Consider the below a useful place to get started, and once you've become comfortable with this basic outline, don't hesitate to tinker and customize.

1\. Setting up the project directory
------------------------------------

As we've done throughout this workshop, let's create a project (a reasonably self-contained set of code, data, and results to answer a discrete scientific question) that will analyze the number of birds counted during a field survey. We begin by creating a directory called `bird_project` in a convenient place on our hard drive (if you've completed the [version control lesson]({{page.root}}/lessons/git/), note that we're starting a new project directory here, which will be organized and managed more comprehensively than the example in that lesson).

Now, within the `bird_project` directory, create four subdirectories (for bonus points, do this from the command line):

    .
    |-- data
    |-- man
    |-- results
    |-- src

The `data` directory will hold all of the raw data associated with the project, which in this case will be just a single large csv file containing data on the bird counts.

The `man` folder, short for manuscript, will (someday) contain the manuscript that we'll write describing the results of our analysis. You can consider this directory optional, as there are good arguments both for and against the practical value of putting your manuscripts under version control. I'd suggest at least trying it once to see if you feel that it makes your life easier. Note that if you write your manuscripts in a plain text format like LaTeX or Markdown (perhaps in concert with [pandoc](http://pandoc.org)), you will be able to use version control to diff and merge your manuscript drafts, which can be useful.

Finally, the `results` folder will contain the results of our analysis, including both tables and figures, and the `src` directory will contain all of our code used to perform the analysis.

In a more complex project, each of these directories may have additional 
subdirectories to help keep things organized.

2\. Initialize a Git repository
-------------------------------

Since we want to use version control to track the development of our project, we'll start off right away by initializing an empty Git repository within this directory. To do this, open a terminal window, navigate to the main `bird_project` directory, and run the command `git init`.

As you add things to the project directory, and modify old things, you'll want to frequently commit your changes, as we discussed in the Git tutorial.

3\. Add raw data
----------------

Often, we start a project with a particular data file, or set of data files. In this case, we have the file `birds_lg.csv`, which contains the records that we want to analyze. If you don't have it already, download this file [here](birds_lg.csv) and place it in the `data` subdirectory.

Now we reach an interesting question --- should the files in your `data` directory be placed under version control (i.e., should you `git add` and `git commit` these files)? Although you might automatically think that this is necessary, in principle our raw data should never change --- that is, there's only one version (the original version!), and it will never be updated (any modified versions of our data are considered a "result"). As a result, it's not necessarily useful to place this file under version control for the purpose of tracking changes to it.

A reasonable rule of thumb for getting started is that if the file is realatively small (ours is < 100k), go ahead and commit it to the tit repository, as you won't be wasting much hard disk space. Additionally, the file will then travel with your code, so if you push your repository to GitHub (for example) and one of your collaborators clones a copy, they'll have everything they need to generate your results.

However, if your file is realatively large AND is backed up elsewhere, you might want to avoid making a duplicate copy in the `.git` directory.

In either case, you'll want to ensure that every one of your data files has some sort of metadata associated with it to describe where it came from, how it got to you, the meaning of the columns, etc. There are many formats for metadata that vary from simple to very complex. Ecologists, for example, have a standard known as [Ecological Metadata Language](http://knb.ecoinformatics.org/software/eml/) standards and a tool [Morpho](http://knb.ecoinformatics.org/morphoportal.jsp) for creating metadata files. For your own private work, make sure that, at a minimum, you create a `README.txt` file that describes your data as best you can.

Copy and paste the text below into a `README.txt` file and place it in the data subdirectory. Remember that this is a bare-bones description --- in your own work, you'll want to include as much information as you have.

	Data downloaded from North American Breeding Bird Survey web interface at http://www.pwrc.usgs.gov/BBS/RawData/ on December 5, 2015. Table contains summary species counts for California.

At this point, your project directory should look like this:

	.
    |-- data
    |   |-- birds_lg.csv
    |   |-- README.txt
    |-- man
    |-- results
    |-- src

Commit both the data and README files to your git repository.

What about the case in which your raw data is hosted elsewhere, on a SQL server, for example, or a shared hard drive with your lab? Now your data is living somewhere else, and you don't necessarily have direct control over its provenance (what if someone changes it while you weren't looking?). In this situation, you should try to make your `runall.py` script (see below) make a copy of the metadata associated with the dataset (it does have metadata, doesn't it?), which hopefully will include something like a version number and a last-updated date, and store this along with your results. That way you'll at least have some information on the version of the data that was used. If there's no metadata, try to shame your collaborators into creating some. If all else fails, at least record the date on which your analysis was run so that, in principle, you could later try to find out what state the raw data was in on that date. If you're really nervous about the data changing, though, you might want to look into making yourself a local copy.

4\. Write code to perform analysis
----------------------------------

Now for the real work --- writing the code that will perform our analysis. As before, we'll separate the "scientific" part of our code, which does the conceptual heavy lifting of our analysis, from the more specific parts of the code that handle the logistics of running this particular, individual analysis.

In our case, the scientific "guts" of our code are found in the `analysis_functions.py` module AND, just as importantly, in the test file that we wrote to verify that the function in our module is working properly. So at this point, we can just copy the `analysis_functions.py` and `test_analysis_functions.py` into our `src` directory. If you don't have these handy, or if you didn't finish these exercises in the previous lesson, you can download a complete working copy of the module [here](analysis_functions-master.py) and the test file [here](test_analysis_functions-master.py). Note that these files have "-master" in their file names, to distinguish them from the ones that you may have created in previous lessons --- if you're going to use these downloaded versions going forward, you can remove the "-master" part from the file names.

Now we reach a small question, which is what to do with the `birds_sm.csv` data table (you can get it [here](birds_sm.csv) if you don't have it handy). This is technically data, but it is also only used for our module testing, not for our final analysis. While it might seem that this should live in the `data` directory, what if (as is often the case) the data in `birds_sm.csv` was actually fake data that was set up in a particular way to test our module? There's thus some argument to put it in the `src` directory along with the test file. I've seen reasonable people take both approaches --- here we'll also copy `birds_sm.csv` into our `src` directory to keep things easy, although feel free to move it to the data directory (note that if you move it, you'll have to modify the path to this data file that you previously put in your test file).

At this point, your project directory should look like this:

    .
    |-- data
    |   |-- birds_lg.csv
    |   |-- README.txt
    |-- man
    |-- results
    |-- src
    |   |-- birds_sm.csv
    |   |-- analysis_functions.py
    |   |-- test_analysis_functions.py

Make sure that you commit these three new files (your module, test file, and test data set) to your git repository. You can commit these together, or separately if you think it would be useful to add a different commit message for the different files. At this stage, you might want to run `nosetests` again in the `src` directory to make sure everything is working.

Now, of course, that copying and pasting in a completed module is not the normal workflow for this step. Normally, you'd spend days/weeks/months working in the `src` directory, writing code and tests, generating intermediate results, looking at the results, writing new code and tests, generating new results, etc. This iterative cycle isn't unlike writing a paper --- you spew out a draft that's not so bad (but also not so good), then go back and revise it, then spew out some new material, revise that, etc.

At this point, it's worth taking a moment to discuss how you might approach this iterative software development cycle. Below are two possible suggestions, although the "stack" that one chooses to use is very much a personal preference.

One strategy is to simultaneously work on three files at once --- a module like `analysis_functions.py`, a file to test the functions in your module like `test_analysis_functions.py`, and a third script that calls various functions from your module and runs them so that you can see whether your code is doing what you want it to do. I sometimes call this `scratch.py` or something like that, and fill up my terminal window with hundreds of lines of `python scratch.py` as I modify my code and look at the results that are saved, results that are printed to the terminal window, and errors that pop up.

Conversely, you could replace the scratch file with a cell in a Jupyter notebook that serves the same function. if you do this, you should put the line `reload(my_module)` under the line `import my_module` in the cell to make sure that any changes you make in the module are re-imported into your notebook when you run a cell.

Another strategy is to take advantage of the Jupyter notebook more fully, and , write your code in individual cells, executing each one sequentially, 
making sure each cell executes properly, and review the values of variables after each step. This can be great and efficient in the event that you really don't have any idea what your final code will look like. The downside here is that, at the end, you'll be left with one enormous notebook file (probably without unit tests), and you'll need to go back at the end to properly modularize your code into functions and separate files, similar to the structure that we're using in this exercise, so that you can have a fully reproducible workflow. Plus you may end up writing your unit tests at the end rather than iteratively with your code as you go. All that said, though, this is particularly useful strategy if you think you need to feel your way around for a while. Note that the new Jupyter notebooks work with many programming languages, including R, and you can thus use this same process for code development in other languages.

5\. The runall script
---------------------

Now that we have our core functions and tests in place, it's time to implement the "button" for our push-button workflow --- the `runall.py` script. Once again, we've already created this file in a previous lesson (download it [here](runall-master.py) if you don't have your own copy handy, and remove the "-master" part from the file name), so you can just copy this file into your `src` directory.

As a reminder, the idea of the `runall` script is to collect all of the "wrapper" code that's needed to run this particular analysis into a single file. When you execute this file with the command `python runall.py`, it will fill in your previously empty results directory with the output of our analysis (in this case, a table and a plot).

To make our `runall` script look for data in the `data` directory and save our output in the `results` directory, rather than in the same directory as the script, modify these three lines

    birds_df = pd.read_csv('birds_lg.csv', index_col='Species')
    ...
    results_df.to_csv('birds_results.csv')
    ...
    fig.savefig('birds_results.pdf') 

to instead read

    birds_df = pd.read_csv('../data/birds_lg.csv', index_col='Species')
    ...
    results_df.to_csv('../results/birds_results.csv')
    ...
    fig.savefig('../results/birds_results.pdf')

You should recognize this syntax from our shell lesson as providing a relative path from the `src` directory to the `data` and `results` directories (remember that the `..` syntax means "go up one level").

After making these two changes, commit the `runall` script to your git repo.

6\. Run the push button analysis
--------------------------------

Now with everything in place, we're ready for the magic. Execute `python runall.py` from your `src` subdirectory and marvel at your results!

Now, here's the fun part. __Delete the files in your results directory.__ (Was that scary?) And then run the `runall` script again and marvel at your fully reproducible workflow! This "delete and rerun" strategy actually comes up in real life --- if you've been making a lot of changes to your code, and aren't quite sure what's in your `results` directory, you may want to periodically clear out this folder and re-run everything to make sure that everything is regenerating properly.

For extra credit, delete everything in your `src` folder too. Once it's gone, try running the command `git reset --hard` and see what happens. Can you figure out what this command means?

At this point, your directory should look like the below.

	.
    |-- data
    |   |-- birds_lg.csv
    |   |-- README.txt
    |-- man
    |-- results
    |   |-- birds_result.csv
    |   |-- birds_result.png
    |-- src
    |   |-- birds_sm.csv
    |   |-- mean_sightings.py
    |   |-- runall.py
    |   |-- test_mean_sightings.py

At this point, a natural question to ask is whether you need to add the contents of your `results` directory to your git repository. The answer should be obvious --- you do not need to do this, since the files in your `results` directory contain no unique information on their own. Everything you need to create them is contained in the `data` and `src` directories. One exception to this, though, might be if your analysis takes a very long time to run and the outputs are fairly small in size, in which case you may want to periodically commit (so that you can easily recover) the results associated with "intermediate" versions of your code.

While many of your projects will be nearly this simple, some will be more complex, sometimes significantly so. You will eventually come across the need to deal with modules that are shared across multiple projects, running the same analysis on multiple sets of parameters simultaneously, running analyses on multiple computers, etc. While we don't have time to go into these extra bits in detail, feel free to ask the instructors about any specific issues that you expect to encounter in the near future.

And that just about does it. Good luck!
