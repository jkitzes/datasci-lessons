---
layout: lesson
root: ../..
title: Version Control with Git
---

If you're like most scientists, you spend a fair amount of your "computer time" 
just trying to organize and keep track track of all of the files associated 
with your research projects. Among the many logistical headaches that you 
likely deal with on a daily basis are:

1.  Updating files, like scripts or papers, without losing copies of your old 
    version (Myfile\_2014\_01\_v2\_Sent\_Final\_FINAL\_Submitted.doc)

2.  Figuring out what changed between two versions of a file (When was the last 
    time I updated the regression model?)

3.  Maintaining multiple versions of files that started off the same but then 
    diverged (I need to make a lab meeting version and a poster version of 
    Figure 1, which are mostly the same but not exactly.)

4.  Merging two divergent copies of a file (I want to add the Figure 1 changes 
    from the poster into the file that makes the figures for my paper, but 
    without losing all of the new stuff that I've added to the latter file.)

5.  Sharing your files (and their history) with the world - or just a few 
    collaborators.

6.  Syncing versions of your project files across multiple computers and 
    collaborating with colleagues on projects.

We've all developed various habits and protocols that we use (consciously or 
unconsciously) to manage these issues. The usual practice is often some 
combination of nested folders, file naming conventions, emailing files, cutting 
and pasting, and lots of opening-two-files-side-by-side and reading line by 
line.

In this lesson, we're going to look at a tool known as a version control system 
(VCS) that provides an integrated means of dealing with all of the above 
logistical issues. Specifically, we're going to learn the basics of git, which 
is rapidly becoming the most popular version control system in scientific 
software development.

The practice of using version control will pay dividends immediately from an 
organizational perspective, even if your projects are relatively small and you 
work on them alone. However, version control really starts to show its 
importance as the size of your projects grow. When you write a program that 
will be maintained on an ongoing basis (rather than just a one-off script for a 
single project) and when you try to start collaborating with other 
computational scientists, version control becomes a virtual requirement. 
Knowing how to work with version control systems will also be necessary if you 
ever want to contribute to existing open source scientific software packages, 
including IPython, numpy, and many of the other tools that we've been 
discussing.

Before we get started, we'll make sure you have all of the software and 
accounts that you'll need for this lesson and then discuss some basic 
background and terminology. We'll then proceed through each of the seven 
"headaches" above and see how we can make these less painful through judicious 
use of git. Finally, we'll close with a brief discussion of the difference 
between plain text and binary files, as these relate to version control, and 
talk through a few tips for writing papers.

