# Log Analysis Project

Python code to answer three questions based on the news database. This is an assignment from Udacity Fullstack Web Developer Nanodegree.
The database generation commands are inside "newsdata.sql", and they expect the role 'vagrant' to work.
The questions this program answers are:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The database created represents a blog website and is made of three tables:articles, authors and log.
The first is a collection of full articles and references the authors, present in the authors table.
The log tells us the user behaviour, indicating when each page was accessed.

The output.txt file contains the program output.

## Where do I get it?
The main repository of this code is [here](https://github.com/marph13/log_analysis).
Feel free to clone or fork it!
```
git clone https://github.com/marph13/log_analysis.git
```

## How do I run it?
First make sure you postgresql have a database named news with the structure created by
newsdata.sql, so unpack it and just run:
```
psql -d news -f newsdata.sql
```

Then, check for the psycopg2 python module:
```
pip3 install psycopg2
```
The third question used some subqueries, so I created a view for each of them:
```
CREATE VIEW total_requests AS SELECT date(time) AS day, count(*) AS tot FROM log GROUP BY day;
CREATE VIEW error_requests AS SELECT date(time) AS d, count(*) AS err FROM log WHERE status != '200 OK' GROUP BY d;
```

After the views creation you may run the code with Python 3:
```
python3 analyser.py
```

## Resources used on the project:
The database generation script is from Udacity Fullstack Developer Nanodegree, please ask them if you want to use or reproduce it in any way.

## License
The contents of this repository are under the [MIT License](https://github.com/marph13/log_analysis/blob/master/LICENSE)
