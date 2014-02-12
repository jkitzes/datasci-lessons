## Justin Kitzes | Data Science Lessons

This repo contains lesson materials developed by Justin Kitzes for teaching 
data science skills to scientists. The lessons can be used as self-paced 
tutorials or as teaching materials for live workshops.

If you are interested in reviewing the lesson materials, you can find all of 
the lessons nicely rendered at the [GitHub pages site for this 
repo](http://jkitzes.github.io/datasci-lessons/). Feel free to use this site 
for personal use or teaching.

If you are a Software Carpentry instructor and want to use these lessons in a 
bootcamp, begin by creating a repo for your bootcamp following the [usual 
instructions](http://github.com/swcarpentry/bc/). Then, from within your local 
copy of your bootcamp repo, run the commands

    $ git remote add jkitzes https://github.com/jkitzes/datasci-lessons.git
    $ git fetch jkitzes
    $ git checkout -b datasci jkitzes/gh-pages
    $ git mv README.md README2.md
    $ git mv index.md index2.md
    $ git commit -am "Avoid conflicts"
    $ git checkout gh-pages
    $ git merge datasci

The first three commands fetch data from this repo and create a local branch 
containing these lessons. The next three commands rename the README and index 
files in an attempt to avoid a merge conflict later. The final two commands 
merge these lessons into the main `gh-pages` branch of your bootcamp repo (if 
there are other conflicts during this merge, you'll need to resolve them).

You'll now have all of the lessons from this repo in your bootcamp repo, and 
they should build in your bootcamp's `gh-pages` branch without any additional 
modification. See the page that is now `index2.html` for a reminder of the 
location of each lesson and its supporting files.

If you have questions, suggestions, or corrections, please feel free to raise 
an issue or [contact me](mailto:jkitzes@berkeley.edu) directly.
