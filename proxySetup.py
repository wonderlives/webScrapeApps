import parameterSetup
import csv
import random

# Retrive credentials from parameterSetup
proxyUser = parameterSetup.proxyUser
proxyPW = parameterSetup.proxyPW
proxyPort = parameterSetup.proxyPort

# Open Proxy csv file
with open((parameterSetup.currentDir + '/ProxiesList.csv'), 'rb') as f:
    reader = csv.reader(f)
    proxyList = list(reader)
    proxyList = [ip[0] for ip in proxyList]


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

# Test:
# print(getRandomProxy())