import os
import csv
import random
# Get curr directory
current_dir = os.path.dirname(os.path.realpath(__file__))
# print(current_dir)

with open((current_dir + '/ProxiesList.csv'), 'rb') as f:
    reader = csv.reader(f)
    proxyList = list(reader)
    proxyList = [ip[0] for ip in proxyList]

# print proxyList
proxyUser = "rogerxren"
proxyPW = "ptid6Ilm"
proxyPort = "60099"


# generate proxy
def getRandomProxy():
    # choose a proxy server to use for this request, if we need one
    # if not settings.proxies or len(settings.proxies) == 0:
    #     return None
    proxyIp = random.choice(proxyList)
    proxyUrl = "socks5://{user}:{passwd}@{ip}:{port}/".format(
        user=proxyUser,
        passwd=proxyPW,
        ip=proxyIp,
        port=proxyPort,
    )
    return {
        "http": proxyUrl,
        "https": proxyUrl
    }
# print(getRandomProxy())