The lessons below are really just an entry point into the world of git. For 
more information, and more detailed explanations of all that follows, have a 
look at the excellent free book [Pro Git](http://git-scm.com/book).

Installing and configuring git
------------------------------

To confirm that git is installed on your computer, open a terminal window and 
run the command

	$ git --version
	
If this prints something like `git version 1.8.3.4` (or any other version 
number), then you're ready to go. If you see `git: command not found` then you 
need to install git.

The easiest way to install git is to use one of the installers 
[here](http://git-scm.com/downloads). On Windows, you might want to instead 
install [mysysgit](http://msysgit.github.io/) which will also give you a 
bash-like command line environment. On Linux or a Mac, you can also install git 
through your package manager (on a Mac, you might be interested in trying 
[homebrew](http://brew.sh/)).

Once git is installed, we will need to configure a few global options. The most 
important are to tell git your name and your email address, which will be used 
to identify your actions. To do this, run the following commands in a terminal 
session (using your name and email address):

	$ git config --global user.name "John Doe"
	$ git config --global user.email johndoe@example.com

Additionally, we want to make sure that git is going to use a useful text 
editor when necessary. If you're on a Mac or have installed nano using the 
Software Carpentry Windows installation instructions, you should run

    $ git config --global core.editor "nano"

Before doing the above, you should try running the command `nano` in your shell 
to make sure that it opens. If you're on Linux (or otherwise prefer to use a 
different text editor like emacs or vim), you can enter something different 
here.

Note that this configuration information isn't sent anywhere - it's just saved 
in a file on your computer (specifically, a file named `.gitconfig` that is 
located in your home directory).

For the later parts of this lesson where we begin working with remote copies of 
our files, we'll need a non-local account to hold our uploaded files. The most 
popular site for doing this is Github, which is what we'll use here. To create 
an account on Github, simply go to [http://github.com](https://github.com) and 
sign up (it's free). A similar, though not quite a widely used, service is 
[Bitbucket](https://bitbucket.org/), which you may want to check out for your 
own uses later.

Getting started with git
------------------------

The first step in using git is to select a project (i.e., a set of files in a 
directory that accomplish a defined research task) that you wish to manage with 
version control. You'll then create what's known as a git repository to contain 
and manage these files.

To start off, let's imagine that we have a project in which we're analyzing 
data from camera traps that have photographed the wildlife in a particular 
area. Our basic tasks are to read in the raw data, run a regression analysis, 
make a table, and make a figure. In practice, we would likely manage a simple 
analysis like this by placing all of our code into a single file, probably a 
hundred lines long or so, which is what we'll model here.

To keep things simple in this lesson, we won't actually write the code to 
perform these tasks - instead, we'll create the script file and add simple 
lines of pseudo-code to describe each action. (Incidentally, we'll actually 
review some real code to do this in a later lesson.)

To start off, our script file will contain the following text.

    # Camera trap script
    
    Read data file

    Run analysis

>### Exercise 1
>Using the terminal, navigate to a convenient location on your computer and 
>make a directory called `wildphoto`. Inside this folder, create a text file 
>called `script.py` that contains the text above.

Now, we'll set up a git repository for this folder by running the following 
command within that directory. Again, make sure that you're in the `wildphoto` 
directory before running this command.

    $ git init
    Initialized empty Git repository in /Users/jkitzes/wildphoto/.git/

As you can tell by the output of the `git init` command, initializing a 
repository involves creating a hidden folder, called `.git`, inside of the 
`wildphoto` folder. This hidden folder will contain all of the tracking 
information about your files. If you ever want to delete the git repository, so 
that you're back where you started without any version control history, it's 
actually as simple as just deleting this folder.

Now that you have your repository initialized, it's time to start tracking 
files. At this point, git is not paying specific attention to any files in this 
directory - if you'd like git to track a file, you have to tell git to track 
it. Any files that you don't tell git about will remain untracked.

To track a file, we need to add it to the repository. Once we've added a file 
once, git will watch it from then forward as we make changes to it. To add a 
file to a repository, we first need to review the three possible "locations" 
that a file can be in. These are

1. Workspace - a new file, or a change to a file that's already tracked (more 
   on this later), that's sitting in your folder
2. Staging area (or index) - a temporary holding state where you line up all of 
   the files or changes that you want to commit to your repository
3. Repository (or repo, for short) - git's "memory bank" that holds and tracks 
   your files and changes to your files

Basically, the process of using git involves making edits in our workspace, 
adding these edits to our staging area (this is known as "staging"), then 
saving everything in the staging area to the git repository (this is known as 
"committing").

To get started, it's often a good idea to check in on git to see what it thinks 
is going on. To do this, we run the simple command

    $ git status
    # On branch master
    #
    # Initial commit
    #
    # Untracked files:
    #   (use "git add <file>..." to include in what will be committed)
    #
    #	script.py
    nothing added to commit but untracked files present (use "git add" to track)

This information returned by this command tells us what git is thinking at the 
moment. In this case, git is telling us that we have an untracked file called 
`script.py` and that nothing is currently present in our commit (this is 
another way of saying that nothing is in our staging area). We'll talk about 
the meaning of "branch master" later on.

To add the file `script.py` to the staging area, we run the command

    $ git add script.py

This command doesn't seem to do anything, but if we run `git status` again, 
we'll see its effect.
   
    $ git status
    # On branch master
    #
    # Initial commit
    #
    # Changes to be committed:
    #   (use "git rm --cached <file>..." to unstage)
    #
    #	new file:   script.py
    #

Now we have the new file `script.py` in our staging area. If we wanted to, we 
could add other files, or make other changes, and add them all to the staging 
area as well. Remember, the staging area is a way of collecting any number of 
changes that you'd like to commit to the repository all at once.

A logical question at this point is why git bothers to have a staging area at 
all - why don't you just commit everything that's changed all at once to the 
repository? This boils down to a question of workflow. It is often the case 
that you'll make a bunch of changes to a bunch of files (possibly screwing up 
all sorts of things), but you don't necessarily want to add all of these 
permanently to the repository all at once. You may want to add them a few at a 
time, so as to better keep track of their history. Or you may not want to add 
some of them at all. The staging area basically helps you organize all of the 
changes that you've made into commits that you add to your repo, one by one, in 
some logical fashion that will be useful to you later on.

Finally, we end by committing our changes that are currently in the staging 
area to the git repository. To do this we run

    $ git commit

When you do this, you will appear to be suddenly transported somewhere else in 
your terminal window (or a graphical text editor of some kind might pop up). 
Don't worry - all that has happened is that git has opened a text editor for 
you to enter a commit message. This is one of the most useful features of a 
version control system - each time you commit some set of changes to your repo, 
you get to enter a short description of what the change was and perhaps why you 
made it. This helps to track the history of the updates to your project files.

It's good practice to start by entering a short one line sentence to describe 
the commit in general terms. Often this is all that you'll need. If you want to 
capture more ideas, you can press Return twice to enter a blank line below the 
first sentence and then type as much information as you'd like.

You'll see that git has added some lines starting with `#` symbols to your 
commit message. Since anything starting with `#` is considered to be a comment 
and not included in your commit message, these lines are just for your 
information and you can safely ignore them.

So, in this case, a useful message might just be "Initial commit of script to 
analyze camera data". Go ahead and type that line at the top of the text 
editor, then save the file and exit the editor. In nano, you can just press 
Ctrl-x to exit, after which nano will ask you if you want to save the file. 
Press Y for yes and press Enter to accept the file name/location that it 
suggests.

Now you'll magically be dropped back into your terminal window, and you'll see 
that your command has printed output like the following.

    $ git commit
    [master (root-commit) beda5b7] Initial commit of script to analyze camera 
    data
     1 file changed, 9 insertions(+)
     create mode 100644 script.py

The key information here is that we've successfully changed 1 file 
(`script.py`) by making 9 insertions (that's one for each new line of text in 
the file). You'll learn about the other information here as we go along.

So, what was the point of all that? The upshot is that the exact state of the 
file `script.py` that was in the staging area at the moment of our commit is 
now permanently stored and tracked in our version control system. No matter 
what changes we make to this file in the future, we can always easily come back 
to this version at any time, as we'll see later. We can also easily compare 
this version to other future versions.

To see a record of our previous commits, we can run the command `git log`, 
which will show us a history of our commits (so far, just this one initial 
commit).

    $ git log
    commit beda5b7b6fa4c3b8642c7d26b87f691fd6bcd8dc
    Author: Justin Kitzes <jkitzes@berkeley.edu>
    Date:   Mon Jan 13 16:07:01 2014 -0800

        Initial commit of script to analyze camera data

As before, we can check `git status` to see what git thinks is going on (typing 
these two words will soon become like a reflex).

    $ git status
    # On branch master
    nothing to commit, working directory clean

Once again, we'll talk about the meaning of "branch master" later on. The 
second line, though, tells us that our working directory is "clean" (i.e., it 
matches the repository exactly), and as such there's nothing available to 
commit. In other words, we haven't changed anything since our last commit.

Having made our initial commit to track `script.py`, we can now get on with our 
actual research work of writing more code to perform more analysis. As we do 
so, our workflow will now include periodically committing our changes to the 
git repository so that we save a historical record of everything that we've 
done.

Now that you've got the basics down, we'll turn to our seven "headaches" and 
see how git can help us alleviate each of these.


1. Keeping version history
--------------------------

Probably the most basic logistical headache of computational research (or, 
really, any kind of research) is keeping track of old and new versions of files 
as they're updated. Whether you primarily work with Word documents or computer 
code, you probably have folders sitting around on your computer containing 
files like `Analysis_v3.doc`, `Analysis_v4.doc`, `Analysis_v5_final.doc`, etc. 
Or, if you like to live dangerously, maybe you only have file and rely on a 
backup system (like Time Machine or Dropbox) to retain snapshots of the file 
and pre-set time intervals, so that you can (in theory) got back to any moment 
in time and see what your file contained.

Rather than constantly using "Save As" on our files or relying on a backup 
system, we can instead use git to hold both old and new copies of our files for 
us. To see how this works, let's make a few updates to our file.

>###Exercise 2
>Update this file two times, each time adding a new line to the script. For the 
>first update, add a blank line under `Run analysis` and then a line reading 
>`Make table`. Save this change, stage this change using `git add`, and then 
>commit it, adding a useful commit message. Then, add another blank line under 
>`Make table` followed by another line `Make small figure`, and commit this 
>change as well. Run `git log` to see your three commits.

After making both of these changes, your `script.py` file should look like 
this.

    # Camera trap script
    
    Read data file

    Run analysis

    Make table

    Make small figure

If we run `git log` again, we should see something like this.

    $ git log
    commit 89f54453b748131b87cee9d5742dd4412cd8183d
    Author: Justin Kitzes <jkitzes@berkeley.edu>
    Date:   Mon Jan 13 16:08:44 2014 -0800

        Add initial code to make small figure

    commit 97e349856f3b3ee2647c327d3a609ff1dc9fae6f
    Author: Justin Kitzes <jkitzes@berkeley.edu>
    Date:   Mon Jan 13 16:08:20 2014 -0800

        Add code to make table

    commit beda5b7b6fa4c3b8642c7d26b87f691fd6bcd8dc
    Author: Justin Kitzes <jkitzes@berkeley.edu>
    Date:   Mon Jan 13 16:07:01 2014 -0800

        Initial commit of script to analyze camera data

Pretty soon, our log of commits is going to start getting longer, and it will 
be helpful to have a better way of viewing our commit history. To help 
visualize our history better, try running the version of `git log` below, which 
adds some additional arguments.

    $ git log --oneline --graph --decorate --all
    * 89f5445 (HEAD, master) Add initial code to make small figure
    * 97e3498 Add code to make table
    * beda5b7 Initial commit of script to analyze camera data

You'll note that new version of our command this gives a simple list of our 
three commits, each represented by a * symbol. Following the * is a strange 
list of characters, which is known as a hash. A hash is a random string that is 
used as an identifier for each commit and can be used to reference the commit 
(we'll use these in just a moment). Note that your hashes will be different 
from these, as they're randomly generated for each individual commit. Finally, 
you'll see the first line of each commit message.

Before your most recent commit, you'll see two additional words in parentheses, 
HEAD and master. These labels provide a useful way of navigating around your 
history and of knowing where you are in your history at any time. HEAD is 
particularly important - git uses the special label `HEAD` to refer to the 
location of your workspace with regard to your git history. In other words, if 
`HEAD` points to the commit labeled 89f5445, as it does here, it means that 
when you actually open the `wildphoto` folder on your computers, you'll be 
looking at all of your files as they were at commit 89f5445. As we'll see in a 
moment, we can move HEAD around so that we see different versions of our files 
in our `wildphoto` folder, or our workspace. The word master refers to a branch 
called master, which once again we'll discuss later.

As you've probably gathered by now, each of these commits is storing the exact 
state of our file `script.py`, as present in the staging area, at the moment of 
the commit. In that sense, git is retaining an exact history of our file for us 
over time. (If we had more than one file, it would be storing the exact state 
of our entire workspace folder at each commit.)

Before we move on, it turns out that the above version of `git log` is going to 
be very useful, so let's quickly create an alias for it.

    $ git config --global alias.lg "log --oneline --graph --decorate --all"

If you now type `git lg`, you'll see that does the same thing as the long line 
that we entered above.

Moving on, one of the simplest things that we might want to do with our history 
is to pull up and examine older version of our file, perhaps to run it again to 
compare its analysis results to a different version. There are a few ways to do 
this - we'll discuss the most important here, and you'll see a few others 
later.

In this case, let's say that we want to roll back our entire workspace to a 
previous state, say the state of the folder at the time of our initial commit. 
Recall, at this point, that our script did not yet have the lines to make the 
table or figure.

To roll back our entire workspace, we use the command `git checkout` followed 
by the hash for the commit that we want to go back to (be sure to use the hash 
for your initial commit in your own repository, as found by running the `git 
lg` command described above).

    $ git checkout beda5b7
    Note: checking out 'beda5b7'.

    You are in 'detached HEAD' state. You can look around, make experimental
    changes and commit them, and you can discard any commits you make in this
    state without impacting any branches by performing another checkout.

    If you want to create a new branch to retain commits you create, you may
    do so (now or later) by using -b with the checkout command again. Example:

      git checkout -b new_branch_name

    HEAD is now at beda5b7... Initial commit of script to analyze camera data

Wow, that was kind of a lot of output. The important line is the last one, 
starting with "HEAD is now at...". If we run our special `git lg` command 
again, we'll see that `HEAD` has in fact moved.

    $ git lg
    * 89f5445 (master) Add initial code to make small figure
    * 97e3498 Add code to make table
    * beda5b7 (HEAD) Initial commit of script to analyze camera data

This tells us that our workspace, that is our actual `wildphoto` folder on our 
computer, now is showing us our files exactly as they were at the moment of 
this initial commit. Hop over to your `wildphoto` folder and open the file 
`script.py`. Miraculously, it has reverted back to it's state as of your 
original commit!

It can be a little disconcerting to see your files update like this "in 
place" - it may give you the feeling that you're losing or overwriting 
information. Rest assured that git has a history of all of your file versions 
that you've ever committed and that you can get back to any spot at any time.

The rest of that `git checkout` command output mentioned a detached HEAD state. 
Fortunately, a detached HEAD in git is not nearly as frightening as it sounds. 
All it means is that you shouldn't start editing files from this place in 
history and committing them, because you'll lose those changes. This is 
probably the only major danger that you'll run across using git - make sure not 
to commit new changes in a detached head state, because you may lose them! 
We'll talk later on about how you would correctly "go back in time" and then 
start making new versions of your files beginning from this older location. For 
now, though, since we just want to look at our old files, we won't be running 
into this problem.

Let's say you've looked around at this old version and want to come back now to 
your most recent version. Looking at the output of the previous `git lg`, we 
can see that the label `master` is attached to our most recent commit regarding 
the figure. To get back to this spot, just run another git checkout command.

    $ git checkout master
    Previous HEAD position was beda5b7... Initial commit of script to analyze camera data
    Switched to branch 'master'

Be careful here not to use `git checkout` followed by the hash for the most 
recent commit - that will leave you in a detached HEAD state and just move you 
around. The command above, on the other hand, places you on something called a 
branch that has the name "master". This is where you want to be (on a branch) 
before you start committing more changes - we'll explain that more in a minute.

You can run the `git lg` command above again to see that, in fact, your `HEAD` 
has returned to the most recent commit.

A final word about using commit hashes to check out versions. Aside from using 
a hash, git gives us an easy way to label particularly important commits so 
that we can easily get to them later on. To do this, we use a command called 
`git tag my-tag-name`. For example, you can tag our current commit with the 
name `lab_mtg` by running the command

    $ git tag lab_mtg

Running our `git lg` command, we now see

    $ git lg
    * 89f5445 (HEAD, tag: lab_mtg, master) Add initial code to make small figure
    * 97e3498 Add code to make table
    * beda5b7 Initial commit of script to analyze camera data

In addition to HEAD and master, we now see that the commit 89f5445 is labeled 
by a tag `lab_mtg`. We can now use this label instead of the commit hash to 
work with this commit from here forward.

2. Comparing two versions of a file
-----------------------------------

In the previous section, we saw how we could roll back our entire project to a 
previous state. While this is great for reviewing the history of our project, 
it doesn't help us much if we want to compare versions of a file from two 
particular points in that history (for example, compare our current version to 
a version a few commits back). For this, we can use two different techniques.

### Comparing files 1

If the file that you want to compare is simply a plain text file, like our 
`script.py`, then we can use an easy command called `git diff`.

    $ git diff beda5b7:script.py 89f5445:script.py
    diff --git a/script.py b/script.py
    index b60af41..b4c75da 100644
    --- a/script.py
    +++ b/script.py
    @@ -3,3 +3,8 @@
     Read data file

     Run analysis
    +
    +Make table
    +
    +Make small figure

In the above command, we entered the hash for the earlier commit (here, our 
initial commit) followed by the hash for the later commit (here, our most 
recent commit). The command `git diff` actually calls an external command line 
program called `diff` and runs it on the versions of `script.py` found in those 
two commits. After a few cryptic lines (that you might be able to interpret if 
you stare hard), you'll see that this command prints out the file `script.py` 
with some `+` signs to show the lines that were added between these two 
commits. If lines were deleted, you'd see `-` signs, and if lines were changed 
you'd see something a bit more complicated that indicated the in-place change.

Two quick tips. First, you'll want to be sure to enter the earlier commit first 
to get the order of changes correct. Second, if you leave off the `:` and file 
names from the `git diff` command, you'll see the differences between all files 
that changed between two commits.

For large files, the output of `git diff` can be less than helpful. If you want 
to use this command in "real life", check out the command `git difftool` and 
how to set up an external, graphical viewer for diff-ing. Still, this is a 
reasonable place to start for identifying changes to plain text files.

>###Exercise 3
>Consider the command `git diff lab_mtg HEAD`. See if you can guess what the 
>output will be, and then run it and see the actual output. Were you right?

### Comparing files 2

There are two cases in which a diff tool is not going to be very helpful for 
comparing file versions. First, if your files are not plain text but are 
instead binary or some other complicated text format (see section at end of 
this lesson), the output of `diff` will be essentially nonsensical. Second, 
sometimes you just want to compare two files visually side by side (i.e., just 
opening them both and reading them at the same time) rather than relying on a 
tool.

In both of these cases, you need to go back in time, grab a copy of a specific 
file from an earlier commit, and bring it into your present workspace so that 
you can actually open the current version and the older version at the same 
time. You can do this fairly easily with a command called `git show`.

    $ git show beda5b7:script.py > old_script.py

Now, if you look into your folder, you'll see a new file called 
`old_script.py`. If you open this, you'll see that it gives you the version of 
the `script.py` file that you had at the commit beda5b7. You can use the syntax 
above to get back a copy of any file from any commit. Recall that the `>` 
symbol is a redirect, a shell command that takes the output of the git command 
and saves it in the file with the name following this symbol.

Keep in mind that using `git show` generates temporary files that are copies of 
old versions. You'll want to delete these after you're done looking at them, or 
else your repo will just end up with a whole bunch of copies of different 
versions of your files all mushed together, which is exactly the confusion that 
we're trying to avoid by using version control in the first place.

A final note - if you write your papers in Word, you can use this `git show` 
approach to approximate the `git diff` command above. Simply use `git show` to 
bring an old copy of your Word doc into your workspace and then use the Word 
(Compare and Merge Documents)[http://support.microsoft.com/kb/306484] feature.

3. Maintaining multiple project branches
----------------------------------------

So far, the techniques that we've looked at provide a unified way of replacing 
the "Save As..." technique that you may be using now to save and review old 
copies of files. This next lesson is where the power of version control really 
starts to make our lives more efficient.

To get started, we'll introduce the concept of a branch. Branches work sort of 
like they sound - imagine a tree with a big trunk growing upward, with a branch 
coming out to one side. Both the trunk and the branch are growing from the tips 
(from the apical meristem, for you biologists), so the newest wood is always at 
the tip of the branch and the tip of the trunk.

Now, apply this analogy to the development of a file. Let's say we're working 
on `script.py` for some time, and at some point we need to create a version of 
our analysis that's specifically for a seminar presentation. While we work on 
adjusting our script for the presentation, we also may want to keep working on 
the main version of our file, which runs the analysis for our dissertation. To 
do this, we'll create a separate branch for the "presentation version" of our 
script and allow it to grow, on its own, independently of the trunk. At any 
time, we can switch back and forth between the tip of the branch and the tip of 
the trunk, depending on whether we want to "add new wood" to the presentation 
or the dissertation branch.

Let's walk through this process, which should make the above example more 
clear. First, we can run our `git lg` command again to see where we are.

    $ git lg
    * 89f5445 (HEAD, tag: lab_mtg, master) Add initial code to make small figure
    * 97e3498 Add code to make table
    * beda5b7 Initial commit of script to analyze camera data

Direct your attention now to the label "master" that's associated with our most 
recent commit. Whenever you create a new git repository, a branch called 
"master" is automatically created, and this is the branch where all of your 
commits are added unless you specify otherwise. Master is thus the trunk from 
our tree analogy above. So far, we've just been growing our trunk upwards.

Now, however, let's introduce a second branch (aside from the main branch 
"master"). To do this, we use our old friend the `git checkout` command, but 
with a new additional option.

    $ git checkout -b presentation
    Switched to a new branch 'presentation'
    $ git lg
    * 89f5445 (HEAD, tag: lab_mtg, presentation, master) Add initial code to 
      make small figure
    * 97e3498 Add code to make table
    * beda5b7 Initial commit of script to analyze camera data

The option `-b` in this command tells git to create a new branch with the 
subsequent name. We only need to use this option once - from now on, to switch 
between branches, we can just use `git checkout branch-name`. As you can see, 
we now have a new branch called presentation that points to the commit that we 
were just on. At the moment, the presentation and master branches point to the 
same place.

It's important to keep track of which branch you're on at all times, since that 
branch is where any new commits will be appended (i.e., whether the new commit 
will grow the trunk or a branch of our tree). To check what branch you're on, 
you can always run

    $ git branch
      master
    * presentation

The branch with the * symbol is, logically, the one that you're currently on.

Now, let's try adding some commits that will cause the two branches to start 
growing apart.

>###Exercise 4
>Now that we're on the presentation branch, let's start making a few updates to 
>our analysis specifically for our presentation. First off, we'll want the 
>lines in our figure to be red so they can be seen better. Change the line 
>"Make small figure" to "Make small figure, red line" and commit this change. 
>Run `git lg` and review the output. What has happened?

Here's a tip for commit messages. If you just want to add the opening sentence 
of a commit, without a longer description, you can run `git commit -m "My 
message"` directly from the command line so that you don't have to drop into 
and out of a text editor every time.

From running `git lg`, you can see that we've added a commit (i.e., some new 
growth) to the presentation branch, while the master branch has stayed where it 
was. Now, let's imagine that while we're waiting for the presentation to 
happen, we had a new idea about our table. We don't need to change the table 
for the presentation, but we do want to make the change so that it will be 
reflected later on in our dissertation.

>###Exercise 5
>Switch back to the master branch by running `git checkout master`. Run `git 
>lg` and review your `wildphoto` folder to make sure you understand where you 
>are now - is the edit to make the figure line red present here? Open 
>`script.py` and add the line "Make header bold" underneath the "Make table" 
>line. Commit this change. Run `git lg` and examine the output - does it remind 
>you of a tree trunk with a branch?

The more that you play around with branches, the more that you'll realize how 
incredibly useful they are. Another great use of branches is to create a branch 
for some experimental change that you'd like to make that might take a while to 
complete and could really mess up your results in the mean time. If you make 
all of those messy edits in a branch, you can always `git checkout master` to 
get back to your last clean, working copy of your files. You can even do 
something like wake up in the morning, `git checkout messy-change`, work on 
your experimental stuff, have lunch, `git checkout master`, and then go back to 
plodding along slowly but surely towards your dissertation.

One final note. Now that we've discussed branches, we're better able to discuss 
the "detached HEAD" state that we saw earlier. A detached HEAD simply means 
that your HEAD (i.e., the commit that your project folder currently represents) 
is not linked to the tip of a branch. What this means is that if you add a 
commit, this commit will just be floating in space rather than glued on to the 
tip of an existing branch (imagine a tree adding 1 inch of new wood floating 
somewhere by itself in the sky). If we do this, we won't have any easy way of 
getting back to that new commit later on. To avoid this problem, you should 
only commit when you are at the tip of an existing branch (i.e., when your HEAD 
is attached). If you ever get completely lost, running `git checkout master` 
will always take you back to a safe, known location at the tip of your main 
trunk.


4. Merging two project branches together
----------------------------------------

We've now discussed how to use branches to develop your project along two 
parallel lines. Now, we'll discuss how to bring two branches back together 
after they've diverged (something a real tree doesn't do, most of the time) 
using an operation called a merge. Merging two branches is actually quite 
common, and applies most commonly when you've gone off and created some edits 
in a branch that you want to bring back to be a part of your canonical "master" 
branch going forward.

Merging two branches can range in difficulty from very easy to extremely 
difficult, with the difficulty depending on how many conflicting changes you've 
made in the two branches. Fortunately, many times merging a branch will 
introduce no specific conflicts, in which case merging is trivial. First we'll 
examine a merge with no conflicts, and then we'll try our hand at a merge with 
conflicts.

### Merging with no conflicts

Let's say that we like the new red line in our figure that we made for the 
presentation and that we want to bring this change back into our master "trunk" 
so that we'll have it in our future development. To merge the branch 
presentation into the branch master, we do the following (note that when you 
run the second command, the `git merge`, you'll be asked to enter a commit 
message for the special commit that performs the merge itself).

    $ git checkout master
    Already on 'master'
    $ git merge presentation
    Auto-merging script.py
    Merge made by the 'recursive' strategy.
     script.py | 2 +-
     1 file changed, 1 insertion(+), 1 deletion(-)

The first `git checkout` command is just to make extra sure that we're on the 
master branch - the branch that you're on when you run `git merge` is the one 
that the changes will come _into_. The second command actually performs the 
merge, and we can see that it succeeds with no problems. Running `git log` to 
see our current status shows us the following.

    $ git lg
    *   288f50d (HEAD, master) Merge branch 'presentation'
    |\
    | * df89527 (presentation) Make line red
    * | 013b1af Make header bold
    |/
    * 89f5445 (tag: lab_mtg) Add initial code to make small figure
    * 97e3498 Add code to make table
    * beda5b7 Initial commit of script to analyze camera data

We can see that the presentation branch is still right where we left it, but 
now master has, as antecedents, both the "Make header bold" commit from earlier 
and merged in the "Make line red" commit from the presentation branch. That 
means that our current workspace, at the tip of master, will reflect the 
changes associated with both of these commits, even though they were originally 
on two separate branches. If you open `script.py`, you'll see that both of 
these changes are now in our workspace, which is showing us the new tip of our 
master branch.

### Merging with conflicts

Unfortunately, some merges can be more difficult due to conflicts. Conflicts 
occur when you've made changes in both branches since they've diverged that 
conflict with each other. A merge with only a few conflicts is still relatively 
easy to handle, as we'll see below. If you routinely end up merging branches 
with a lot of conflicts, I would recommend that you look into setting up `git 
mergetool` to make your life easier.

To create a conflict, we could create another branch and start committing, but 
to save us some time, we'll instead just undo our last merge and start from 
there. To undo your last commit, completely nuking everything that you did in 
tha commit forever, run the following.

    $ git reset --hard HEAD^1
    HEAD is now at 013b1af Make header bold

You can run `git lg` again to see that our version history now looks just like 
it did before we merged. The above command is quite handy any time you make a 
mistake by committing. The notation "HEAD^1" is a shortcut way of saying "one 
commit before HEAD", where HEAD (as you recall) points to the commit that is 
currently present in our workspace. If you want to undo the commit but not nuke 
everything, you can use the `--soft` option instead - this will leave the 
changes that you made in the commit in your staging area, so that you can 
review, edit, and re-commit them, rather than destroying them entirely like 
`--hard` does.

Let's now create a conflict. Imagine that while you were working alternately on 
the presentation and the master versions, you checked out the master branch and 
decided that you wanted the lines in the figure to be thicker for your 
dissertation figures. To do so, you changed the line "Make small figure" in 
your script file in the master branch to "Make small figure, thick line". Go 
ahead and make and commit this change.

Now, let's once again try to merge the presentation branch into the master 
branch. Running `git merge` now gives us a little trouble.

    $ git merge presentation
    Auto-merging script.py
    CONFLICT (content): Merge conflict in script.py
    Automatic merge failed; fix conflicts and then commit the result.

Uh oh, now what's going on? We're actually currently paused in the middle of 
our merge, and git is waiting for us to resolve the merge conflict.

Again, a merge conflict occurs when we've made changes in the same location in 
a file in both branches since the point at which the branches diverged. In this 
example, we caused the conflict by editing the line "Make small figure" two 
different ways in the two branches - in one branch, we added "make line red" 
and in the other branch we added "thick line". Git has no automatic way of 
knowing which of these we want to keep (or if we want to combine these 
somehow), so it asks for our help.

If we run `git status` now to see what git is thinking, we'll see some new 
output.

    $ git status
    # On branch master
    # You have unmerged paths.
    #   (fix conflicts and run "git commit")
    #
    # Unmerged paths:
    #   (use "git add <file>..." to mark resolution)
    #
    #	both modified:      script.py
    #
    no changes added to commit (use "git add" and/or "git commit -a")

This tells us that we have one file, `script.py` that is "unmerged" (i.e., we 
have to complete the merge ourselves).

To complete the merge, we start by opening the `script.py` file currently in 
our workspace to see what it looks like. When you do that, you'll see these 
funny lines in the middle of the file.

    <<<<<<< HEAD
    Make small figure, thick line
    =======
    Make small figure, red line
    >>>>>>> presentation

The <<<< and >>>> symbols give the top and the bottom of the conflict area, and 
the ==== symbols separate the top version, which was the version in HEAD (where 
our workspace was pointed - this was the master branch that we were merging 
into), from the bottom version, which was the version in the presentation 
branch.

To settle this conflict, we just edit this section however we want. In this 
case, we'll make the line say "Make small figure, thick red line". Make sure to 
delete all of the other stuff (from the <<<< to the >>>>) added by the merge 
command, so that the file looks exactly how we want it to look after the merge 
is done. In other words, instead of that whole block of stuff above, our file 
should now just have

    Make small figure, thick red line   

in its place.

Now we can add this fix to our staging area using `git add` and then run `git 
status` to see what's going on.

    $ git add script.py
    $ git status
    # On branch master
    # All conflicts fixed but you are still merging.
    #   (use "git commit" to conclude merge)
    #
    # Changes to be committed:
    #
    #	modified:   script.py
    #

Git helpfully tells us that we've fixed all of our conflicts, but that we're 
still in the middle of our merge, and that we need to run `git commit` to 
complete the merge. Go ahead and do so, and run `git lg` once again to make 
sure that you've got the history that you would expect.

And with that, we conclude the main part of our lesson focused on working with 
git locally for your own projects. Next we'll turn somewhat briefly to the 
basics of using git remotely for syncing, sharing and collaboration. But before 
we do that, try your hand at the capstone exercise(s) below.

>###Exercise 6
>To really hammer home everything that we've learned so far, try the following 
>tasks.
>
>1. Since you're so proud of your script, add a line that says "# All rights 
>   reserved" near the top and commit this change on your master branch.
>2. Use `git diff` to compare the current version of your script to the one 
>   from the initial commit.
>3. Use `git show` to bring a copy of your script version tagged `lab_mtg` into 
>   your current workspace and open it side by side with your most recent 
>   version. Don't forget to delete this temporary file when you're done.
>4. Make a branch called `experimental` and commit a few changes there. Don't 
>   hold back - create conflicts if you dare!
>5. Merge your experimental branch back into your master branch.

If you finish the above easily, here's a bonus exercise.

>###Exercise 7
>Make a change to your script and add it to the staging area. Then make another 
>additional change and, before running `git add` again, run `git status`. What 
>does this output tell you about how git understands files versus changes to 
>files? Can you think of practical applications of this behavior?

Before we move on to using git remotely, a final word about using git in 
practice. While it's important to understand the basics of how to use git from 
the command line, as we have here, there are certain operations that are much 
more easily done with a "modern" graphical program, including visualizing 
complex branching structures and dealing with difficult merges. There are many 
programs to choose from - on a Mac or Windows, I would suggest trying 
Sourcetree, which you can download and install 
[here](http://www.sourcetreeapp.com/). If you're on Linux, you might try 
[Smartgit](http://www.syntevo.com/smartgithg/) or search for other 
alternatives.

5. Sharing a project
--------------------

Once you have your research projects managed with version control, you will 
soon want to find ways to share your project and its history with the world (or 
at least with a few collaborators). We're going to walk through the very basics 
of how to do this using Github, which is rapidly becoming the most popular site 
for sharing scientific code. Working with so called remote repositories can get 
quite complicated, and here we'll only be able to scratch the surface of what's 
possible. Refer to the free online book [Pro Git](http://git-scm.com/book) or 
talk to the instructors if you'd like more information or pointers.

Syncing your files across computers and sharing them with the world requires 
access to somewhere up in "the cloud" where you will upload and download files. 
For this, we're going to use Github. By now, you should have already created a 
user account on Github, and we're going to use that account to upload your 
`wildphoto` project to a remote repository.

To get started, we need to tell Github to create a remote repository space to 
hold your project. Head over to [github.com](http://github.com) and log in, if 
you haven't already. You'll then be taken to a page (currently mostly empty) 
where, on the right hand side, you will see a box with the title "Your 
repositories". Next to that box, you'll see a green button called "New 
repository". Click this button. On the next page, fill in `wildphoto` as the 
Repository name, leave the button checked to make the repository public, and do 
not check the box to Initialize the repository. Then click the button to Create 
repository.

In the future, you may want to create private repositories to hold code that 
you do not wish to make publicly available. To do this, you'll need to upgrade 
to a Micro account, which is [free for students](https://github.com/edu). 
Github will then give you the option of allowing only specific collaborators to 
view your private repositories.

Once you create the remote repository, Github will provide you with some 
helpful instructions on what to do next. Since we already have a local 
repository that we want to upload, we want to use the second set of 
instructions, Push an existing repository from the command line. You can think 
of the `git push` command as basically equivalent to uploading your current 
project directory as well as all of your project history. Later on, we'll use a 
command called `git pull`, which you can think of as equivalent to downloading. 
(Side note: `git pull` is actually a little more complicated, as it has to deal 
not only with downloading but with merging in any changes that have been made 
in the remote repository that you don't have. We'll discuss this more later 
on.)

Now that we've mentioned `push` and `pull`, there's one more concept that we 
need to consider right now, which is the idea of a remote. In git, a remote is 
essentially an internet address to which you can push, and from which you can 
pull, changes to your project. To tell our local `wildphoto` repository how to 
interact with our new Github remote repository, we thus have to "add a remote" 
to our local project.

To do this, as explained on the Github help page that you're now looking at, we 
can run the command

    $ git remote add origin https://github.com/jkitzes/wildphoto.git

This tells git to add a remote address named `origin`, and to assign it the URL 
given at the end of the statement. `origin` is a special name that is usually 
reserved for the main remote repository that we're working with. As you might 
have gathered from the above, it's possible to work with multiple remote 
repositories for a single project. This is an important part of advanced 
collaborative workflows that are beyond the scope of this beginner tutorial. 
For now, we're only going to be working with this one remote, which now points 
to our main Github repo that we just set up.

Finally, we're ready to send our project and it's history to Github. To do 
this, we run our `git push` command. The argument `-u` is an option that you 
only need to use the first time you push to a remote repository, and the 
following words `origin master` indicate to push the master branch to the 
remote repository named origin.

    $ git push -u origin master
    Counting objects: 24, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (16/16), done.
    Writing objects: 100% (24/24), 1.94 KiB | 0 bytes/s, done.
    Total 24 (delta 8), reused 0 (delta 0)
    To https://github.com/jkitzes/wildphoto.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.

You may need to enter your Github password after running this command, which 
you should do. Hopefully you will see something similar to the above, which 
indicates that everything completed successfully. The output here tells us that 
our data was compressed, written to our remote repository, and that git has set 
up our local master branch to track the remote repository branch also called 
master. This essentially means that when we later "download" our data using 
`git pull`, git will know where to put it.

If you're working on a Windows machine, that command may have failed with an 
error message like `could not read Username for https:...: No such device or 
address`. If you get this message, try entering the command `env 
GIT_SSL_NO_VERIFY=true` and then try again.

Now, head back over to your web browser and reload the page that you were just 
on (or head over to http://github.com/my-username/wildphoto), and you'll see 
that your `script.py` file is available for all the world to see. You've just 
published your first scientific software package!

>###Exercise 8
>Take a few minutes to poke around the Github page for your project. In 
>particular, try clicking on the link for the file `script.py` and the link in 
>the header that says "7 commits".  Ask your instructors any questions as they 
>come up.
>
>If you'd like to make sure that you've got this workflow down, create a README 
>file in your local `wildphoto` directory, commit it to your local repo, then 
>push it to Github.

As you begin to work with git remotes, you may notice that you have to enter 
your password every time you try to `git push`. One good way to avoid this is 
to set up and use [SSH 
keys](https://help.github.com/articles/generating-ssh-keys), but we won't go 
through that process here.

6. Syncing and collaborating
----------------------------

Syncing files across multiple computers and collaborating with colleagues on a 
project requires, at the most basic level, essentially the same operations - 
you need to be able to create local copies of your repository on many 
computers, make changes to your files on any computer, push these changes back 
to the remote repository, then re-sync each of the computers with the new 
changes found in the remote repository. Here, we'll walk through a simple 
example using two computers, one owned by you and one by your (lone) 
collaborator on your `wildphoto` project, in which you'll use the simplest 
possible collaborative workflow, called "shared repo". If you imagine that your 
collaborator is actually you working at your home computer (instead of your 
office computer), you'll see that the process for collaborating is actually 
identical to the process of keeping your two computers in sync.

Before we get started, to immediately answer the obvious question - yes, you 
can place your version controlled project folder in Dropbox and access it from 
different computers, as well as share it with others. And yes, this can 
sometimes lead to problems that can be hard to fix (Dropbox's syncing mechanism 
can have trouble with the file structure of the `.git` folder where your 
project history is stored), especially if you both start working on the same 
file at the same time. We're going to discuss the more formal and "official" 
way for syncing and collaborating for the rest of this lesson.

To get started, pair up with a partner seated near you. Elect one of you to be 
the main project "owner" and one to be the project "collaborator". (For the 
rest of our lesson, being the collaborator is going to be more work, so you may 
want to have the person who's feeling the most comfortable so far be the 
collaborator.) In real world collaboration, the distinction between these two 
is not that important - it basically just involves choosing whose account is 
going to host the `wildphoto` repository that you both work with.

To begin, have the collaborator navigate to a different location on his/her 
hard drive, away from his/her own copy of the `wildphoto` project. From here 
forward, the collaborator will be working with the owner's remote repository.

Now, the collaborator needs to get a copy of the owner's `wildphoto` 
repository. The command for getting a fresh copy of a remote repository is `git 
clone`, followed by the URL from which you want to download the project. Have 
the collaborator navigate to the owner's `wildphoto` project page on Github by 
going to http://github.com/owners-username/wildphoto. There, on the right hand 
side of the owner's `wildphoto` project page on Github, you'll see a little box 
with the title "HTTPS clone URL". Copy this URL, and use it in the below 
command (you can also just replace owners-username with the owner's actual 
username, which will give the same thing).

    $ git clone https://github.com/owners-username/wildphoto.git
    Cloning into 'wildphoto'...
    remote: Counting objects: 24, done.
    remote: Compressing objects: 100% (8/8), done.
    remote: Total 24 (delta 8), reused 24 (delta 8)
    Unpacking objects: 100% (24/24), done.
    Checking connectivity... done

Now the collaborator has a complete, working copy of the owner's `wildphoto` 
repository on his/her computer, including the most current project files and 
the entire project history. Pretty easy, eh? Note that this was possible 
because the owner's Github repo was public - part of creating a public repo is 
allowing anyone, anywhere in the world, to clone a copy of your project and 
start working with it.

To follow our basic collaborative workflow (again, if you imagine that your 
collaborator is you at a different computer, then this is the workflow for 
syncing), we now need to complete the following three steps.

1. Have the collaborator make a change to the project and commit this change to 
   his/her local repo
2. Have the collaborator push this change to the remote Github repo.
3. Have the owner download this change from the remote repo so that the owner's 
   repo includes the collaborator's change.

You actually have almost all the tools to do this already. First, though, the 
owner will have to give the collaborator permission to push changes to the 
owner's repo (in a public repo, anyone can clone, but not everyone can push). 
To do this, the owner will need to go to the page for their repo on Github 
(http://github.com/owners-username/wildphoto), click on the Settings link on 
the right, click on the Collaborators link on the left, and add the 
collaborator's Github username on this page.

With that, you'll just need a few additional pieces of information to complete 
the three steps above. First, you should know that when the collaborator cloned 
the owner's repo, it automatically set up a remote called `origin` that points 
to the owner's Github repository (very convenient) - the collaborator can thus 
push changes to the remote master branch on Github using the same command that 
we saw before, `git push origin master`. Second, when it comes time for the 
owner to download and sync the new changes that the collaborator pushed to 
Github, the owner can just use the command `git pull origin master`, which will
download and merge in all changes in the master branch of the git remote
`origin` to your locally checked out branch (when running this, make sure you're
on the master branch - run `git checkout master` if you're not sure).

>###Exercise 9
>Complete the three steps described above for a simple collaborative workflow. 
>The instructors will come around the room to help you.

And that pretty much covers the basics of simple collaborating and syncing. 
Congrats - you're now a certified git beginner!

While that last comment was a bit tongue in cheek, it is true that what we've 
been able to cover today has only introduced a few of the many things that git 
can do and the many ways in which git can be used. In particular, while we were 
able to fairly thoroughly cover the basics of using git on your local computer, 
we only scratched the surface of how to use git remotely and collaboratively. 
If you are interested in moving forward with using git remotely, there are 
three additional "bit topics" that you'll soon need to learn about.

The first of these is how to work remotely with branches. You'll note that in 
the above, we only discussed how to push and pull the master branch from a 
remote repository. For the most part, working with other branches just involves 
adding the branch name to the end of the end of the `git push` and `git pull` 
commands, but you'll probably shortly need to look up the definition of 
tracking branches among other things.

The second is how to deal with conflicts that collaborators create when they 
work on the same part of a file. On your local machine, we saw conflicts arise 
when trying to merge one branch into another. When working remotely, this same 
type of conflict can happen. What you need to know is that you run `git pull`, 
you are actually both downloading the remote changes to the repository as well 
as trying to merge them into the branch that you are currently on. If this 
creates a merge conflict, you'll have to address it. To gain a finer level of 
control over this process, most intermediate and advanced git users use the two 
commands `git fetch` and `git merge`, instead of `git pull`, and often make 
extensive use of temporary branches to hold different versions of the project 
so they can be merged in a logical fashion.

The third is how to use a "fork/pull" collaborative workflow instead of the 
"shared repo" model that we've described above. If you end up collaborating on
larger projects, including, for example, the repository [holding all of the 
core Software Carpentry bootcamp lessons](http://github.com/swcarpentry/bc), 
you'll find that most large projects don't allow all collaborators to have push 
access to the main repository, the model that we used above. Rather, each 
collaborator makes a "fork", or a copy of the main repository, on their local 
Github account. They then make changes in branches of their own forks and then 
submit a "pull request" back to the main repository, asking the maintainers of 
the core repository to pull in their changes. In addition to preventing 
mistakes in the core repository, this model also builds in the idea of code 
review, and the discussions surrounding pull requests are often extensive.

Once again, if you'd like to learn more about these or more about git in 
general, check out the book [Pro Git](http://git-scm.com/book).

Why plain text?
---------------

Now that we've discussed many of the things that git can do with files, here's 
a closing word about the difference between plain text and binary files. Plain 
text files are exactly what they sound like - files that contain nothing other 
than text, as in letters, numbers, and (some) basic symbols. Plain text files 
thus lack formatting like font sizes (or even font names), metadata such as 
margin sizes, and fancy features such as comment bubbles, embedded images, and 
anything else other than (you guessed it) text.

The file that we worked with in this lesson was a plain text file, as are most 
files that contain code, such as `.m` or `.R` files that contain code for 
Matlab or R respectively. Other common examples of plain text files include 
`.txt` files containing narrative text (like the README files that come with 
many programs), and `.csv` files, which are actually just plain text files in 
which each "column" of data is separated from the next by a comma (csv actually 
stands for "comma separated values").

Plain text files have two major advantages for our purposes. First, being a 
simple and standard format, plain text can be read by almost any program. As a 
corollary, the ubiquitous nature of plain text means that it is likely to 
outlive all of those other proprietary file formats in the future. Second, with 
specific regard to git, plain text files are very easy to compare to each 
other. In other words, it's relatively easy for a program (like the command 
line `diff` program that we used above) to open two plain text files and find 
the differences between them simply by comparing, line by line, the contents of 
each file. This is much harder, if not impossible, to do for more complex file 
formats.

This type of line-by-line comparison is not possible for binary files, which 
for these purposes is the "opposite" of a plain text file. Binary files are 
files, like an image, that cannot be converted into any sort of textual 
representation. Because they cannot be diff-ed, version control is somewhat 
less useful for binary files, although it can still help greatly with headaches 
1, 3, 5, and 6 above.

Somewhere in between plain text and binary files are markup files like xml 
files, html files, the IPython notebook files, Microsoft's docx format, etc. 
These are technically plain text files, but ones that contain many other 
characters (beyond the actual important content, in an intellectual sense) that 
control how the content of the file is displayed and rendered. As plain text 
files, version control can "see inside" of these, but it often does a poor job 
at comparing them to each other due to the presence of all of those additional 
characters and how they are updated when you change the important content of 
the file.

A final note on writing papers
------------------------------

Personally, I've found that one of the most useful applications of version 
control is to manage revisions to my papers. Revising manuscripts represents a 
great example of a process in which you're likely to have multiple versions of 
parts of a file (i.e., the long and the short Methods version, the dissertation 
vs. the submission version) that you need to assemble repeatedly in different 
orders and combinations (i.e., as you submit your manuscript to the fourth 
journal). This makes papers a great candidate for version control. However, 
these benefits really become most apparent only when you're using plain text 
files - that it, when you've written your papers in plain text (not in Word).

If you already use LaTeX, then you're all set - go forth and use git! (Side 
tip: if you are planning to use LaTeX for your UC Berkeley dissertation, check 
out the [ucbthesis](http://math.berkeley.edu/~vojta/ucbthesis/) class file and 
documentation).

If you usually write your papers in Word, but work in a field in which your 
papers really only involve text (i.e., no or very few figures, tables, or 
equations), then I would suggest trying out the very simple markup language 
called Markdown, which will allow you to write your manuscripts in plain text 
with some basic, minimum formatting tags. Overall, it's very easy to use 
Markdown for writing, and there's a great command line program called 
[pandoc](http://johnmacfarlane.net/pandoc/) that will convert Markdown to Word 
(and other formats) when you need to.

If you don't fall into either of these camps, version control can still help 
you keep track of your manuscripts as "blobs" - this just means you won't be 
able to do the diff and merge work that we've discussed. If are willing to make 
an effort to switch your writing to plain text, and especially if you plan on 
writing lots of equations in the future, I would recommend that you invest the 
time to learn LaTeX - it has a somewhat steep learning curve, but you're very 
likely to be pleased with the results in the long term. LaTeX is especially 
good for managing and formatting large documents, like dissertations, which is 
an area where Word often falls short.
