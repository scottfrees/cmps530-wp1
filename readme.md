# Weekly Project 1
The purpose of this project is largely just to make sure you are able to get your programming environment up and running. 

## Get the project
From your terminal / command line, navigate to a directory where you'd like to store your work.  Then, clone the assignment's github repository and `cd` into the directory to begin working.

```
git clone https://github.com/scottfrees/cmps530-wp1.git
cd cmps530-wp1
```

## Create your environment
Python is a language that uses many third party libraries and dependencies.  It's hard keeping track of them all, so most developers use *environments* to isolate their projects from each other, and keep their dependencies in one project from interfering with another.  We use Anaconda for this - and you should create a new environment for every project you start in this course.  Alternatively, you can create one for the entire semester, and just re-activate it each time you start a project - it's your choice.  Best practice is to use separate environments however.

```
conda create --name weekly1 python=3.7
```

## Install dependencies
You should have installed Python 3 using Anaconda.  Once installed, you have a `conda` command on your command prompt / terminal which will allow you to install additional libraries.

In your project template file, you'll notice that most of the code I provided you centers around commenting what you should be doing - **however** - I did provide a very small amount of code that creates a bar graph of the data.  This bar graph is drawn with `plotly`.  You won't be able to run your program correctly unless you install this.  Use the following command to do so:

```
conda install plotly
```

## Get the data
The git repository has `.dvc` files, you just need to pull the data to get the actual data set associated with this project.

```
dvc pull
```

*The project uses our standard AWS data repository, make sure you've configured your [dvc installation](https://pages.ramapo.edu/~sfrees/courses/cmps530/dvc.html) so you can pull the data.*

## Analyze the Data
Your primary task in this assignment is to compute the average, minimum, and monthly monthly rainfall in NJ from 1700-2000 and to create a bar chart to visualize it.  You don't need to do much to create the bar chart - I've provided most of the work for that - but computing average, minimum, and maximum is all you.

**Please open `analysis.py` and read my comments carefully, which explains the requirements for the program in detail.**

## Cleaning the Data
As we will discuss many times throughout the semester, data is rarely in great shape.   For this project, I've given you a file containing the average monthly rainfall in the state of New Jersey for every year from 1700 to 2000 (hint... [I made this data up](https://www.socscistatistics.com/utilities/normaldistribution/default.aspx)). Each year is written on a single line - which makes it pretty easy to calculate the average, maximum, and minimum - except some lines will have words, not numbers.  You'll also call an `add_to_plot` function (we'll cover these next week) that the script uses to eventually draw a bar graph.

The tricky part is that some lines have -1, some are blank, and some lines say "unavailable".  For whatever reason, there is no data available for these years - and there wasn't a well agreed upon standard way of representing "no data".  In these cases, you should make sure you call `add_to_plot` with 0 for the year - so the bar graph will contain the missing year.  **You should not** include the missing year in your calculation of the average, minimum, or maximum however.

## Checking your work
Sometimes checking that your analysis is accurate is challenging - and we'll discuss this a lot during the remainder of the semester.  For this project, it's easy to know if you are correct!

```
Average Rainfall: 4.204456140350879
Maximum Rainfall: 9.57
Minimum Rainfall: 0.06
```
<img src="https://pages.ramapo.edu/~sfrees/courses/cmps530/weeks/rainfall.png"/>

## Submitting your work
This project is not graded, you should complete this as soon as possible however, and if you are unable to get the work done - please ask me for help.  I am also happy to review your code and provide feedback, just ask!

## Takeaways
Consider the following questions:
- What changes would you recommend to make this data easier to work with?
- What changes would you recommend to make this data more independent and self-describing?

