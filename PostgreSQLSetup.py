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

# Run Only Once !!!!
if __name__ == '__main__':

    # Item information table
    cur.execute("DROP TABLE IF EXISTS itemInfo")
    cur.execute("""CREATE TABLE itemInfo (
        id          serial PRIMARY KEY,
        title       varchar(2056),
        product_url varchar(2056),
        listing_url varchar(2056),
        price       varchar(128),
        primary_img varchar(2056),
        crawl_time  timestamp
    );""")

    # Item review table
    cur.execute("DROP TABLE IF EXISTS itemReview")
    cur.execute("""CREATE TABLE itemReview (
        id          serial PRIMARY KEY,
        title       varchar(2056),
        product_url varchar(2056),
        listing_url varchar(2056),
        price       varchar(128),
        primary_img varchar(2056),
        crawl_time  timestamp
    );""")

    # Item NLP table
    cur.execute("DROP TABLE IF EXISTS itemNLP")
    cur.execute("""CREATE TABLE itemNLP (
        id          serial PRIMARY KEY,
        title       varchar(2056),
        product_url varchar(2056),
        listing_url varchar(2056),
        price       varchar(128),
        primary_img varchar(2056),
        crawl_time  timestamp
    );""")
    conn.commit()