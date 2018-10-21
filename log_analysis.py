#!/usr/bin/env python3

import psycopg2

"""
The app will loop through dictionary below and query each question in database
to generate a TXT file with all questions and their results.
"""

questions = [
    {
        "title": "Question 1",
        "query": """
                 select * from authors;
                 """,
        "suffix": "views"
    },
    {
        "title": "Question 2",
        "query": """
                 select * from articles;
                 """,
        "suffix": "results"
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
                rows = getAnalysis(question["query"])
                file.write("{}) {}\n\n".format(index + 1, question["title"]))
                for row in rows:
                    file.write("{} - {} {}\n"
                               .format(row[0], row[1], question["suffix"]))
                file.write("\n\n")

            print("File '{}' successfully saved.".format(filename))
    except IOError as err:
        filename = ""
        print("I/O error: {}".format(err))


if __name__ == "__main__":
    main()
