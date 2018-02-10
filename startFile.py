import os

# Get curr directory
current_dir = os.path.dirname(os.path.realpath(__file__))
print(current_dir)

# Content Storage (SQL/NoSQL Database)
database = "amazon_crawler"
host = ""
user = ""

# URL Cache (Redis Cache system)
redis_host = ""
redis_port = 6379
redis_db = 0

# Proxies Set-up
proxies = [
    # your list of proxy IP addresses goes here
    # check out https://proxybonanza.com/?aff_id=629
    # for a quick, easy-to-use proxy service
]
proxy_user = ""
proxy_pass = ""
proxy_port = ""

# Crawl Parameters
start_file = os.path.join(current_dir, "start-urls.txt")
print(start_file)
max_requests = 2 * 10**6  # two million
max_details_per_listing = 9999
max_threads = 200
log_stdout = True
image_dir = "/tmp/crawl_images"
export_dir = "/tmp"