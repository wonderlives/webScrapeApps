import parameterSetup
import redis

# Acqure credentials from parameterSetup 
redisHost = parameterSetup.redisHost
redisPort = parameterSetup.redisPort
redisDb = parameterSetup.redisDb

# Create Redis
redis = redis.StrictRedis(host=redisHost, port=redisPort, db=redisDb)

# Test Redis Working
# for i in range(10):
#     redis.sadd("testItem", i)
#     redis.sadd("testItem2", i+200)
#     k = redis.spop("testItem")
#     print(k.decode('utf-8'))
#     k = redis.spop("testItem2")
#     print(k.decode('utf-8'))

# Add
def addToRedis(url):
    item = url
    return redis.sadd("Col", item)


# Pop
def removeFromRedis():
    return redis.spop()


##### COME BACK LATER FOR BETTER 