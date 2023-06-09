# OfficePythonProgramming
This repository contains five project reports for the modul: 'Office Application Programming'. </br>

The characteristics of the modul are:

    learn VBA basic functionalities
    learn Python as alternative to VBA and Excel
    first steps in analyzing Datasets and working with them             

The valuation of the course consist of five individual projects. Every project is based on a indiviual dataset.
The indivual projects are collected / documented in an data report, which keeps track of all projects. The complete report is deliveried as part of the fifth project.

Every project is verbally and codevise documented in this repository. The full report can't be published on here due to data protection reasons, but to still provide some context to the task a content section was added to every project. This section contains an excerpt or further explanation for every project.

*Note:* To run the writte code without any issues, a 'requirements.txt'-file was initialized to create an virtual environment.

## First Project: First Touch
|||
|--|--|
|Time Estimated|*3 to 5 hours*|
|Current State|*completed*|
|Actuael Time|*4.5h*|
|Reference|*Project/1_Task*|

### Task

    1. Analyse and understand the structure and content of a choosen dataset.
    2. Write a short report about the dataset and the article.

### Content

In the first project the student has to unterstand what the dataset is about. Every dataset is related to an article written by authors of FiveThirtyEight.
In this case the article was about the acceptans of Robert Mueller and his work as special counsel in the "Report On The Investigation Into Russian Interference In The 2016 Presidential Election".

In 2016 the American presidental election was the biggest political event. The decision was beetween Donald Trump and his opponent Hillary Clinton. 
During the elecation russian hackers tried to manipulate voters on social platforms to positively effect votes for Donald Trump.<br>

Because of rising Accusations against the manipulation, a special force was formed to investigate this. The head of this special force, was Robert Mueller. 
He was reponsible for this investigation. 

In the related article "Both Parties Think The Mueller Report Was Fair. They Just Completely Disagree On What It Says." written by Dhrumil Mehta discussed the results and reactions of the two parties.
To sum things up, the article shows that, both Republicans and Democrats think the article was fair, but the interpretation is completly different. Republican think, that the report discharge Trump of any responsibility. Democrats think the complete opposite and demand further actions.

This opion formation is also pictured in the given dataset, that was created as part of the article (https://github.com/fivethirtyeight/data/tree/master/mueller-polls). The dataset contains every job approval poll of Robert Mueller between start (2017) and end (2019) in his job as special councel.

## Second Project: Database Design

|||
|--|--|
|Time Estimated|*5 to 7 hours*|
|Current State|*completed*|
|Actuael Time|*7h*|
|Reference|*Project/2_Task*|

### Task

    1. Use your given dataset and create an Entity-Relationship-Model (ERM).
    2. Use the ERM to create an relational SQL-Database.

### Content
The SQL-Database was design with the Entity-Relationship modelling language and the use of the simple Chen-Notation as well as the Min-Max-Notation. After designing the database was setup and filled and referenced with in SQL Server. The related script is written in T-SQL.

## Third Project: Categorize Data

|||
|--|--|
|Time Estimated|*no time estimate*|
|Current State|*completed*|
|Actuael Time|*16h*|
|Reference|*Project/3_Task*|

### Task

    1. Optimization of the current Database by
        a. Adding Surrogatekeys
        b. Checking for third normal form and ressource use optimization

    2. Create at least three categorized variables with python

### Content

In this task the occured to redesign the existing database of the second project. As extra, Surrogatekeys where added.

This second task of the third project can be seen as main task. The task contencs two subtask. First one develop three possible categories for certain attributes in the datbase. Second part: Write a python script to categorize the data and insert the categories into your database as extra attributes. <br>

Firt of all: What is meant with categories?
In this case categories mean, that you take an existing attribute of your database like Shirt Colours and aggregate them. For example Shirt colours can be green, dark-green, blue, light-blue and so on. Then you can categorize this colours in the categories green (green, dark-green) and blue (light-blue). Thats an example for a simple categorization.

The attributes and the transformed variables based on them were selected as shown below: Quarter, absolute/decrease or increase and sample size.

The category Quarter is used to categorize dates.

Accordingly, a timeline with specific dates, months or years can be created. With quarters, this is also possible, but only through an extremely cumbersome SQL query. The categorization of dates into quarters enables the opinions of the respondents to be captured in a more granular way than with years, but still aggregated than with months. The categorization comes from the economic sector but is also used in statistical analyses to better understand developments (see OECD, 2011, pp. 63 ff).

The classic categorization is from Quarter 1 to Quarter 4 and can then be evaluated with the year. The transformed variable is applied to the Start and End attributes. The second transformed variable is the absolute increase or decrease. In the dataset, there are four different attributes that represent the opinions of the respondents in percentage from 0 to 100, as shown in the following excerpt:

To convert this data into a transformed variable, the approach of absolute majority was chosen. This comes from politics and states that an absolute majority is achieved when "the voting result is at least one vote above half of all members of parliament" (German Bundestag, n.d.). Since the values are not absolute but relative, this approach was only used as a principle for categorization.

For the categorization of the voting results, a result was considered an absolute majority if it is equal to or above 51 percent. Conversely, all results below 50 percent were categorized as an absolute minority. Results equal to 50 percent were categorized as Undecided. This categorization makes it possible to make immediate statements, for example, about the majority or minority of respondents who agree or disagree with a particular question. The overall picture of the opinions can be presented in an aggregated form, which may bring about new insights.

The categorization of Majority, Minority, and Undecided can be applied to the Approve, Disapprove, ApproveRepublican, and ApproveDemocrats attributes. An application to the Unsure attribute is conceivable but was not initially considered due to its lower informative value compared to the Approve or Disapprove positions.

The last attribute refers to the sample size. To evaluate the sample size not only numerically but also verbally, a grading was established. The evaluation of the sample size is useful because its size directly determines the validity of the results. The larger the sample, the less influence chance events have on the results (see Rüschemeyer, 2020). Accordingly, the sample size was divided into the categories small, medium, and large. The division of the limits is based on a box-whisker plot (see Appendix C). Based on the lower and upper quartiles, the following threshold values ​​were defined:

The 'low' categorization is applied when a sample contains less than 1000 respondents. The 'medium' category is applied when a sample contains between 1000 and under 1500 respondents. The 'high' category is used when a sample size of more than 1500 is present.The categorization of small, medium, and large can be used to evaluate the validity of the surveys in a more precise manner. Additionally, results with a small sample size can be better filtered to increase the validity of other statistical analyses.


## Fourth Project: Optimize Database and preparation with pandas lib

|||
|--|--|
|Time Estimated|*no time estimate*|
|Current State|*completed*|
|Actuael Time|*4h*|
|Reference|*Project/4_Task*|


### Task

    1. Last chance to optimize the database design
        a. Complete third normal form based optimizations
        b. Design the database as resources considerated as possible
    2. Get in touch with the functionalities of possibilities of the pandas lib.

### Content

The background of this task was to get more in touch with pandas and gain confidients in it's use. The dataset was import and new findings were made. Just a little task to play around.

## Fifth Project
|||
|--|--|
|Time Estimated|*no time estimate*|
|Current State|*in progress*|
|Actuael Time|*28h*|
|Reference|*Project/5_Task*|

### Task

    1. Mathplotlib / Seaborn
        a.  Visualize a choosen part of your dataset with axes
            1. First has to be an Heatmap
            2. Second can be individually choosen
            3. Third can be everything except Scatterplot, bar chart or line diagramm
        b. export and interpret the results contentwise

### Content


