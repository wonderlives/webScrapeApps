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
max_requests = 2 * 10**6  # two million
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

# Redis
redisHost = "test-001.6lkeyx.0001.usw2.cache.amazonaws.com"
redisPort = 6379
redisDb = 0

# Database Credentials
dBSever = "amazonscrape.culx5fq06xwk.us-west-2.rds.amazonaws.com"
dBUser = "roger"
dBPw = "supercrazy123"
dBCurrDb = "AmScrap"
##############HEADERS##############
# Request
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
}
allowed_params = ["node", "rh", "page"]