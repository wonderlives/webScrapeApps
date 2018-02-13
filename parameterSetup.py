### 
# Set-up for parameters used in this data mining project
# Author: Roger Ren
# Date: 02/11/2018
###

# import lib
import os

# Get current working directory
currentDir = os.path.dirname(os.path.realpath(__file__))

##############SCRAPE PARAMETERS##############
#start_file = os.path.join(current_dir, "start-urls.txt")
maxGlobalRequest = 2000 
max_details_per_listing = 9999

# Threads
max_threads = 200

# Logging & Storage
log_stdout = True
image_dir = "/tmp/crawl_images"
export_dir = "/tmp"


##############CREDENTIALS##############
# Proxy Credentials
proxyUser = "rogerxren"
proxyPW = "ptid6Ilm"
proxyPort = "60099"
proxySocks = "61336"

# Redis
redisHost = "test-001.6lkeyx.0001.usw2.cache.amazonaws.com"
redisPort = 6379
redisDb = 0

# Database Credentials
dBSever = "amazonscrape.culx5fq06xwk.us-west-2.rds.amazonaws.com"
dBUser = "roger"
dBPw = "supercrazy123"
dBCurrDb = "AmScrap"