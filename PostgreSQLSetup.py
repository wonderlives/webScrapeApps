# 3 Tables:
#	- Item information table: 
#	- Item review table:
#	- Item NLP table:

import parameterSetup
import psycopg2

# Retrive credentials from parameterSetup
dBSever = parameterSetup.dBSever
dBUser = parameterSetup.dBUser
dBPw = parameterSetup.dBPw
dBCurrDb = parameterSetup.dBCurrDb

# Connect to AWS PostgreSQL
conn = psycopg2.connect(host=dBSever, user=dBUser, password=dBPw, dbname=dBCurrDb)
cur = conn.cursor()

if __name__ == '__main__':

    # Drop, Drop, Drop them all!!!!
    cur.execute("DROP TABLE IF EXISTS itemReview")
    cur.execute("DROP TABLE IF EXISTS itemInfo")
    cur.execute("DROP TABLE IF EXISTS itemNLP")

    # Item information table
    cur.execute("""CREATE TABLE itemInfo (
        asin        varchar(10) PRIMARY KEY,
        itemTitle   text,
        itemPrice   real,
        itemRating  real,
        reviewCounts integer,
        crawlTime   timestamp
    );""")

    # Item review table
    cur.execute("""CREATE TABLE itemReview (
        reviewID    varchar(14) PRIMARY KEY,
        asin        varchar(10) REFERENCES itemInfo(asin),
        reviewTitle text,
        reviewBody  text,
        reviewDate  date,
        reviewUser  text
    );""")

    # Item NLP table
    cur.execute("DROP TABLE IF EXISTS itemNLP")
    cur.execute("""CREATE TABLE itemNLP (
        id          serial PRIMARY KEY,
        title       varchar(2056),
        crawl_time  timestamp
    );""")

    # Commit
    conn.commit()