---
layout: page
root: ../..
title: Modules and Testing
---

Modules and Testing
===================

Now that you understand the basics of programming in Python, we'll move on to discuss strategies for managing the code that you write. In this lesson, we'll cover four topics:

1. How to move your code out of the Jupyter notebooks that we've been using so far and into plain text files
2. How to create modules and scripts that separate the reusable, "conceptual" parts of your code from the code needed to execute a specific, individual analysis
3. How to use unit tests to evaluate the accuracy of the important functions that you write
4. How to systematically document the code that you write so that others, including you in the future, can understand what it does.

Before we get started, let's review the code that we'll use for this lesson, which comes from our earlier [Scientific Programming II]({{page.root}}/lessons/python/) lesson. In that lesson, we developed code to load a small data table of bird sightings, calculate the mean number of birds seen per present species, and save the results. By the final exercise in that lesson, we ended up with a cell in our notebook containing the following code:

~~~
import pandas as pd  # 1
  
birds_df = pd.read_csv('birds_sm.csv', index_col='Species')  # 2
    
def count_birds(birds_df):  # 3
    years = birds_df.columns
    results_df = pd.DataFrame(index=['Mean'], columns=years)  # 4

    for year in years:  # 5
        birds_this_year = birds_df[year]
        sum_counts = birds_this_year.sum()  # 6
        species_seen = (birds_this_year > 0).sum()
     
        if species_seen == 0:  # 7
            results_df[year] = 0
        else:
            results_df[year] = sum_counts / species_seen

    return results_df  # 8
    
results_df = count_birds(birds_df)  # 9
    
results_df.to_csv('birds_results.csv')  # 10
    
ax = results_df.T.plot()  # 11
fig = ax.get_figure()
fig.savefig('birds_results.pdf')
~~~

As a reminder, this code does the following (the numbers below correspond to the numbers in the comments in the code above):

1. Import the `pandas` module
2. Load a small data table as a data frame
3. Define a function that...
4. ... creates an empty results data frame
5. ... loops through each year in the input data frame and ...
6. ... ... calculates the number of species present and the total birds seen
7. ... ... stores either the mean birds per species or zero as the result for that year
8. ... returns the now filled out results data frame
9. Runs the function we just defined for the small data table
10. Saves the results data frame
11. Plots the results data frame and saves the plot

We'll use this code as a starting point for this lesson on modules and testing. If you haven't done so already, you'll need to download the file [birds\_sm.csv](birds_sm.csv) and make sure that it's in the same directory where you eventually save your code files.

1\. Putting code in plain text files
------------------------------------

Up to this point, we've written and executed all of our Python code in Jupyter notebooks. A notebook is a great way to try new things and to write prototype code, and some "advanced" data scientists use notebooks for their entire workflow. However, the more common means of structuring scientific software is to save your code in various plain text files and to run these files from the command line. We'll look at how to do this now.

To get started, open a plan text editor on your computer (you don't want to use `nano` for this exercise --- you'll want a fully fledged graphical editor). If you haven't downloaded a good plain text editor yet, you might try [Sublime Text](http://www.sublimetext.com/).

>### Exercise 1
>Using your editor, copy and paste the entire block of code above into a file called `runall.py`. Change the data table from `birds_sm.csv` to `birds_lg.csv`, since we're now interested in running our full analysis. See the notes below for some potential issues to avoid.

As you start to work with plain text code files, there are three important pitfalls to note. First, __be careful with file extensions__. Some editors will try to append something like `.txt` when you save a file --- you want to be sure that your files actually have the extension `.py` as shown above. Second, __watch out for indenting__. The code in these files should all be flush against the left margin of the editor, with indents used, as before, only for the for loop and the if statement. Third, __never use tabs__. You should always use spaces to indent code, with the standard size of an indent being four spaces. Most good text editors will have an option to automatically substitute spaces when you press the tab key (in Sublime Text, look at the bar at the bottom of the window, click on the words Tab Size, and check the option to indent using spaces).

At this point, we have a file that contains the same code that we had in a Jupyter notebook cell at the end of the Scientific Programming II lesson. In the notebook, we could press a button or use Ctrl-Enter to execute a cell. So how do we run the code contained in a file? We can actually do this quite easily from the command line.

<blockquote>
<h3>Exercise 2</h3>

