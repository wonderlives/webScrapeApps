# import related libs
import os
import random
import datetime
import eventlet
from bs4 import BeautifulSoup #bs4
from requests.exceptions import RequestException

# import self-built libs
import parameterSetup   
from proxySetup import getRandomProxy       
import redisSetup       
from headerSetup import getRandomHeader

# over-write requests and time for coroutine process
requests = eventlet.import_patched('requests.__init__')
time = eventlet.import_patched('time')

# set-global request count
globalRequest = 0

# Retrive all needed pieces.
redis = redisSetup.redis
maxGlobalRequest = parameterSetup.maxGlobalRequest

def mRequest(url, doParse=False):

    # Get random header and proxy
    proxy = getRandomProxy()
    header = getRandomHeader()

    # just in case
    global globalRequest
    if globalRequest >= maxGlobalRequest:
        raise Exception("Reached the max number of requests: {}".format(settings.max_requests))

    # make request
    try:
        response = requests.get(url, headers=header,proxies=proxy) 
    except RequestException as e:
        print('Something went wrong, cannot get response')
        #return mRequest(url)
    globalRequest += 1

    # Analyze response
    if response.status_code != 200:
        print('Wrong code', response.status_code)
        return 

    if doParse:
        return BeautifulSoup(response.text), response.text

    itemAsin = url[39:52]

    return response, itemAsin

# https://api.ipify.org?format=json
# print r.text
#age.findAll("div", "bxc-grid__image")

def reviewParse(response, itemAsin):
    result = []
    soup = BeautifulSoup(response.text)
    reviews = soup.find_all(attrs={"data-hook": "review"})
    reviewLastpage = soup.find_all(attrs={"data-reftag":"cm_cr_arp_d_paging_btm"})[-1].get_text()
    print reviewLastpage
    for review in reviews:

        reviewID    = review['id']
        asin        = itemAsin
        reviewTitle = review.find(attrs={"data-hook":"review-title"}).get_text()
        reviewDate  = review.find(attrs={"data-hook":"review-date"}).get_text()[3:]
        reviewUser  = review.find("a", attrs={"data-hook": "review-author"}).get_text()
        reviewStars = review.find(attrs={"data-hook":"review-star-rating"}).get_text()[:3]
        reviewBody  = review.find(attrs={"data-hook":"review-body"}).get_text()
        result.append((reviewID, reviewTitle, reviewDate, reviewUser, reviewStars, reviewBody ))
    return result