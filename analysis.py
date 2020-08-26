##################################################################
## The following are libraries, variables, and functions to be used
## below, do not change them in any way.  We will be learning
## more about tuples, lists, functions, pandas, and plotly later
## in the semester.
##################################################################
import plotly.express as px
import pandas as pd

chart = []


def add_to_chart(year, rainfall):
    chart.append((year, rainfall))


def draw_chart():
    df = pd.DataFrame(chart, columns=["year", "rainfall"])
    fig = px.bar(df, x="year", y="rainfall")
    fig.write_html("rainfall.html")
    print(
        "rainfall.html has been created, you can open it with a web browser to see the resulting chart"
    )


##################################################################
# Step 1:  Open rainfall.data in read mode, and store the file
#          in a variable
##################################################################
your code here...

##################################################################
# Step 2:  Variable initialization.  You should create a [year]
#          variable, initialized to 1700 and increment it after
#          reading each line.  You will likely want
#          to create other variables to help you calculate the
#          average, minimum, and maximum as well.
##################################################################
your code here...

##################################################################
# Step 3:  Use a [for] loop to iterate over each line in the file.
#          Note that each line will be presented to you as a string,
#          with new line (\n) at the end.
#
#          To calculate average, you might want to keep a running
#          sum of all rainfall, and a running count of all rainfall
#          lines you've read - which can be used at the end to compute
#          average.
#
#          To calculate minimum, you could initialize a minimum variable
#          to some very large number, and then on each line, see if
#          the current rainfall value is less than your minimum variable,
#          and if it is, simply reset the minimum to the current value.
#          You can use a similar approach for maximum.
#
#          You will need to check for lines with nothing, -1,
#          or unavailable, and be careful not to include that
#          data in your average / max / min calculation.
#
#          IMPORTANT:  Preparing for charts
#          ----------------------------------------------------
#          If the data is missing, you should call add_to_chart
#          with a 0:
#
#          add_to_chart(year, 0)
#
#          If the data is present, convert it to a float and store
#          the numeric value in a variable (i.e. rainfall), and
#          call add_to_chart with the year and the actual data.
#
#          add_to_chart(year, rainfall)
##################################################################
your code here...

##################################################################
## Step 4:  Output the average, maximum, and minimum rainfall to
##          an output file named rainfall.out.  Print each value
##          on a single line - average, maximum, then minimum.
##          Do not label the data - simply output the number on
##          each line.
##################################################################
your code here...

##################################################################
# This function saves a bar graph in an html file
# called rainfall.html
draw_chart()
