#!/usr/bin/python3
"""Project of a log analyser using the 'news' database.
   Part of Udacity Fullstack Developer Nanodegree"""

import psycopg2


def get_results_from_query(query):
    """Generic method to make a database query in the news DB"""
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def get_most_popular_articles():
    """This method's target is to answer the first question:
    What are the most popular articles of all time?
    The method executes a database query and returns the result to the user"""
    query = """SELECT a.title,count(*) AS num_views FROM articles AS a, log AS l
    WHERE l.path LIKE '%' || a.slug || '%' GROUP BY a.title
    ORDER BY num_views DESC LIMIT 3;"""
    return get_results_from_query(query)


def get_most_popular_author():
    """This method's target is to answer the second question:
    Who is the most popular article author of all time?
    The method executes a database query and returns the result to the user"""
    query = """SELECT au.name,cnt.num_views FROM authors AS au,
    (SELECT a.author,count(*) AS num_views FROM articles AS a,
    log AS l WHERE l.path LIKE '%' || a.slug || '%' GROUP BY a.author
    ORDER BY num_views DESC) AS cnt WHERE au.id = cnt.author;"""
    return get_results_from_query(query)


def get_days_with_errors():
    """This method's target is to answer the third question:
    On which days did more than 1% of request lead to errors?
    The method executes a database query and returns the result to the user"""
    query = """SELECT t.day,CAST(e.err AS FLOAT)/t.tot as pct FROM
    total_requests as t, error_requests as e
    WHERE e.d = t.day GROUP BY t.day, e.err, t.tot
    HAVING CAST(e.err AS FLOAT)/t.tot > 0.01;"""
    return get_results_from_query(query)


if __name__ == "__main__":
    print("Log Analysis Project - Let's Answer the questions:")
    print("\t1-What are the most popular three articles of all time?")
    popular = get_most_popular_articles()
    print("\t\tA:The most viewed articles are:")
    for article in popular:
        print("\t\t\t", article[0], "with", article[1], "views")

    print("\t2-Who are the most popular article authors of all time?")
    authors = get_most_popular_author()
    print("\t\tA: The most popular authors are:")
    for author in authors:
        print("\t\t\t", author[0], "with", author[1], "article views")
    print("\t3-On which days did more than 1% of requests lead to errors?")
    days = get_days_with_errors()
    print("\t\tA: On the following days:")
    for day in days:
        formated_day = day[0].strftime("%B %d, %Y")
        formated_percentage = "{:.2f}".format(day[1]*100) + "%"
        print("\t\t\t", formated_day, "with",
              formated_percentage, "of them as errors")
