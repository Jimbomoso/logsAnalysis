# Logs Analysis Project 

## Description:

This is a project from my [Udacity Full Stack Development Nanodegree Program.][1]

---

#### Udacity's Project Prompt:

> You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

> The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

> The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

#### Udacity's why this project?

> In this project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data.

#### Report generation

> Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity we collect logs to help us measure student progress and the success of our courses. The reporting tools we use to analyze those logs involve hundreds of lines of SQL.

#### Database as shared resource

> In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

---
## How to use:

1. Install [PostgreSQL][2] and [Python][3] if not installed
2. Download report.py, newsdb.py and newsdata.sql into a local folder
3. Load newsdata.sql into PostgreSQL database by typing this in the terminal: 
   
    `psql -d news -f newsdata.sql`
4. Run report.py by typing this in the terminal: 
   
    `python3 reporty.py`

### Result:

Report printed: 

 1. What are the most popular three articles of all time?
    * "Candidate is jerk, alleges rival" - 338647 views
    * "Bears love berries, alleges bear" - 253801 views
    * "Bad things gone, say good people" - 170098 views
 2. Who are the most popular article authors of all time?
    * "Ursula La Multa" - 507594 views
    * "Rudolf von Treppenwitz" - 423457 views
    * "Anonymous Contributor" - 170098 views
    * "Markoff Chaney" - 84557 views
1. On which days did more than 1% of requests lead to errors?
    * "Jul 17, 2016" - 2.26 errors
  
[1]: [http:udacity.com](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044)
[2]: [https://www.postgresql.org/download/]
[3]: [https://www.python.org/downloads/release/python-374/]