<p>Open a terminal window and navigate to the directory holding your <code>runall.py</code> script. Make sure that it also contains the file <code>birds_sm.csv</code>. If you still have the results files <code>birds_results.csv</code> and <code>birds_results.pdf</code> in this directory from the previous lesson, delete them using <code>rm</code>. Then type the command <code>python runall.py</code> and hit Return. What happens?</p>

<p><strong>Bonus:</strong> Open your <code>runall.py</code> file and add a line to print the contents of the results data frame. Run the script again.</p>

<p><a href="#" onclick="var e = document.getElementById('answer2'); if(e.style.display == 'block') e.style.display = 'none'; else e.style.display = 'block'; return false;">Click to show/hide answer</a></p>

<div style="display: none;" id="answer2">If all goes well, you should see the results files, both the table and the plot, reappear in your directory. When you add the print statement, the lines that were previously printed below our cell in the Jupyter notebook are now printed at the command line itself.
</div>
</blockquote>

The statement `python my_file.py`, run at the command line, thus does the exact same thing as executing a cell, or several cells, in a Jupyter notebook containing the same code.

2\. Separating code into modules and scripts
--------------------------------------------

Now that you've seen how to get your code out of a notebook and into a plain text file, let's start thinking about how to organize your code into files. Perhaps the single most important advice that we can give you for managing your code is to _separate the reusable, conceptual parts of your code (the part that does the "science") from the code used to run a specific individual analysis_. There are at least three important reasons to do this:

1. It will make it easier for you to conceptualize what the different parts of your code does, and the different roles that they play in your research
2. It will allow you to more easily test the core scientific "guts" of your code
3. It will support your efforts to achieve reproducibility

Looking at the code that we've written above, which part is the scientific "guts" and which part is specific to this analysis? Sometimes, as in this case, it's fairly obvious --- here, the conceptual analysis part of the code occurs in the `count_birds` function, while the rest of the code loads and saves a particular data set.

