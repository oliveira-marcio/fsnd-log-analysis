#!/usr/bin/env python3

import psycopg2

"""
The app will loop through dictionary below and query each question in database
to generate a TXT file with all questions and their results.
"""

questions = [
    {
        "title": "What are the most popular three articles of all time?",
        "query": """
                 select title, count(*) as views
                 from articles, log
                 where ('/article/' || slug) = path
                 group by 1
                 order by 2 desc
                 limit 3
                 """,
        "suffix": " views"
    },
    {
        "title": "Who are the most popular article authors of all time?",
        "query": """
                 select aut.name, count(*) as views
                 from authors aut, articles art, log
                 where ('/article/' || art.slug) = log.path
                 and aut.id = art.author
                 group by 1
                 order by 2 desc
                 """,
        "suffix": " views"
    },
    {
        "title": "On which days did more than 1% of requests lead to errors?",
        "query": """
      select to_char(date_trunc('day', time), 'FMMonth FMDD, FMYYYY') as date,
      trunc(cast(100*(count(*)::float / totals.total) as numeric), 2) as ratio
      from log,
           (select date_trunc('day', time) as date, count(*) as total
            from log group by 1) as totals
      where log.status not like '200%'
      and date_trunc('day', log.time) = totals.date
      group by 1, totals.total
      having (count(*)::float / totals.total) > 0.01
                 """,
        "suffix": "% errors"
    }
]


def getAnalysis(query):
    DBNAME = "news"
    db = psycopg2.connect(dbname=DBNAME)
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def main():
    filename = "analysis.txt"
    try:
        with open(filename, mode="w") as file:
            for index, question in enumerate(questions):
                print("Fetching results ({}/{})...".format(
                    index + 1, len(questions)))
                rows = getAnalysis(question["query"])
                file.write("{}) {}\n\n".format(index + 1, question["title"]))
                for row in rows:
                    file.write("{} - {}{}\n".format(
                        row[0], row[1], question["suffix"]))
                file.write("\n\n")

            print("\nFile '{}' successfully saved.".format(filename))
    except IOError as err:
        filename = ""
        print("I/O error: {}".format(err))


if __name__ == "__main__":
    main()