(As an aside, you might argue that the loading and saving parts are actually conceptual as well, and that we should consider everything other than just picking the input data table to be part of the core scientific analysis. This is reasonable, and in this case, I would encourage you to refactor the function above so that you have a single function that takes in a path to the data file and then saves the result data frame and plots. You'll see later, though, that this design would make our code harder to test.)

Our task, then, is to separate our `count_birds` function from the rest of the code.

<blockquote>
<h3>Exercise 3</h3>

<p>Open your <code>runall.py</code> file and create a new file called <code>analysis_functions.py</code>. Cut the function <code>count_birds</code> out of <code>runall.py</code> and paste it into <code>analysis_functions.py</code>. At the top of this file, before the function, add the line <code>import pandas as pd</code>, since our function makes use of the <code>pandas</code> library.</p>

<p>Run the <code>runall.py</code> script again and you'll see an error. What's the problem? Can you fix it? (Hint: Think about how you tell your <code>runall.py</code> to find the <code>pandas</code> module, and then how you call a function within that module.)</p>

<p><a href="#" onclick="var e = document.getElementById('answer3'); if(e.style.display == 'block') e.style.display = 'none'; else e.style.display = 'block'; return false;">Click to show/hide answer</a></p>

<div style="display: none;" id="answer3">At the top of the file, add the line <code>import analysis_functions</code> (just like how we imported <code>pandas</code>). Then modify the line that calls the <code>count_birds</code> function so that it calls <code>analysis_functions.count_birds</code> (just like <code>pd.to_csv</code>, for example).

<p>This simple <code>import X</code> syntax will work so long as the file that is being imported is in the same directory as the file that is doing the importing (this is the case for all of our examples in this workshop). You can feel free to use the syntax <code>import X as Y</code> to pick a shorter name for your <code>analysis_functions</code> module.</p>
</div>
</blockquote>

At this point, we have two files: the file `analysis_functions.py` contains the scientific core of our analysis, the function `count_birds`, and the file `runall.py` contains the surrounding code that executes and saves the results from our particular data set analysis. Below we'll refer to the `analysis_functions.py` file as a module, which is the common term for a file containing functions that is designed to be imported, and we'll refer to `runall.py` as a script, the term for a file that is meant to be run itself.

3\. Testing functions in your modules
-------------------------------------

Now that we've separated our core, conceptual scientific code out into a module, we can start to think not about the technicalities of writing it, but the bigger picture question of "righting" it --- that is, how can we tell that our code is actually giving us the correct answer? As disciplinary scientists, we would never trust a lab measurement that we made with uncalibrated instruments. Similarly, as computational scientists, we shouldn't trust the results that our code gives us until we have tested it. 

In this lesson, we'll focus on unit tests, perhaps the most basic type of testing that we can run. Unit tests focus on a single "unit" of code, which in our case will be functions that we've written. We'll write tests to ensure that when our function is given a certain set of arguments as input, it generates output that we know to be correct. Once we have a complete test suite for a function, we can run the entire suite to make sure that all the tests pass (i.e., that our function gives the correct output for all the combinations of input that we have decided to test).

In our example, we'll focus on testing the `count_birds` in our `analysis_functions.py` module. Our strategy will be simply to give this function a data frame for which we can calculate the correct result by hand, and we'll make sure that the function gives us back this known correct answer. We can do this several times for different test data sets. If our function passes all of our tests, it gives us more confidence that if we run the function on a different data set, perhaps a huge one for which we can't verify the results by hand, we'll get an accurate result.

Although we won't discuss it explicitly here, testing has another huge mental benefit for the long-term maintenance and reuse of code, which is that if we make changes to the internals of our function, we can run our tests again to make sure that we haven't accidentally broken anything (this is known as a "regression"). This makes us more free to continue to improve the performance of our code over time, and helps avoid the dreaded "it's working, don't touch it" phenomena.

In this lesson, we're going to use the simple and very popular `nose` package to write and run our tests.

We'll start by creating a new text file called `test_analysis_functions.py`, which will hold our unit tests. At the top of this file, type (or copy) in the following lines to import `pandas`, `numpy` (an important scientific package that, among other things, contains some useful functions for testing), and our module:

    import pandas as pd
    import numpy as np
    import analysis_functions as af

Now, let's write our first test function, which will simply test to make sure that our function gives the right answer for the first year in our small data set. This is a very simple test which, if nothing else, will at least catch that the function runs at all, without giving an error, and that it gives a correct result for a very typical case.

Test functions (written for the `nose` testing package) can contain any type of Python code, like regular functions, but have a few key features. First, they don't take any arguments. Second, they contain at least one `assert` statement that compares two variables, the one calculated by our function and a correct one that we enter by hand.

The test function below load our small data table, uses `count_birds` to analyze it, and tests the result for 2010. Copy and paste this code into the `test_analysis_functions.py` file, below the import statements:

    def test_count_birds_small_table():
	    input_df = pd.read_csv('birds_sm.csv', index_col='Species')
	    results_df = af.count_birds(input_df)
	    np.testing.assert_array_equal(results_df['2010'], 24.5)

The first of the three lines in this test function reads in our small data table. The second line runs the `counts_birds` function on the table, and saves the resulting data frame as `results_df`. The third line uses a function from `numpy` to assert that the two arguments given to the function, here `results_df['2010']` and 24.5, are equal. There are a few different ways to write assert statements, but this function from `numpy` will work for all reasonably simple kinds of tests.

Note that we had to calculate the correct value for 2010, which is 24.5, by looking at the csv file manually. Make sure that you get this right. And resist the temptation to run the function, print the result, assume that it's correct, and then make a test based on that output --- you'll never catch a bug that way!

Now we're ready to run our suite of tests (so far, just this one test). Open a terminal window, and `cd` to the directory containing your Python files. Type `nosetests`, and examine the output. It should look something like this:

    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.238s

    OK

The dot on the first line indicates that we had one test, and that it passed. There is one character printed for each test. A '.' means the test passed, a 'F' means the test failed, and an 'E' means there was an error in the test function itself or in a function that it called.

Just for fun, try changing your test so that it fails (for example, assert that the answer for 2010 should be 30). What output do you see now? Don't 
forget to change the test back so that it passes after you're done.

In addition to reading in data, we could also have constructed the input data frame manually, which gives us an easy way to test and verify the behavior of our function under special circumstances (like only one species, or an empty input table). We can create a data table manually using the code below:

    input_df = pd.DataFrame([[1,2],[3,4]], index=['Sp1', 'Sp2'],
                            columns=['2010', '2011'])

This code uses the function `DataFrame` from the `pandas` library in order to create a new data frame called `input_df`. The first argument, which looks a bit funny, is just a list of lists (remember lists from the first scientific programming lesson?), which is how we can tell `pandas` that we want to make a two dimensional table. The second argument `index` tells the function what names we want to use for the index of the records (i.e., the names of the rows), and the third argument `columns` is a list of the names of the columns. Note that it's OK for the arguments to a function to appear on multiple lines.

It's not always obvious what a line of code like the above will actually do. To see it better, open a terminal window, navigate to your folder containing the Python lessons, and run the command `jupyter notebook`. Create a new notebook using the menu bar near the top of the screen. In that notebook, first import `pandas`, then copy the line of code above into a cell, run the cell, and then `print(input_df)`. This will show you what our manually created data frame actually looks like, and in particular what numbers have ended up in the rows and columns of the table.

<blockquote>
<h3>Exercise 4</h3>

<p>Here's another test function that looks a lot like the first, except that we've manually constructed our input data frame using the <code>pd.Dataframe</code> function.</p>

<pre><code>def test_count_birds_simulated_data():
    input_df = pd.DataFrame([[1,2],[3,4]],
        index=['Sp1', 'Sp2'], columns=['2010', '2011'])
    results_df = af.count_birds(input_df)
    np.testing.assert_array_equal(results_df, [[XXX, YYY]])</code></pre>

<p>Figure out what the number XXX and YYY should be in the final assert statement. Fill them in, then copy the entire test function into your <code>test_analysis_functions.py</code> file, and run <code>nosetests</code> again to make sure that this function also passes.</p>

<p><a href="#" onclick="var e = document.getElementById('answer4'); if(e.style.display == 'block') e.style.display = 'none'; else e.style.display = 'block'; return false;">Click to show/hide answer</a></p>

<div style="display: none;" id="answer4">The simulated data frame has rows for Sp1 and Sp2 and columns for 2010 and 2011. It has 1 and 3 in the 2010 column and 2 and 4 in the 2011 column. XXX and YYY are the expected values in the result array for these two years, so XXX is 2 and YYY is 3.
</div>
</blockquote>

<blockquote>
<h3>Exercise 5</h3>

<p>Recall that when we were writing the `count_birds` function, we had to be careful to specify what the function should do if there were no species seen in a particular year. Make a copy of the test function from the previous exercise, and using it as a starting point, design a test to ensure that the `<code>count_birds</code> function returns a result of zero for a year in which no birds of any species were seen. Add this third function to your test file and run <code>nosetests</code> again.</p>

<p><a href="#" onclick="var e = document.getElementById('answer5'); if(e.style.display == 'block') e.style.display = 'none'; else e.style.display = 'block'; return false;">Click to show/hide answer</a></p>

<div style="display: none;" id="answer5"><pre><code>def test_count_birds_simulated_data():
    input_df = pd.DataFrame([[0,2],[0,4]],
        index=['Sp1', 'Sp2'], columns=['2010', '2011'])
    results_df = af.count_birds(input_df)
    np.testing.assert_array_equal(results_df['2010'], 0)</code></pre>
</div>
</blockquote>

Of course, our `count_birds` function was relatively simple, and so there wasn't a whole lot of behavior to test. Many of the functions you write will take a number of different parameters as inputs, and you'll want to test several different combinations of them.

When designing tests, I'd recommend thinking in two steps. First, think about writing tests that will make sure that all possible behavior for your function is tested (that's why we wrote the test about species with zero counts above --- we want to verify all possible behavior). Second, think about how the arguments that you, or someone else, might give your function could cause it to break. Can you verify that it works correctly in these cases? Think in particular about boundary cases (what if an input argument is zero? What if it's huge?).

Although here we've written our function first and then our tests, this isn't the way that software development proceeds in reality. There's always an interaction between writing your code and its tests --- writing tests often highlights ways in which you need to modify your code, and modifying your code often adds new features that you know you should test. Both code and tests are thus best written at the same time. (There's also a school of thought called Test Driven Development, or TDD, that says that all of your tests should be written _first_, and that you should never actually write any production code until there's already a test to determine whether it works. This is an interesting ideal, if one that's difficult to follow in practice.)

4\. Documentation
-----------------

A final and very important part of managing your scientific code is writing useful documentation. First and foremost, good documentation will help you, and your collaborators, better understand and maintain your code. Documentation is also an important component of a reproducible workflow, which we'll discuss in the next lesson --- in the way that code helps to reproduce the results of your analysis, think of documentation as helping you reproduce the thought process that led you to write your code in a particular way.

Every programming language has its own particularguidelines and style for documentation --- regardless of what language you're using, I'd suggest Googling something like "SomeLanguage style guide" to read about common conventions. Below, we'll briefly discuss documentation in the context of Python code, functions, and modules, but a similar high-level conceptual framework will apply to any language.

In short, I would suggest mentally dividing your documentation into four basic levels, ranging from the smallest to the broadest scale.

### 1\. Line-level comments

At the smallest scale are line-by-line comments on your code, such as

    # If no species present, mean counts per species should be zero
    if species_seen == 0:
        results_df[year] = 0
    else:
        results_df[year] = sum_counts / species_seen

Code comments such as these should generally be restricted to one line, although two or three lines would be OK for cases that require more explanation. Most importantly, comments should __describe what the code is intended to do and why__, not simply repeat literally what the code does. The above comment, for example, explains the purpose of the subsequent lines. In contrast, the comment below is basically useless, as it simply repeats what anyone reading the code could have already told you.

    # Set x to zero
    x = 0

A better option would be

    # Initialize running count of individuals
    x = 0

There's an art to determining how many comments are too many. I tend to personally be quite verbose with my comments, as I tend to use comments as markers to help me find the sections of my code that perform particular conceptual steps. Most of my code thus has a comment every three to five lines or so, although some would find this excessive.

Finally, make sure not to let your comments get out of date --- when you update your code, you __must__ update the corresponding comments. An out of date or incorrect comment is worse than no comment at all.

>#### Exercise 6
>
>Open your `analysis_functions.py` module and add a few comments to various lines to help explain what's happening there.

### 2\. Function-level definitions

All languages have conventions surrounding how to document the operations of a function. In Python, a description of a function is known as a docstring. 
Many scientific Python packages use a convention similar to the below.

    def count_birds(birds_df):
        """
        Calculate mean number of birds per species present.

        Parameters
        ----------
        birds_df : DataFrame
            Table with species in rows and years in columns, values are counts

        Returns
        -------
        : DataFrame
            One row titled Mean for the result with column for each year
        """

Docstrings in Python begin and end with triple quotes, on their own lines, and they are indented just like the code that comes within the function.

Other than the specific syntax, two main features of this docstring apply to any scientific programming language. First, the first line of the function description is a single line describing the high level purpose and/or function of the function. Second, the inputs and outputs of the function are clearly described. If the function were more complex, it would also be common to include here an example of how it could be used.

>#### Exercise 7
>
>Copy the above docstring (feel free to modify it if you'd like) into your `count_birds` function.

### 3\. Module-level documentation

At a higher level, you should also provide some overarching documentation of each of your Python module files. This is usually a relatively short summary, compared to a function-level docstring, that states the purposes of the module and lists what the module contains.

    """
    Module containing functions to calculate mean number of sightings of 
    bird species.
    
    Functions
    ---------
    count_birds - Calculate mean number of birds per species present.
    
    """

Like function docstrings, a module docstring starts and ends with triple quotes. Module docstrings appear at the very top of your module file, above the import statements and any other Python code.

>#### Exercise 8
>
>Copy the above module documentation to the top of your `analysis_functions.py` module.

### 4. Package-level and user documentation

At the highest level of documentation, we find information that is intended (mostly) to be read by users of your code to gain an overview of everything that your code does. We won't talk about this level in detail, as it is most important for larger projects that are shared widely and maintained on an ongoing basis (which may not apply to many of your research projects). That said, even for relatively small projects, it never hurts to create a short document, or even a script, that shows off how your code can and should be used.

If you are interested in learning more about this process for Python packages, I'd suggest having a look at [Sphinx](http://sphinx-doc.org/), which is the tool used to create documentation for Python itself as well as most of the main scientific packages. The websites documenting [core Python](http://docs.python.org/2/), [matplotlib](http://matplotlib.org/), and [numpy](http://docs.scipy.org/doc/numpy/) provide some useful examples of Sphinx in use as well as some general documentation styles that you might wish to review.
